import pandas as pd
import logging
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

font_dict = {
    'family': 'serif',
    'color': 'Black',
    'size': 20
}

plot_dict = {
    'color': 'red',
    'line': '--'
}

def rolling_metrics(df):
    """
    Plots the average rolling temperature and speed against timestamp.
    The first subplot shows the average rolling temperature vs time, 
    while the second subplot shows the average rolling speed vs time. 
    The plot is saved as 'rolling_metrics.png' in the 'screenshots' directory.

        :param df:
            A pandas DataFrame containing the data.

        :return:
            None
    """
    df = df.sort_values("timeStamp")
    logging.info("Plotting Average rolling temp vs timestamp...")
    plt.figure(figsize=(8, 12))
    plt.subplot(2, 1, 1)
    plt.plot(df['timeStamp'], df['rolling_avg_temp'])
    plt.title("Average rolling temp vs Time", fontdict=font_dict)
    plt.xlabel("Timestamp")
    plt.ylabel("Average Temperature")
    plt.xticks(rotation=45)
    plt.grid(linestyle='--')
    logging.info("Plotting completed...")

    logging.info("Plotting Average rolling speed vs timestamp...")
    plt.subplot(2, 1, 2)
    plt.plot(df['timeStamp'], df['rolling_avg_speed'])
    plt.title("Average rolling speed vs Time", fontdict=font_dict)
    plt.xlabel("Timestamp")
    plt.ylabel("Average Speed")
    plt.xticks(rotation=45)
    plt.grid(linestyle='--')

    plt.suptitle('Rolling Metrics Visualization', family='serif', weight='bold', size='30')
    plt.tight_layout()
    plt.savefig('screenshots/rolling_metrics.png')
    logging.info("Plotting completed...")