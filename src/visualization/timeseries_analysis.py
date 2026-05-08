import logging
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

font_dict = {
    'family': 'serif',
    'color': 'Black',
    'size': 20
}

def time_series_analysis(df):
    """
    Plots the GPS speed and temperature against timestamp.
    The first subplot shows GPS speed vs time, while the second subplot shows temperature vs time.
    The plot is saved as 'timeseries_plot.png' in the 'screenshots' directory.

        :param df:
            A pandas DataFrame containing the data with columns 'timeStamp' for timestamps,
            'gps_speed' for GPS speed, and 'cTemp' for temperature.
            
        :return:
            None
    """
    df = df.sort_values("timeStamp")
    logging.info("Plotting gps_speed vs timestamp...")
    plt.figure(figsize=(8, 12))
    plt.subplot(2, 1, 1)
    plt.plot(df['timeStamp'], df['gps_speed'])
    plt.title("Speed vs Time", fontdict=font_dict)
    plt.xlabel("Timestamp")
    plt.ylabel("GPS Speed")
    plt.xticks(rotation=45)
    plt.grid(linestyle='--')
    logging.info("Plotting completed...")

    logging.info("Plotting cTemp vs timestamp...")
    plt.subplot(2, 1, 2)
    plt.plot(df['timeStamp'], df['cTemp'])
    plt.title("cTemp vs Time", fontdict=font_dict)
    plt.xlabel("Timestamp")
    plt.ylabel("Temperature")
    plt.xticks(rotation=45)
    plt.grid(linestyle='--')
    plt.suptitle('Time series analysis', family='serif', weight='bold', size='30')
    
    plt.tight_layout()
    plt.savefig('screenshots/timeseries_plot.png')
    logging.info("Plotting completed...")