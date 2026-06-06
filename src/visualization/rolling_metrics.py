import pandas as pd
import logging
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

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
    logging.info("Starting rolling metrics visualization...")

    # Sort by timestamp
    df = df.sort_values("timeStamp")

    # Create figure
    fig, axes = plt.subplots(
        nrows=2,
        ncols=1,
        figsize=(14, 10),
        sharex=True
    )

    # ==================================================
    # Rolling Temperature
    # ==================================================

    logging.info("Plotting rolling temperature trend...")

    axes[0].plot(
        df['timeStamp'],
        df['cTemp'],
        alpha=0.4,
        linewidth=1,
        label='Actual Temperature'
    )

    axes[0].plot(
        df['timeStamp'],
        df['rolling_avg_temp'],
        linewidth=2,
        label='Rolling Avg Temperature'
    )

    avg_temp = df['rolling_avg_temp'].mean()

    axes[0].axhline(
        avg_temp,
        linestyle='--',
        linewidth=2,
        label=f'Avg Temp = {avg_temp:.2f}'
    )

    axes[0].set_title(
        "Temperature Trend Analysis",
        fontsize=14,
        fontweight='bold'
    )

    axes[0].set_ylabel(
        "Temperature (°C)",
        fontsize=12
    )

    axes[0].grid(alpha=0.3)
    axes[0].legend()

    # ==================================================
    # Rolling Speed
    # ==================================================

    logging.info("Plotting rolling speed trend...")

    axes[1].plot(
        df['timeStamp'],
        df['gps_speed'],
        alpha=0.4,
        linewidth=1,
        label='Actual Speed'
    )

    axes[1].plot(
        df['timeStamp'],
        df['rolling_avg_speed'],
        linewidth=2,
        label='Rolling Avg Speed'
    )

    avg_speed = df['rolling_avg_speed'].mean()

    axes[1].axhline(
        avg_speed,
        linestyle='--',
        linewidth=2,
        label=f'Avg Speed = {avg_speed:.2f}'
    )

    axes[1].set_title(
        "Speed Trend Analysis",
        fontsize=14,
        fontweight='bold'
    )

    axes[1].set_xlabel(
        "Timestamp",
        fontsize=12
    )

    axes[1].set_ylabel(
        "Speed (km/h)",
        fontsize=12
    )

    axes[1].grid(alpha=0.3)
    axes[1].legend()

    # Rotate timestamps
    plt.xticks(rotation=45)

    # Main title
    fig.suptitle(
        "Vehicle Telemetry Rolling Metrics Analysis",
        fontsize=20,
        fontweight='bold',
        family='serif'
    )

    # Adjust layout
    plt.tight_layout()

    # Save figure
    plt.savefig(
        "screenshots/rolling_metrics.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    logging.info("Rolling metrics visualization completed...")