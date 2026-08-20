import pandas as pd


# What is the most commonly awarded gender and birth country?
# Store your answers as string variables top_gender and top_country.

df = pd.read_csv('data/nobel.csv')
top_gender = df.groupby('sex')['sex'].count().idxmax()
top_country = df.groupby('birth_country')['birth_country'].count().idxmax()

print(top_gender)
print(top_country)


# Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?
# Store this as an integer called max_decade_usa.

df['decade'] = (df['year'] // 10) * 10

awarded_decade = (
    df.groupby('decade')
    .size()
    .rename('all')
    .to_frame()
)

awarded_usa_and_decade = (
    df[df['birth_country'].isin(['USA', 'United States of America'])]
    .groupby('decade')
    .size()
    .rename('usa')
    .to_frame()
)

new_table = awarded_decade.merge(awarded_usa_and_decade, on='decade', how='inner')
new_table['procent'] = new_table['usa'] / new_table['all'] * 100

max_decade_usa = int(new_table['procent'].idxmax())
print(max_decade_usa)


# Which decade and Nobel Prize category combination had the highest proportion of female laureates?
# Store this as a dictionary called max_female_dict where the decade is the key and the category is the value. There should only be one key:value pair.

female_proportion = (
    df.groupby(['decade', 'category'])['sex']
    .apply(lambda x: (x == 'Female').mean())
)

max_combination = female_proportion.idxmax()

max_female_dict = {
    max_combination[0]: max_combination[1]
}

print(max_female_dict)

# Who was the first woman to receive a Nobel Prize, and in what category?
# Save your string answers as first_woman_name and first_woman_category.

df_2 = df[df['sex'].isin(['Female'])][['category','full_name','year']].sort_values('year').head(1)
first_woman_name = df_2['full_name'].iloc[0]
first_woman_category = df_2['category'].iloc[0]

print(first_woman_name)
print(first_woman_category)


# Which individuals or organizations have won more than one Nobel Prize throughout the years?
# Store the full names in a list named repeat_list.

more_than_one = (
    df['full_name'].value_counts()
)

repeat_list = more_than_one[more_than_one>= 2].index.to_list()
print(repeat_list)