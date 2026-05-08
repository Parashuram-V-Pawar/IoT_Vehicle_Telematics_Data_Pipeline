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
    plt.hist(df['avg_speed'], bins='auto')
    plt.xlabel("Average Speed")
    plt.ylabel("Number of Trips")
    plt.title("Distribution of Average Speed per Trip")
    plt.savefig('screenshots/trip_speed_distribution.png')
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
    logging.info("Plotting trip duration comparision...")
    plt.figure(figsize=(8, 8))
    plt.bar(df['tripID'], df['trip_duration'])
    plt.xlabel("Trip duration")
    plt.ylabel("Trip ID")
    plt.title("Trip Duration Comparision")
    plt.xticks(rotation=90)
    plt.savefig('screenshots/trip_duration_comparision.png')
    logging.info("trip duration comparision plot completed...")
    