import logging
from pyspark.sql.types import *
from pyspark.sql.functions import *

logging.basicConfig(level=logging.INFO)

BASE_PATH = 's3a://vehicle-telemetry-project/processed'

def load_data(session, s3_path, schema):
    logging.info("Loading data from s3...")
    spark = session
    df = spark.read.schema(schema).json(s3_path)
    logging.info("Data loaded successfully...")
    return df


def save_to_s3(data, dataset_name, partition_cols=None, s3_path='s3a://vehicle-telemetry-project'):
    full_path = f"{s3_path.rstrip('/')}/{dataset_name}"
    writer = data.write.mode("append")

    logging.info(f"Uploading {dataset_name} to s3({full_path})...")
    if partition_cols:
        writer = writer.partitionBy(*partition_cols)

    writer.parquet(f'{full_path}/')
    logging.info(f"Uploaded {dataset_name} to s3({full_path})...")


def data_cleaning(data):
    # Formatting timestamp column
    logging.info("formatting timeStamp column to proper format...")
    data = data.withColumn(
        "timeStamp",
        to_timestamp(col("timeStamp"), "yyyy-MM-dd HH:mm:ss")
    )

    # Filtering invalid values
    logging.info("Filtering data dropping null values...")
    data = data.filter(
        (col("deviceID").isNotNull()) & 
        (col("timeStamp").isNotNull()) &
        (col("deviceID") != "") &
        (col("gps_speed") >= 0) &
        (col("battery").between(0, 100)) &
        (col("cTemp").between(-40, 150))
    )

    # Dropping duplicates
    logging.info("Dropping duplicate records...")
    data = data.dropDuplicates(['tripID', 'deviceID', 'timeStamp'])

    # Dropping unwanted columns
    logging.info("Dropping unwanted colums from dataframe...")
    data = data.drop('year','month','day','hour')

    # Extracting columns
    logging.info("Extracting time features (hour, day, week, month).")
    data = data.withColumns({
        'hour': hour('timeStamp'),
        'day': dayofmonth('timeStamp'),
        'week': weekofyear('timeStamp'),
        'month': month('timeStamp'),
        'year': year('timeStamp')
    })

    # Enriching data 
    logging.info("Enriching data by categorizing vehicles...")
    data = data.withColumn(
        'vehicle_category', when(col('cTemp') > 90, 'HIGH_TEMP')
        .when(col('battery') < 30, 'LOW_BATTERY')
        .otherwise('NORMAL')
    )
    data = data.repartition('year', 'month', 'day', 'hour')
    
    # Save data
    logging.info("Saving the processed data to s3...")
    save_to_s3(data, 
               dataset_name='cleaned', 
               partition_cols=['year', 'month', 'day', 'hour'],
               s3_path=BASE_PATH
               )
    logging.info("Processed data saved to s3...")
    return data