import logging
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

font_dict = {
    'family': 'serif',
    'color': 'Black',
    'size': 20
}

def anomaly_visualization(df):
    """
    This function visualizes temperature anomalies and speed spikes in the given DataFrame. 
    It creates two separate plots: one for temperature anomalies and another for speed spikes. 
    The temperature anomalies are highlighted in red, while the speed spikes are highlighted in blue. 
    Both plots are saved as PNG files in the "screenshots" directory.
        
        :param df:
            A pandas DataFrame containing the data to be visualized. 
        
        :return:
            None
    """
    df = df.sort_values("timeStamp")
    logging.info("Plotting cTemp vs timestamp anomaly...")
    plt.figure(figsize=(8, 8))
    plt.plot(df['timeStamp'], df['cTemp'], label='Temperature', color='blue')
    anomaly_df = df[df['temp_anomaly_flag'] == 1]
    plt.scatter( anomaly_df['timeStamp'], anomaly_df['cTemp'], label="Anomaly", marker='o', color='red')
    plt.title("Temperature Anomaly Detection", fontdict=font_dict)
    plt.xlabel("Timestamp")
    plt.ylabel("Temperature")
    plt.legend()

    plt.xticks(rotation=45)
    plt.savefig("screenshots/temp_anomaly.png")
    logging.info("Temperature anomaly plot completed...")


def speed_anomaly(df):
    """
    This function visualizes speed anomalies in the given DataFrame. 
    It creates a plot of gps_speed vs timestamp, highlighting the speed spikes in blue. 
    The plot is saved as a PNG file in the "screenshots" directory.

        :param df:
            A pandas DataFrame containing the data to be visualized.

        :return:
            None
    """
    df = df.sort_values("timeStamp")
    logging.info("Plotting gps_speed vs timestamp anomaly...")
    plt.figure(figsize=(12, 5))
    plt.plot(df['timeStamp'], df['gps_speed'], label='Speed', color='orange')
    spike = df[df['speed_spike'] == 1]
    plt.scatter(spike['timeStamp'], spike['gps_speed'], label='Speed Spike', marker='o', color='blue')
    plt.xlabel("Time")
    plt.ylabel("Speed")
    plt.title("Speed Spike Detection")
    plt.legend()

    plt.xticks(rotation=45)
    plt.savefig("screenshots/speed_spike.png")
    logging.info("Speed spike plot completed...")
