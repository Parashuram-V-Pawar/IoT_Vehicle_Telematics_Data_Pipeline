import logging
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

font_dict = {
    'family': 'serif',
    'color': 'Black',
    'size': 20
}

def trip_speed_distribution(df):
    """
    Plots the distribution of average speed per trip. 
    The x-axis represents the average speed, while the y-axis represents the number of trips. 
    The plot is saved as 'trip_speed_distribution.png' in the 'screenshots' directory.
    
        :param df:
            A pandas DataFrame containing the data with a column 'avg_speed' for average speed per trip.

        :return:
            None
    """
    logging.info("Plotting trip speed distributions...")
    plt.figure(figsize=(8, 8))

    plt.hist(df['avg_speed'], 
             bins=20, 
             alpha=0.8,
             edgecolor='black'
            )
    
    plt.xlabel("Average Speed (km/h)")
    plt.ylabel("Number of Trips")
    plt.title("Distribution of Average Speed per Trip",
              fontdict=font_dict
              )

    plt.savefig('screenshots/trip_speed_distribution.png',
                bbox_inches='tight'
                )
    plt.close()
    logging.info("trip speed distributions plot completed...")

def trip_duration_comparision(df):
    """
    Plots the comparison of trip durations.
    The x-axis represents the trip ID, while the y-axis represents the trip duration.
    The plot is saved as 'trip_duration_comparision.png' in the 'screenshots' directory.
    
        :param df:
            A pandas DataFrame containing the data with columns 'tripID' for trip ID 
            and 'trip_duration' for trip duration.
            
        :return:
            None
    """
    df['tripID'] = df['tripID'].astype(int)

    df = (
        df.sort_values(
            by='trip_duration',
            ascending=False
        )
        .head(20)
        .sort_values(by='trip_duration')
    )

    logging.info("Plotting trip duration comparision...")
    plt.figure(figsize=(12,6))

    plt.barh(
        df['tripID'].astype(str),
        df['trip_duration']
    )

    plt.xlabel("Trip Duration (minutes)")
    plt.ylabel("Trip ID")

    plt.title(
        "Top 20 Longest Trips",
        fontdict=font_dict
    )

    plt.tight_layout()

    plt.savefig('screenshots/trip_duration_comparision.png',
                bbox_inches='tight'
                )
    logging.info("trip duration comparision plot completed...")
    