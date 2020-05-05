import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import requests
import json

covid_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/05-02-2020.csv"
csv_file = requests.get(covid_url)
open("05-02-2020.csv", "wb").write(csv_file.content)

# Read data from the csv file
csvfname = "05-02-2020.csv"
# With read_csv we control delimiters, rows, column names
col_list = ["Province_State", "Confirmed", "Deaths", "Recovered", "People_Tested", "People_Hospitalized"]
data = pd.read_csv(csvfname, index_col='Province_State', usecols=col_list, header=0, skipinitialspace=True)
datasort = data.sort_values('Deaths', ascending=False)
# Preview all of the loaded data
print(datasort[:50])
datasort = datasort.head(15)


A = ["Confirmed", "Deaths"]
datasort[A].plot.bar(figsize=(30,5), rot=0, width=0.9)
plt.xticks(rotation=90)
plt.show()


