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