import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import io
import sys
import os

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
datasort[A].plot.bar(figsize=(30, 5), rot=0, width=0.9)
plt.xticks(rotation=75)
plt.title("Confirmed cases and deaths by regions")
plt.show()
plt.clf()

B = ["People_Tested", "Confirmed"]
datasort[B].plot.bar(figsize=(20, 5), rot=0, width=0.9)
plt.xticks(rotation=75)
plt.title("People tested and confirmed cases by regions")
plt.show()
plt.clf()

C = ["People_Hospitalized", "Recovered"]
datasort[C].plot.bar(figsize=(20, 5), rot=0, width=0.9)
plt.xticks(rotation=75)
plt.title("People hospitalized and recovered cases by regions")
plt.show()
plt.clf()

url_conf = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
url_dths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
url_reco = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"


def update():
    # Initialise the json object
    json_data_final = {}

    # Get content using http request
    try:
        confirmed_ = requests.get(url_conf).content
    except requests.exceptions.RequestException as e:
        print("Fatal error on confirmed cases request")
        raise SystemExit(e)

    try:
        deaths_ = requests.get(url_dths).content
    except requests.exceptions.RequestException as e:
        print("Fatal error on deaths cases request")
        raise SystemExit(e)

    try:
        recovered_ = requests.get(url_reco).content
    except requests.exceptions.RequestException as e:
        print("Fatal error on recovered cases request")
        raise SystemExit(e)
