from pyspark.sql.functions import *
from .data_processor import save_to_s3

BASE_PATH = 's3a://vehicle-telemetry-project/processed'

def save_anomaly_dataset(data):
    """
    Saves the anomaly dataset to S3 for further analysis and reporting.
    
        :param data:
            Input DataFrame containing telemetry data with anomaly flags and z-scores.

        :return:
            None
    """
    anomaly_dataset = data.select(
        "tripID", "deviceID", "timeStamp",
        "cTemp", "gps_speed", "battery",
        "engine_overheating",
        "engine_load",
        "speed_spike",
        "battery_drop",
        "fault_flag",
        "temp_z_score",
        "temp_anomaly_flag",
        'year',
        'month',
        'day'
    )
    save_to_s3(anomaly_dataset, 
               dataset_name='anomaly', 
               partition_cols=['year', 'month', 'day'], 
               s3_path=BASE_PATH
               )


def anomaly_detection(data):
    """
    Performs anomaly detection by creating conditional flags for various 
    anomaly types and calculating z-scores for temperature.
    The results are saved to S3 for further analysis and reporting.

        :param data:
            Input DataFrame containing telemetry data(Processed).

        :return:
            DataFrame with anomaly flags and z-scores.
    """
    # Conditional flags
    data = data.withColumns({
        "engine_overheating": when(col('cTemp') > 110, 1).otherwise(0),
        "engine_load": when(col('eLoad') > 85, 1).otherwise(0),
        "speed_spike": when(col('speed_change') > 100, 1).otherwise(0),
        "battery_drop": when(col('battery_drain_rate') >= 2, 1).otherwise(0),
        "fault_flag": when(col("dtc").isNotNull() & (col("dtc") != 0), 1).otherwise(0)
    })

    # Statistical anomaly detection
    stats_data = data.groupBy("deviceID").agg(
        round(avg("cTemp"), 2).alias("mean_temp"),
        round(stddev("cTemp"), 2).alias("std_temp")
    )
    data = data.join(stats_data, on="deviceID", how="left")

    # Temperature z-score
    data = data.withColumn(
        "temp_z_score",
        when(
            col("std_temp") != 0,
            round((col("cTemp") - col("mean_temp")) / col("std_temp"), 2)
        ).otherwise(0)
    )
    
    # Temperature anomaly flag
    data = data.withColumn(
        "temp_anomaly_flag",
        when(abs(col("temp_z_score")) > 2, 1).otherwise(0)
    )
    data = data.repartition('year', 'month', 'day')

    # Save data
    save_anomaly_dataset(data)
    return data