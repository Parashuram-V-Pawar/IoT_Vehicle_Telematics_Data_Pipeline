import logging
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

font_dict = {
    'family': 'serif',
    'color': 'Black',
    'size': 20
}

def device_avg_speed(df):
    """
    Plots the average speed for each device. The x-axis represents the device IDs, 
    and the y-axis represents the average speed. 
    The plot is saved as "device_avg_speed.png" in the "screenshots" directory.

        :param df:
            The input DataFrame containing the data to be plotted.

        :return:
            None
    """
    df['deviceID'] = df['deviceID'].astype(int)
    df = df.sort_values(by='avg_speed')

    logging.info("Plotting average speed per device...")
    plt.figure(figsize=(8, 8))
    plt.bar(df['deviceID'], df['avg_speed'])
    plt.xlabel('Device')
    plt.ylabel('Average speed')
    plt.title("Average Speed Per Device", fontdict=font_dict)
    plt.xticks(rotation=45)
    plt.savefig("screenshots/device_avg_speed.png")
    logging.info("Average speed per device plot completed...")

def hourly_trends(df):
    """
    This function plots the hourly speed trend. The x-axis represents the hours of the day (0-23),
    and the y-axis represents the average speed for each hour. 
    The plot is saved as "hourly_speed_trend.png" in the "screenshots" directory.

        :param df:
            The input DataFrame containing the data to be plotted.

        :return:
            None
    """
    # Formatting loaded data
    hourly_df = df.groupby('hour')['avg_hourly_speed'].mean().reset_index()
    hourly_df['hour'] = hourly_df['hour'].astype(int)
    hourly_df = hourly_df.sort_values(by='hour')
    hourly_df = hourly_df.reset_index(drop=True)

    # Plotting
    logging.info("Plotting hourlty trends...")
    plt.figure(figsize=(10, 5))
    plt.plot(hourly_df['hour'], hourly_df['avg_hourly_speed'])
    plt.xlabel("Hour")
    plt.ylabel("Average Speed")
    plt.title("Hourly Speed Trend", fontdict=font_dict)
    plt.xticks(range(0, 24))

    plt.tight_layout()
    plt.savefig("screenshots/hourly_speed_trend.png")
    logging.info("Hourly trends plot completed...")

def device_vs_time(df):
    """
    This function plots a heatmap showing the average speed for each device across different hours of the day.
    The x-axis represents the hours of the day (0-23), and the y-axis represents the device IDs.
    The color intensity in the heatmap indicates the average speed, with a color bar to show the scale. 
    The plot is saved as "device_vs_time_heatmap.png" in the "screenshots" directory.
       
        :param df:
            The input DataFrame containing the data to be plotted.

        :return:
            None
    """
    # Formatting loaded data
    heatmap_df = df.groupby(['deviceID', 'hour'])['gps_speed'].mean().reset_index()
    heatmap_df['hour'] = heatmap_df['hour'].astype(int)
    heatmap_df = heatmap_df.sort_values(by='hour')
    pivot = heatmap_df.pivot(index='deviceID', columns='hour', values='gps_speed')

    # Plotting
    logging.info("Plotting device vs time heatmap...")
    plt.figure(figsize=(12, 6))
    plt.imshow(pivot, aspect='auto')
    plt.colorbar(label='Avg Speed')
    plt.xticks(range(len(pivot.columns)), pivot.columns)
    plt.yticks(range(len(pivot.index)), pivot.index)
    plt.xlabel("Hour")
    plt.ylabel("Device ID")
    plt.title("Heatmap: Device vs Hour (Avg Speed)", fontdict=font_dict)

    plt.tight_layout()
    plt.savefig('screenshots/device_vs_time_heatmap.png')
    logging.info("Device vs time heatmap plot completed...")