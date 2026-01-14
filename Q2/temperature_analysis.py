import os
import pandas as pd

FOLDER_PATH = "temperatures"

all_data = []

for file in os.listdir(FOLDER_PATH):
    if file.endswith(".csv"):
        year = file.split("_")[-1].replace(".csv", "")
        file_path = os.path.join(FOLDER_PATH, file)

        df = pd.read_csv(file_path)
        all_data.append(df)
