# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 2. Load Dataset
# You can use a CSV or API — here's an example with CSV
df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')

# 3. Basic Data Exploration
print(df.head())
print(df.info())

# 4. Clean Data (drop NaNs, filter dates, etc.)
df = df[df['date'] >= '2020-01-01']  # Filter from Jan 2020 onwards
df = df[['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'continent']]
df = df.dropna(subset=['total_cases', 'location'])

# 5. Global Trend Over Time
global_data = df.groupby('date')[['new_cases', 'new_deaths']].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=global_data, x='date', y='new_cases', label='New Cases')
sns.lineplot(data=global_data, x='date', y='new_deaths', label='New Deaths')
plt.title('Global COVID-19 New Cases and Deaths Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Top 10 Countries by Total Cases (latest date)
latest_date = df['date'].max()
latest_data = df[df['date'] == latest_date]
top10 = latest_data.sort_values('total_cases', ascending=False).head(10)

plt.figure(figsize=(10, 5))
sns.barplot(data=top10, x='total_cases', y='location', palette='Reds_r')
plt.title(f'Top 10 Countries by Total COVID-19 Cases ({latest_date})')
plt.xlabel('Total Cases')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

# 7. Interactive Plotly Chart – Total Cases Over Time by Continent
continent_data = df.dropna(subset=['continent'])
continent_grouped = continent_data.groupby(['continent', 'date'])['total_cases'].sum().reset_index()

fig = px.line(continent_grouped, x='date', y='total_cases', color='continent',
              title='COVID-19 Total Cases Over Time by Continent')
fig.show()
