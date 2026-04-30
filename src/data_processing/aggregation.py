import logging
from pyspark.sql.functions import *
from .data_processor import save_to_s3

logging.basicConfig(level=logging.INFO)

BASE_PATH = "s3a://vehicle-telemetry-project/aggregated"

def device_level_aggregation(data):
    logging.info("Device level aggregation started...")
    device_aggregation = data.groupBy("deviceID").agg(
        count("*").alias("total_records"),
        round(avg("gps_speed"), 2).alias("avg_speed"),
        round(avg("battery"), 2).alias("avg_battery"),
        sum(
            coalesce(col("engine_overheating"), lit(0)) +
            coalesce(col("engine_load"), lit(0)) +
            coalesce(col("speed_spike"), lit(0)) +
            coalesce(col("battery_drop"), lit(0)) +
            coalesce(col("temp_anomaly_flag"), lit(0))
        ).alias("anomaly_count"),
        sum(col("fault_flag")).alias("fault_count")
    )
    save_to_s3(device_aggregation,
               dataset_name='device_level',
               s3_path=BASE_PATH
               )
    logging.info("Device level aggregation completed...")
    return device_aggregation


def trip_level_aggregation(data):
    logging.info("Trip level aggregation started...")
    trip_aggregation = data.groupBy('tripID').agg(
        round(avg('gps_speed'), 2).alias('avg_speed'),
        max('cTemp').alias('max_temp'),
        (max('timeStamp').cast('long') - min('timeStamp').cast('long')).alias('trip_duration')
    )
    save_to_s3(trip_aggregation,
               dataset_name="trip_level",
               s3_path=BASE_PATH
               )
    logging.info("Trip level aggregation completed...")
    return trip_aggregation


def time_based_aggregation(data):
    logging.info("Time-based aggregation started...")
    avg_speed_per_hour = data.groupBy('year', 'month', 'day', 'hour') \
        .agg(round(avg('gps_speed'), 2).alias('avg_hourly_speed')
    )
    avg_temp_day = data.groupBy('year', 'month', 'day').agg(
        round(avg('cTemp'), 2).alias('avg_daily_temp')
    )
    save_to_s3(avg_speed_per_hour,
               dataset_name='avg_speed_aggregation',
               partition_cols=['year', 'month', 'day', 'hour'],
               s3_path=BASE_PATH
               )
    save_to_s3(avg_temp_day,
               dataset_name='avg_temp_aggregation',
               partition_cols=['year', 'month', 'day'],
               s3_path=BASE_PATH
               )
    logging.info("Time-based aggregation completed...")
    return avg_speed_per_hour, avg_temp_day


def correlation_metrics(data):
    logging.info("Calculating correlation metrics...")
    cross_metrics = data.select(
        round(corr('gps_speed', 'eLoad'), 2).alias('speed_vs_load'),
        round(corr('cTemp','eLoad'), 2).alias('temp_vs_load'))
    save_to_s3(cross_metrics,
               dataset_name='correlation_matrix',
               s3_path=BASE_PATH
               )
    logging.info("Correlation metrics calculated...")
    return cross_metrics


def daily_averages(data):
    logging.info("Calculating daily averages...")
    daily_avg = data.groupBy("year", "month", "day").agg(
        round(avg("gps_speed"), 2).alias("avg_speed"),
        round(avg("cTemp"), 2).alias("avg_temp"),
        round(avg("battery"), 2).alias("avg_battery")
    )
    save_to_s3(daily_avg,
               dataset_name='daily_average',
               s3_path=BASE_PATH
               )
    logging.info("Daily averages calculated...")
    return daily_avg


def quality_checks(data):
    logging.info("Performing data quality checks...")
    null_counts = data.select([
        count(when(col(c).isNull(), c)).alias(c)
        for c in data.columns
    ])
    total_count = data.count()
    unique_count = data.dropDuplicates().count()
    duplicate_count = total_count - unique_count
    logging.info(f"Total duplicate records: {duplicate_count}")
    logging.info("Quality checks completed...")


def aggregation(data):
    trip_aggregation = trip_level_aggregation(data)
    device_aggregation = device_level_aggregation(data)
    avg_speed_per_hour, avg_temp_day = time_based_aggregation(data)
    daily_avg = daily_averages(data)
    quality_checks(data)              