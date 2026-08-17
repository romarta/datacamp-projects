import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Które szkoły w Nowym Jorku mają najlepsze wyniki z matematyki?
schools['wynik_math'] = (schools['average_math']/800)*100
schools['wynik_reading'] = (schools['average_reading']/800)*100
schools['wynik_writiing'] = (schools['average_writing']/800)*100

best_math_schools = schools[schools['wynik_math'] >= 80][['school_name','average_math']].sort_values(['average_math'], ascending=False)
print(best_math_schools.head())

# Jakie są 10 szkół osiągających najlepsze wyniki na podstawie połączonych wyników SAT?
schools['total_SAT'] = schools[['average_math','average_reading','average_writing']].sum(axis=1)
top_10_schools = schools.sort_values(['total_SAT'], ascending=False).head(10)[['school_name','total_SAT']]
print(top_10_schools)

# Which single borough has the largest standard deviation in the combined SAT score?
schools['total_SAT_std'] = schools[['average_math','average_reading','average_writing']].std(axis=1)
pivot = schools.pivot_table(values='total_SAT', index='borough', sort=True, aggfunc=['count','mean', 'std'])
pivot.columns = ['num_schools', 'average_SAT', 'std_SAT']
largest_std_dev = pivot.sort_values(('std_SAT'), ascending=False).head(1).round(2)
print(largest_std_dev)