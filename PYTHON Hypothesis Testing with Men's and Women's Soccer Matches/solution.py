import pandas as pd
import pingouin as pg
import matplotlib.pyplot as plt
import seaborn as sns

df_men = pd.read_csv('men_results.csv')
df_women = pd.read_csv('women_results.csv')


# you decide to limit the data used in the analysis to only official
# `FIFA World Cup` matches (not including qualifiers) since `2002-01-01`.
# > Are more goals scored in women's international soccer matches than men's?
# You assume a **10% significance level**, and use the following null and alternative hypotheses:
# H_0: The mean number of goals scored in women's international soccer matches is the same as men's.
# H_A: The mean number of goals scored in women's international soccer matches is greater than men's.

# The p-value and the result of the test must be stored in a dictionary called result_dict in the form:
# result_dict = {"p_val": p_val, "result": result}
# where p_val is the p-value and result is either the string "fail to reject" or "reject", depending on the result of the test.

df = pd.concat([
    df_men.assign(gender="men"),
    df_women.assign(gender="women")
], ignore_index=True)

df['total_score'] = df['home_score'] + df['away_score']

df_filtered = df[(df['tournament'] == 'FIFA World Cup') & (df['date'] >= '2002-01-01')]

df_1 = df_filtered[[
     'total_score',
     'gender', ]]

df_2 = df_1.pivot(
    columns='gender',
     values='total_score',
)

sns.displot(
    data=df_1,
    col='gender',
    x='total_score',
    kind='hist',
    bins=20
)
#skewed distribution -> nonparametrics test

result_test = pg.mwu(
    x=df_2['women'],
    y=df_2['men'],
    alternative='greater'
)

p_val = float(result_test['p_val'].iloc[0])

if p_val >= 0.10:
    result = 'fail to reject'
else:
    result = 'reject'

result_dict = {"p_val": p_val, "result": result}
print(result_dict)

