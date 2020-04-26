import pandas as pd
import os

directory = r"data"
for filename in os.listdir(directory):
	print(filename)
	df_csv = pd.read_csv("data/" + filename)
	df = df_csv[["tripduration", "starttime", "stoptime", "start station name", "end station name", "end station latitude", "end station longitude", "usertype", "birth year", "gender"]]

	df[["end station latitude"]] = df[["end station latitude"]].round(2)
	df[["end station longitude"]] = df[["end station longitude"]].round(2)

	df.to_csv("data/" + filename[0:6] + "-cbdata.csv", index=False)
