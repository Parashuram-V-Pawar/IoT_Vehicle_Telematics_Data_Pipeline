import logging
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

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
    logging.info("Starting time series analysis...")

    df = df.sort_values("timeStamp")

    # Selecting only recent records
    df = df.tail(1000)

    fig, axes = plt.subplots(
        nrows=2,
        ncols=1,
        figsize=(14, 10),
        sharex=True
    )

    # ==================================================
    # GPS Speed
    # ==================================================

    logging.info("Plotting GPS speed trend...")

    axes[0].plot(
        df['timeStamp'],
        df['gps_speed'],
        linewidth=1.5,
        label='GPS Speed'
    )

    avg_speed = df['gps_speed'].mean()

    axes[0].axhline(
        avg_speed,
        linestyle='--',
        linewidth=2,
        label=f'Average Speed = {avg_speed:.2f}'
    )

    axes[0].set_title(
        "Vehicle Speed Trend",
        fontsize=14,
        fontweight='bold'
    )

    axes[0].set_ylabel(
        "Speed (km/h)",
        fontsize=12
    )

    axes[0].grid(alpha=0.3)
    axes[0].legend()

    # ==================================================
    # Coolant Temperature
    # ==================================================

    logging.info("Plotting coolant temperature trend...")

    axes[1].plot(
        df['timeStamp'],
        df['cTemp'],
        linewidth=1.5,
        label='Coolant Temperature'
    )

    avg_temp = df['cTemp'].mean()

    axes[1].axhline(
        avg_temp,
        linestyle='--',
        linewidth=2,
        label=f'Average Temp = {avg_temp:.2f}'
    )

    axes[1].set_title(
        "Coolant Temperature Trend",
        fontsize=14,
        fontweight='bold'
    )

    axes[1].set_xlabel(
        "Timestamp",
        fontsize=12
    )

    axes[1].set_ylabel(
        "Temperature (°C)",
        fontsize=12
    )

    axes[1].grid(alpha=0.3)
    axes[1].legend()

    # Rotate timestamp labels
    plt.xticks(rotation=45)

    # Dashboard title
    fig.suptitle(
        "Vehicle Telemetry Time Series Analysis",
        fontsize=20,
        fontweight='bold',
        family='serif'
    )

    plt.tight_layout()

    plt.savefig(
        "screenshots/timeseries_plot.png",
        dpi=300,
        bbox_inches='tight'
    )

    plt.close()

    logging.info("Time series analysis completed...")