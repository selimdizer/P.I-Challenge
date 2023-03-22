import plotly.express as px
import pandas as pd
# Define the data

df = pd.read_csv('Q1\DailyActivities.csv')

fig = px.bar(df, x="Name", y="Time Spent", color="Area of Interest", title="Daily Activities")
fig.write_image("Q1/Q1.png")
print(df)