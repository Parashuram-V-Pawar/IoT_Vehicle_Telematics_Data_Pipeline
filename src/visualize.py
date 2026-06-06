import pandas as pd
from src.visualization.timeseries_analysis import *
from src.visualization.rolling_metrics import *
from src.visualization.anomaly_visualization import *
from src.visualization.trip_analysis import *
from src.visualization.relationship_analysis import *
from src.visualization.aggregation_visualizattion import *


def load_data(path):
    """
    Loads data from the specified S3 path into a pandas DataFrame.

        Args:
            path (str): The S3 path to the data.

        Returns:
            pd.DataFrame: The loaded data as a pandas DataFrame.
    """
    logging.info("Reading data from s3...")
    df = pd.read_parquet(f"s3://vehicle-telemetry-project/{path}/")
    logging.info("Reading successful...")
    return df

def plotting():
    """
    Main function to perform all visualizations. It loads the necessary data 
    and calls the respective visualization functions for timeseries analysis, 
    anomaly visualization, trip analysis, relationship analysis, and aggregation visualization.

        Args:
            None
            
        Returns:
            None
    """
    logging.info("Starting visualization process...")
    timeseries = load_data('processed/timeseries')
    time_series_analysis(timeseries)
    rolling_metrics(timeseries)

    # anomaly = load_data('processed/anomaly')
    # anomaly_visualization(anomaly)
    # speed_anomaly(anomaly)

    # trip_agg = load_data('aggregated/trip_level')
    # trip_speed_distribution(trip_agg)
    # trip_duration_comparision(trip_agg)

    # cleaned_df = load_data('processed/cleaned')
    # speed_load_relationship(cleaned_df)
    # temp_load_relationship(cleaned_df)

    # aggregated_df = load_data('aggregated/device_level')
    # device_avg_speed(aggregated_df)

    # hourly_df = load_data('aggregated/avg_speed_aggregation')
    # hourly_trends(hourly_df)

    # processed_df = load_data("processed/cleaned")
    # device_vs_time(processed_df)
    # logging.info("Visualization process completed.")
if __name__=="__main__":
    plotting()