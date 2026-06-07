# import pandas as pd
# import matplotlib.pyplot as plt
# import os

# # Load dataset
# df = pd.read_csv('data/Steel_industry_data.csv')

# # Basic exploration
# print("Shape:", df.shape)
# print("\nColumns:", df.columns.tolist())
# print("\nFirst 5 rows:")
# print(df.head())
# print("\nBasic Stats:")
# print(df.describe())
# print("\nMissing Values:")
# print(df.isnull().sum())

import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv('data/Steel_industry_data.csv')

# Create charts folder if not exists
os.makedirs('charts', exist_ok=True)

# ---- CHART 1: Average Energy Usage by Day of Week ----
day_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
day_avg = df.groupby('Day_of_week')['Usage_kWh'].mean().reindex(day_order)

plt.figure(figsize=(10,5))
plt.bar(day_avg.index, day_avg.values, color='steelblue')
plt.title('Average Energy Usage by Day of Week')
plt.xlabel('Day')
plt.ylabel('Average Usage (kWh)')
plt.tight_layout()
plt.savefig('charts/chart1_day_of_week.png')
plt.close()
print("Chart 1 done")

# ---- CHART 2: Energy Usage by Load Type ----
load_avg = df.groupby('Load_Type')['Usage_kWh'].mean()

plt.figure(figsize=(8,5))
plt.bar(load_avg.index, load_avg.values, color=['green','orange','red'])
plt.title('Average Energy Usage by Load Type')
plt.xlabel('Load Type')
plt.ylabel('Average Usage (kWh)')
plt.tight_layout()
plt.savefig('charts/chart2_load_type.png')
plt.close()
print("Chart 2 done")

# ---- CHART 3: Weekday vs Weekend Energy Usage ----
week_avg = df.groupby('WeekStatus')['Usage_kWh'].mean()

plt.figure(figsize=(6,5))
plt.bar(week_avg.index, week_avg.values, color=['steelblue','coral'])
plt.title('Weekday vs Weekend Energy Usage')
plt.xlabel('Week Status')
plt.ylabel('Average Usage (kWh)')
plt.tight_layout()
plt.savefig('charts/chart3_weekday_vs_weekend.png')
plt.close()
print("Chart 3 done")

# ---- CHART 4: CO2 vs Energy Usage Scatter ----
plt.figure(figsize=(8,5))
plt.scatter(df['Usage_kWh'], df['CO2(tCO2)'], alpha=0.3, color='tomato', s=5)
plt.title('CO2 Emissions vs Energy Usage')
plt.xlabel('Energy Usage (kWh)')
plt.ylabel('CO2 (tCO2)')
plt.tight_layout()
plt.savefig('charts/chart4_co2_vs_usage.png')
plt.close()
print("Chart 4 done")

# ---- CHART 5: Average Energy by Load Type and WeekStatus ----
pivot = df.groupby(['Load_Type','WeekStatus'])['Usage_kWh'].mean().unstack()

pivot.plot(kind='bar', figsize=(10,5), color=['steelblue','coral'])
plt.title('Energy Usage by Load Type and Week Status')
plt.xlabel('Load Type')
plt.ylabel('Average Usage (kWh)')
plt.tight_layout()
plt.savefig('charts/chart5_load_weekstatus.png')
plt.close()
print("Chart 5 done")

print("\nAll charts saved in charts/ folder!")

# ---- KEY INSIGHTS ----
print("\n===== KEY INSIGHTS =====")
print(f"Total records: {len(df)}")
print(f"Avg energy usage: {df['Usage_kWh'].mean():.2f} kWh")
print(f"Max energy usage: {df['Usage_kWh'].max():.2f} kWh")
print(f"Avg CO2 emission: {df['CO2(tCO2)'].mean():.4f} tco2")
print(f"Highest usage day: {day_avg.idxmax()}")
print(f"Lowest usage day: {day_avg.idxmin()}")
print(f"Highest load type: {load_avg.idxmax()}")