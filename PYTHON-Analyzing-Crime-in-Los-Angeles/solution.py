import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crimes = pd.read_csv("crimes.csv", dtype={"TIME OCC": str})

# Which hour has the highest frequency of crimes?
# Store as an integer variable called peak_crime_hour.

crimes['TIME OCC 2'] = pd.to_datetime(crimes['TIME OCC'].str[:2] + ":" + crimes['TIME OCC'].str[2:], format='%H:%M')
crimes['HOUR'] = crimes['TIME OCC 2'].dt.hour
peak_crime_hour = crimes['HOUR'].value_counts().idxmax()

# Which area has the largest frequency of night crimes (crimes committed between 10pm and 3:59am)?
# Save as a string variable called peak_night_crime_location.

crimes['TIME GROUP'] = pd.cut(
    crimes['HOUR'],
    bins=[0, 4, 22, 24],
    labels=['night', 'day','night'],
    right=False,
    ordered=False
)
peak_night_crime_location = crimes['AREA NAME'][crimes['TIME GROUP'] == 'night'].value_counts().idxmax()

# Identify the number of crimes committed against victims of different age groups.
# Save as a pandas Series called victim_ages, with age group labels "0-17", "18-25", "26-34", "35-44", "45-54", "55-64", and "65+"
# as the index and the frequency of crimes as the values.

crimes['VICT AGE GROUP'] = pd.cut(
    crimes['Vict Age'],
    bins=[0, 17, 25, 34, 44, 54, 64, 99],
    labels=["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"],
    include_lowest=True,
)
victim_ages = crimes['VICT AGE GROUP'].value_counts().sort_index()
