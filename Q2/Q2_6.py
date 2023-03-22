import pandas as pd

# Read the data
df = pd.read_csv('country_vaccination_stats.csv')

# Group the data by country
grouped_data = df.groupby("country")

# Calculate the median daily vaccination for each country
daily_median_vaccinations = grouped_data['daily_vaccinations'].median()

# Get the top-3 countries with highest median daily vaccination
top_3_country = daily_median_vaccinations.sort_values(ascending=False).head(3)

# Print top 3 country
print(top_3_country)