import logging
from pyspark.sql.window import Window
from pyspark.sql.functions import *
from .data_processor import save_to_s3


logging.basicConfig(level=logging.INFO)

BASE_PATH = 's3a://vehicle-telemetry-project/processed'

def rolling_metrics(data):
    logging.info("Calculating rolling metrics on cleaned data...")
    # Defining window function.
    window_function = Window.partitionBy \
        ('deviceID').orderBy('timeStamp') \
            .rowsBetween(-10, 0)
    
    # Calculating rolling metrics
    data = data.withColumns({
        'rolling_avg_speed' : round(avg('gps_speed').over(window_function), 2),
        'rolling_avg_temp' : round(avg('cTemp').over(window_function), 2),
        'rolling_std_temp' : round(coalesce(stddev('cTemp').over(window_function), lit(0)), 2)
    })
    logging.info("Rolling metrics calculated...")
    return data


def lag_features(data):
    logging.info("Calculating lag features...")
    # Defining window function for lag features
    lag_window = Window.partitionBy('deviceID').orderBy('timeStamp')
    
    # Previous speed and temperature
    data = data.withColumns({
        'previous_speed': round(coalesce(lag('gps_speed').over(lag_window), lit(0)), 2),
        'previous_temperature': round(coalesce(lag('cTemp').over(lag_window), lit(0)), 2)
    })
    logging.info("Lag features calculated...")
    return data


def rate_calculations(data):
    logging.info("Performing rate calculations...")
    #Defining window function for rate calculations
    lag_window = Window.partitionBy('deviceID').orderBy('timeStamp')

    data = data.withColumns({
        # Changes
        'speed_change': round(col('gps_speed') - col('previous_speed'), 2),
        'temperature_change': round(col('cTemp') - col('previous_temperature'), 2),
        # Lag values
        'previous_battery': round(coalesce(lag("battery").over(lag_window), lit(0)), 2),
        'previous_time': lag("timeStamp").over(lag_window)
    })

    # Time difference
    data = data.withColumn(
        "time_diff",
        unix_timestamp("timeStamp") - unix_timestamp("previous_time")
    )

    # Battery drain rate
    data = data.withColumn(
        "battery_drain_rate",
        when(col("time_diff") > 0,
             round((col("battery") - col("previous_battery")) / col("time_diff"), 4)
        ).otherwise(lit(0))
    )
    logging.info("Rate calculations finished...")
    return data


def store_timeseries_data(data):
    time_series_df = data.select(
        "tripID",
        "deviceID",
        "timeStamp",
        "gps_speed",
        "battery",
        "cTemp",
        "rolling_avg_speed",
        "rolling_avg_temp",
        "rolling_std_temp",
        "speed_change",
        "temperature_change",
        "battery_drain_rate",
        'year',
        'month',
        'day',
        'hour'
    )
    save_to_s3(time_series_df, 
               dataset_name='timeseries', 
               partition_cols=['year', 'month', 'day', 'hour'],
               s3_path=BASE_PATH
               )


def time_series_analysis(data):
    data = rolling_metrics(data)
    data = lag_features(data)
    data = rate_calculations(data)
    data.cache()
    data.count() 
    store_timeseries_data(data)
    return data