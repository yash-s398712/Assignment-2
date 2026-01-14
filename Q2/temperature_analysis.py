import os
import pandas as pd

FOLDER_PATH = "temperatures"

all_data = []

# Read all CSV files in the temperatures folder
for file in os.listdir(FOLDER_PATH):
    if file.endswith(".csv"):
        year = file.split("_")[-1].replace(".csv", "")
        file_path = os.path.join(FOLDER_PATH, file)

        df = pd.read_csv(file_path)

        # Convert monthly columns to rows
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

# Combine all years
data = pd.concat(all_data, ignore_index=True)

# Ignore missing values
data = data.dropna(subset=["Temperature"])

# Average temperature per year
avg_per_year = data.groupby("Year")["Temperature"].mean()

# Average temperature per station
avg_per_station = data.groupby("STATION_NAME")["Temperature"].mean()

# Hottest and coldest stations
hottest_station = avg_per_station.idxmax()
coldest_station = avg_per_station.idxmin()

print("Average Temperature Per Year:")
print(avg_per_year.round(2))

print("\nHottest Station:")
print(hottest_station, "-", round(avg_per_station[hottest_station], 2), "°C")

print("\nColdest Station:")
print(coldest_station, "-", round(avg_per_station[coldest_station], 2), "°C")
