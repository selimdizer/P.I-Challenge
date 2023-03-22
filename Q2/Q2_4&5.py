import pandas as pd

# Read the data
df = pd.read_csv('Q2\country_vaccination_stats.csv')

# Group the data by country
grouped_data = df.groupby("country")

# Replace NaN values with minimum daily vaccination number of relevant countries.
df['daily_vaccinations'] = grouped_data['daily_vaccinations'].transform(lambda x: x.fillna(x.min()))

# Replace NaN values with 0 (zero) where a country does not have any valid vaccination number yet
df['daily_vaccinations'] = df['daily_vaccinations'].transform(lambda x: x.fillna(0))

# Save the output data to a CSV file
df.to_csv("Q2\Q2_1.csv", index=False)
