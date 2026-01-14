import os
import pandas as pd

FOLDER_PATH = "temperatures"

all_data = []

for file in os.listdir(FOLDER_PATH):
    if file.endswith(".csv"):
        year = file.split("_")[-1].replace(".csv", "")
        file_path = os.path.join(FOLDER_PATH, file)

        df = pd.read_csv(file_path)

        df_melted = df.melt(
            id_vars=["STATION_NAME"],
            value_vars=[
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ],
            var_name="Month",
            value_name="Temperature"
        )

        df_melted["Year"] = int(year)
        all_data.append(df_melted)


data = pd.concat(all_data, ignore_index=True)
data = data.dropna(subset=["Temperature"])

avg_per_year = data.groupby("Year")["Temperature"].mean()
avg_per_station = data.groupby("STATION_NAME")["Temperature"].mean()

hottest_station = avg_per_station.idxmax()
coldest_station = avg_per_station.idxmin()

