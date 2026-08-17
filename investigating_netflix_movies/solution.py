# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# most frequent movie duration in the 1990s
dur = netflix_df.loc[
    (netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] < 2000),
    ['release_year', 'duration', 'genre']]

duration = dur['duration'].mode()[0]
print(duration)

# number of short action movies released in the 1990s
short_action = dur.loc[
    (dur['duration'] < 90) & (dur['genre'] == 'Action'),
    ['duration', 'genre']]

short_movie_count = short_action['genre'].count()
print(short_movie_count)
