import logging
from src.load_phase.query_executor import run_query

logging.basicConfig(level=logging.INFO)

def vehicle_metrics():
    """
    This function creates the vehicle_metrics table in Redshift and inserts values from S3.
    
        Args:
            None

        Returns:
            None
    """
    logging.info("Table creation started...")
    try:
        # -------------------------------------------------------------------------
        # Creating and inserting values to vehicle_metrics table
        # -------------------------------------------------------------------------
        logging.info("Creating vehicle_metrics table...")
        vehicle_metrics_table = """
            CREATE TABLE IF NOT EXISTS vehicle_metrics(
                deviceID VARCHAR(255),
                total_records BIGINT,
                avg_speed DOUBLE PRECISION,
                avg_battery DOUBLE PRECISION,
                avg_temp DOUBLE PRECISION,
                anomaly_count BIGINT,
                fault_count BIGINT
            );
        """
        run_query(vehicle_metrics_table)
        logging.info("Created vehicle_metrics table...")

        logging.info("Inserting values to vehicle_metrics table...")
        insert_values_vehicle_metrics = """
            COPY vehicle_metrics
            FROM 's3://vehicle-telemetry-project/aggregated/device_level/'
            IAM_ROLE 'arn:aws:iam::950771917939:role/Redshift-S3-access'
            FORMAT AS PARQUET;
        """
        run_query(insert_values_vehicle_metrics)
        logging.info("Insertion completed...")
    except Exception as e:
        logging.info(f"Error executing query: {e}")

def trip_metrics():
    """
    This function creates the trip_metrics table in Redshift and inserts values from S3.

        Args:
            None

        Returns:
            None
    """
    logging.info("Table creation started...")
    try:
        # -------------------------------------------------------------------------
        # Creating and inserting values to trip_metrics table
        # -------------------------------------------------------------------------
        logging.info("Creating trip_metrics table...")
        trip_metrics_table = """
            CREATE TABLE IF NOT EXISTS trip_metrics(
                tripID VARCHAR(25),
                avg_speed DOUBLE PRECISION,
                max_temp DOUBLE PRECISION,
                trip_duration BIGINT
            );
        """
        run_query(trip_metrics_table)
        logging.info("Created trip_metrics table...")

        logging.info("Inserting values to trip_metrics table...")
        insert_values_trip_metrics = """
            COPY trip_metrics
            FROM 's3://vehicle-telemetry-project/aggregated/trip_level/'
            IAM_ROLE 'arn:aws:iam::950771917939:role/Redshift-S3-access'
            FORMAT AS PARQUET;
        """
        run_query(insert_values_trip_metrics)
        logging.info("Insertion completed...")
    except Exception as e:
        logging.info(f"Error executing query: {e}")


def anomaly_summary():
    """
    This function creates the anomaly_summary table in Redshift and inserts values from S3.

        Args:
            None
            
        Returns:
            None
    """
    logging.info("Table creation started...")
    try:
        # -------------------------------------------------------------------------
        # Creating and inserting values to anomaly_summary table
        # -------------------------------------------------------------------------
        logging.info("Creating anomaly_summary table...")
        anomaly_summary_table = """
            CREATE TABLE IF NOT EXISTS anomaly_summary(
                deviceID VARCHAR(25),
                anomaly_count VARCHAR(100),
                count BIGINT
            );
        """
        run_query(anomaly_summary_table)
        logging.info("Created anomaly_summary table...")

        logging.info("Inserting values to anomaly_summary table...")
        insert_values_anomaly_summary = """
            COPY anomaly_summary
            FROM 's3://vehicle-telemetry-project/aggregated/anomaly_summary/'
            IAM_ROLE 'arn:aws:iam::950771917939:role/Redshift-S3-access'
            FORMAT AS PARQUET;
        """
        run_query(insert_values_anomaly_summary)
        logging.info("Insertion completed...")
    except Exception as e:
        logging.info(f"Error executing query: {e}")