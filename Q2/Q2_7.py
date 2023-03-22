import pandas as pd

# Read the data
df = pd.read_csv('country_vaccination_stats.csv')

# Group the data by country
grouped_data = df.groupby("date")

# Filtered date 1/6/2021 and calculate the total vaccinations for that date
filtered_date = grouped_data.get_group('1/6/2021').sum()

# Print total vaccinations on 1/6/2021
print(filtered_date['daily_vaccinations'])
