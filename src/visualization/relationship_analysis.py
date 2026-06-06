import pandas as pd
import logging
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

font_dict = {
    'family': 'serif',
    'color': 'Black',
    'size': 20
}

def speed_load_relationship(df):
    """
    Plots the relationship between GPS speed and engine load. 
    The x-axis represents engine load, while the y-axis represents GPS speed. 
    The plot is saved as 'speed_vs_eload.png' in the 'screenshots' directory.

        :param df: 
            A pandas DataFrame containing the data with columns 'eLoad' 
            for engine load and 'gps_speed' for GPS speed.

        :return: 
            None
    """
    df = df.sample(
        min(5000, len(df)),
        random_state=42
    )

    plt.figure(figsize=(8, 8))

    plt.scatter(df['eLoad'], df['gps_speed'], color='green', alpha=0.5)

    plt.ylabel("GPS Speed")
    plt.xlabel("Engine Load")
    plt.title("Speed vs Engine Load", fontdict=font_dict)

    plt.tight_layout()
    plt.savefig('screenshots/speed_vs_eload.png',
                bbox_inches='tight'
                )

def temp_load_relationship(df):
    """
    Plots the relationship between temperature and engine load.
    The x-axis represents temperature, while the y-axis represents engine load.
    The plot is saved as 'temp_vs_eload.png' in the 'screenshots' directory.

        :param df:
            A pandas DataFrame containing the data with columns 'cTemp'
            for temperature and 'eLoad' for engine load.
            
        :return:
            None
    """
    df = df.sample(
        min(5000, len(df)),
        random_state=42
    )

    plt.figure(figsize=(8, 8))

    plt.scatter(df['cTemp'], df['eLoad'], color='red', alpha=0.5)

    plt.xlabel("Temperature")
    plt.ylabel("Engine Load")
    plt.title("Temp vs Engine Load", fontdict=font_dict)

    plt.tight_layout()
    plt.savefig('screenshots/temp_vs_eload.png',
                bbox_inches='tight'
                )