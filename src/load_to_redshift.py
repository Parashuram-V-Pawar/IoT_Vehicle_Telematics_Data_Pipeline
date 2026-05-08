import logging
from src.load_phase.create_tables import vehicle_metrics, anomaly_summary, trip_metrics

logging.basicConfig(level=logging.INFO)

def load_to_redshift():
    """
    Load the processed data into Redshift by executing SQL scripts to create tables and insert data.
    
        Args:
            None

        Returns:
            None
    """
    logging.info("Redshift scripts execution started...")
    vehicle_metrics()
    anomaly_summary()
    trip_metrics()
    logging.info("Redshift execution completed...")

if __name__=="__main__":
    load_to_redshift()