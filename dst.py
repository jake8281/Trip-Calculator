import pandas as pd
import os


def fetch_distance(start_city, destination_city):
    os.chdir("city_data")
    csv_file = "{}.csv".format(start_city)
    df = pd.read_csv(csv_file)

    x = df.index[df['City'] == "{}".format(destination_city)].to_list()[0]
    return df.iloc[[x]]["Distance"].to_list()[0]

