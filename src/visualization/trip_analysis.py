import pandas as pd
import logging
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

font_dict = {
    'family': 'serif',
    'color': 'Black',
    'size': 20
}

def trip_speed_distribution(df):
    logging.info("Plotting trip speed distributions...")
    plt.figure(figsize=(8, 8))
    plt.hist(df['avg_speed'], bins='auto')
    plt.xlabel("Average Speed")
    plt.ylabel("Number of Trips")
    plt.title("Distribution of Average Speed per Trip")
    plt.savefig('screenshots/trip_speed_distribution.png')
    logging.info("trip speed distributions plot completed...")

def trip_duration_comparision(df):
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
    