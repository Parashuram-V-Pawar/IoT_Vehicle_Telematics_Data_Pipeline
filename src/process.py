from pyspark.sql import SparkSession
from src.data_processing.data_processor import *
from src.data_processing.time_series_analysis import time_series_analysis
from src.data_processing.anomaly_detection import anomaly_detection
from src.data_processing.aggregation import aggregation

def create_session(name: str):
    logging.info("Creating spark session...")
    spark = SparkSession.builder \
    .appName(name) \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.aws.credentials.provider",
            "com.amazonaws.auth.DefaultAWSCredentialsProviderChain") \
    .config("spark.jars.packages",
            "org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262") \
    .getOrCreate()
    logging.info("Spark session created successfully...")
    return spark


def main():
    logging.info('Data processing pipeline initiated...')
    spark = create_session(name='IoT vehicle data pipeline')

    schema = StructType([
        StructField("tripID", StringType(), True),
        StructField("deviceID", StringType(), True),
        StructField("timeStamp", StringType(), True),
        StructField("accData", StringType(), True),
        StructField("gps_speed", DoubleType(), True),
        StructField("battery", DoubleType(), True),
        StructField("cTemp", DoubleType(), True),
        StructField("eLoad", DoubleType(), True),
        StructField("iat", DoubleType(), True),
        StructField("dtc", IntegerType(), True),
        StructField("ingestion_timestamp", StringType(), True)
    ])
    logging.info("Data cleaning initiated...")
    data = load_data(spark, s3_path='s3a://vehicle-telemetry-project/raw/', schema=schema)
    clean_data = data_cleaning(data)
    logging.info("data cleaning completed...")

    logging.info("Time series analysis started...")
    processed_data = time_series_analysis(clean_data)
    logging.info("Time series analysis completed...")

    logging.info("Advanced anomaly detection started...")
    processed_data = anomaly_detection(processed_data)
    logging.info("Advanced anomaly detection completed...")

    logging.info("Data aggregation started...")
    aggregation(processed_data)
    logging.info("Data aggregation completed...")
    logging.info('Data processing pipeline completed and all the results stored to s3...')

if __name__ == "__main__":
    main()