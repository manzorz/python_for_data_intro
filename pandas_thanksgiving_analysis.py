import csv
import datetime

f = open('guns.csv')
data = list(csv.reader(f))

data[0:5]

headers = data[0]
data = data[1:]

years = [row[1] for row in data]

year_counts = {}

for year in years:
    if year not in year_counts:
        year_counts[year] = 1
    else:
        year_counts[year] += 1

year_counts

dates = [datetime.datetime(
            year=int(row[1]),
            month=int(row[2]),
            day=1) for row in data]

date_counts = {}

for date in dates:
    if date not in date_counts:
        date_counts[date] = 1
    else:
        date_counts[date] += 1

sex_counts = {}
race_counts = {}

for row in data:
    sex = row[5]
    race = row[7]
    if sex in sex_counts:
        sex_counts[sex] += 1
    else:
        sex_counts[sex] = 1
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

f = open('census.csv')
census = list(csv.reader(f))

mapping = {}

mapping['White'] = int(census[1][10])
mapping['Hispanic'] = int(census[1][11])
mapping['Black'] = int(census[1][12])
mapping['Native American/Native Alaskan'] = int(census[1][13])
mapping['Asian/Pacific Islander'] = int(census[1][14] + census[1][15])

race_per_hundredk = {}
for key, value in race_counts.items():
    race_counts_value = value
    mapping_value = mapping[key]
    race_per_hundredk[key] = race_counts_value / mapping_value * 100000

intents = [row[3] for row in data]
races = [row[7] for row in data]

homicide_race_counts = {}

for i, race in enumerate(races):
    if intents[i] == 'Homicide':
        if race in homicide_race_counts:
            homicide_race_counts[race] += 1
        else:
            homicide_race_counts[race] = 1

homicide_race_ratek = {}

for key, value in homicide_race_counts.items():
    race_counts_value = value
    mapping_value = mapping[key]
    homicide_race_ratek[key] = race_counts_value / mapping_value * 100000

homicide_race_ratek
