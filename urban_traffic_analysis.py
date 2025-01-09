import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from jinja2 import Template

# Load the dataset
df = pd.read_csv('traffic-volume-counts-2012-2013.csv')

# Define mapping of roadways to regions
roadway_to_region = {
    'HUGUENOT AVE': 'Staten Island',
    'RICHMOND HILL ROAD': 'Staten Island',
    'OCEAN TERRACE': 'Staten Island',
    'LITTLE CLOVE RD': 'Staten Island',
    'HYLAN BOULEVARD': 'Staten Island',
    '4 AVENUE': 'Brooklyn',
    'CROPSEY AVE': 'Brooklyn',
    'BATH AVE': 'Brooklyn',
    'BENSON AVE': 'Brooklyn',
    'SHORE PKWY': 'Brooklyn',
    '86th ST': 'Brooklyn',
    'KINGS HWY': 'Brooklyn',
    'AVE U': 'Brooklyn',
    'BAY RIDGE PKWY': 'Brooklyn',
    '8 AVENUE': 'Brooklyn',
    '13 AVENUE': 'Brooklyn',
    '14 AVENUE': 'Brooklyn',
    '60 STREET': 'Brooklyn',
    '18 AVENUE': 'Brooklyn',
    'AVE P': 'Brooklyn',
    'BAY PKWY': 'Brooklyn',
    '7 AVENUE': 'Brooklyn',
    '3 AVENUE': 'Brooklyn',
    '5 AVENUE': 'Brooklyn',
    '51 STREET': 'Brooklyn',
    '50 STREET': 'Brooklyn',
    '39 STREET': 'Brooklyn',
    '37 STREET': 'Brooklyn',
    'COLUMBIA STREET': 'Brooklyn',
    'CLINTON STREET': 'Brooklyn',
    'HICKS STREET': 'Brooklyn',
    '3 STREET': 'Brooklyn',
    'COURT STREET': 'Brooklyn',
    'TRINITY PL': 'Manhattan',
    'LIBERTY STREET': 'Manhattan',
    'FULTON STREET': 'Manhattan',
    'CHAMBERS STREET': 'Manhattan',
    'MADISON STREET': 'Manhattan',
    'CATHERINE STREET': 'Manhattan',
    'MARKET STREET': 'Manhattan',
    'SURF AVE': 'Brooklyn',
    'NEPTUNE AVE': 'Brooklyn',
    'AVE Z': 'Brooklyn',
    'CONEY ISLAND AVENUE': 'Brooklyn',
    'AVENUE J': 'Brooklyn',
    'AVE M': 'Brooklyn',
    'OCEAN AVE': 'Brooklyn',
    'BEDFORD AVE': 'Brooklyn',
    'NOSTRAND AVE': 'Brooklyn',
    'JAMAICA AVENUE': 'Queens',
    'CONEY ISLAND AVE': 'Brooklyn',
    'CATON AVE': 'Brooklyn',
    'DITMAS AVENUE': 'Brooklyn',
    'CORTELYOU ROAD': 'Brooklyn',
    'CHURCH AVE': 'Brooklyn',
    'OCEAN AVENUE': 'Brooklyn',
    'FARRAGUT ROAD': 'Brooklyn',
    '56th RD': 'Queens',
    'LINDEN BLVD': 'Brooklyn',
    '6 AVENUE': 'Manhattan',
    'ASHLAND PLACE': 'Brooklyn',
    'PROSPECT PARK WEST': 'Brooklyn',
    'CLASSON AVE': 'Brooklyn',
    'BROOKLYN AVE': 'Brooklyn',
    'LAFAYETTE AVE': 'Brooklyn',
    'MYRTLE AVE': 'Brooklyn',
    'MONTROSE AVE': 'Brooklyn',
    'METROPOLITAN AVE': 'Brooklyn',
    'MESEROLE STREET': 'Brooklyn',
    'CORTLANDT ALLEY': 'Manhattan',
    'WEST BROADWAY': 'Manhattan',
    'GRAND STREET': 'Brooklyn',
    'E 4TH ST': 'Manhattan',
    'PITT STREET': 'Manhattan',
    'AVENUE B': 'Manhattan',
    'BROADWAY': 'Manhattan',
    'WEST 30 STREET': 'Manhattan',
    'AVENUE C': 'Manhattan',
    'COMMERCIAL ST': 'Brooklyn',
    'ASH ST': 'Brooklyn',
    'DRIGGS AVE': 'Brooklyn',
    'GREENPOINT AVE': 'Brooklyn',
    'YORK AVENUE': 'Manhattan',
    'CENTRAL PARK WEST': 'Manhattan',
    'WEST END AVENUE': 'Manhattan',
    'AMSTERDAM AVE': 'Manhattan',
    'MANHATTAN AVENUE': 'Manhattan',
    'WEST 135 STREET': 'Manhattan',
    'AVENUE N': 'Brooklyn',
    'AVENUE M': 'Brooklyn',
    'AVENUE U': 'Brooklyn',
    'AVENUE D': 'Brooklyn',
    'CLARENDON ROAD': 'Brooklyn',
    'ALBANY AVENUE': 'Brooklyn',
    'GLENWOOD ROAD': 'Brooklyn',
    'MAC DOUGAL STREET': 'Manhattan',
    'HOWARD AVENUE': 'Brooklyn',
    'HEGEMAN AVENUE': 'Brooklyn',
    'VERMONT PLACE': 'Brooklyn',
    '73 PLACE': 'Queens',
    'PITKIN AVE': 'Brooklyn',
    'LIBERTY AVE': 'Queens',
    '111 AVE': 'Queens',
    'BRINKERHOFF AVE': 'Queens',
    'KEW GARDENS ROAD': 'Queens',
    'VAN WYCK EXPRESSWAY': 'Queens',
    'ARCHER AVE': 'Queens',
    'LAKEWOOD AVE': 'Queens',
    '101 AVE': 'Queens',
    '150th ST': 'Queens',
    'CENTRAL AVE': 'Queens',
    'CROSS ISLAND PKWY SR': 'Queens',
    'HUNGRY HARBOR RD': 'Queens',
    'MAURICE AVE': 'Queens',
    '39th ST': 'Brooklyn',
    '48th ST': 'Queens',
    'EAST 135 STREET': 'Manhattan',
    'MORRIS AVENUE': 'Bronx',
    'AUDUBON AVE': 'Manhattan',
    'UNDERCLIFF AVENUE': 'Bronx',
    'SHERIDAN AVENUE': 'Bronx',
    'JEROME AVENUE': 'Bronx',
    'WADSWORTH AVENUE': 'Manhattan',
    'DYCKMAN STREET': 'Manhattan',
    'CEDAR AVENUE': 'Bronx',
    'HENRY HUDSON PKWY': 'Bronx',
    '32nd AVE': 'Queens',
    'LONGWOOD AVENUE': 'Bronx',
    'EAST 163 STREET': 'Bronx',
    'EAST TREMONT AVENUE': 'Bronx',
    'CROTONA AVENUE': 'Bronx',
    'WEBSTER AVENUE': 'Bronx',
    'PAULDING AVENUE': 'Bronx',
    'HUTCHINSON RIVER PKWY': 'Bronx',
    'BOSTON ROAD': 'Bronx',
    'EAST 241 STREET': 'Bronx',
    'JEWEL AVE': 'Queens',
    'UNION STREET': 'Queens',
    'SANFORD AVE': 'Queens',
    'ROOSEVELT AVE': 'Queens',
    'EAST 177 STREET': 'Bronx',
    'LAFAYETTE AVENUE': 'Bronx',
    'UNDERHILL AVE': 'Bronx',
    'LEXINGTON AVENUE': 'Manhattan',
    'HOMELAWN STREET': 'Queens',
    'HOLLIS COURT BLVD': 'Queens',
    '35 AVE': 'Queens',
    '56 AVE': 'Queens',
    '26 AVE': 'Queens',
    'MARYLAND RD': 'Queens',
    'MARATHON PKWY': 'Queens',
    'FINGERBOARD ROAD': 'Staten Island',
    'WEST 155 ST': 'Manhattan',
    'SOUTHERN BOULEVARD': 'Bronx',
    'ARTHUR KILL ROAD': 'Staten Island',
    'FLUSHING AVE': 'Brooklyn',
    '10 AVENUE': 'Manhattan',
    'GLEN STREET': 'Queens',
    'GRAND AVE': 'Queens',
    'WEST GUN HILL ROAD': 'Bronx',
    'DRUMGOOLE ROAD WEST': 'Staten Island',
    'COLONIAL ROAD': 'Brooklyn',
    '115 ROAD': 'Queens',
    'VERNON BLVD': 'Queens',
    'WHITE PLAINS ROAD': 'Bronx',
    '7 AVE': 'Brooklyn',
    '164 STREET': 'Queens',
    'SPRINGFIELD BLVD': 'Queens',
    'FRANCIS LEWIS BLVD': 'Queens',
    'ATLANTIC AVE': 'Brooklyn',
    'WOODHAVEN BLVD': 'Queens',
    '34th AVE': 'Queens',
    'ESPLANADE': 'Bronx',
    'SEAGRIT BLVD': 'Queens',
    'ROCKAWAY BLVD': 'Queens',
    'MERRICK BLVD': 'Queens',
    'ORIENTAL BLVD': 'Brooklyn',
    'FLATLANDS AVE': 'Brooklyn',
    'LENOX AVE': 'Manhattan',
    'ALLEN STREET': 'Manhattan',
    'EAST 18 STREET': 'Manhattan',
    'NORFOLK STREET': 'Manhattan',
    'MEEKER AVE': 'Brooklyn',
    'KINGS HIGHWAY': 'Brooklyn',
    'ROCKAWAY AVENUE': 'Brooklyn',
    '130 PL': 'Queens',
    'EAST 161 STREET': 'Bronx',
    'EAST 165 STREET': 'Bronx',
    'EAST 204 STREET': 'Bronx',
    'ZEREGA AVENUE': 'Bronx',
    'GRAND CONCOURSE_SERV': 'Bronx',
    'E 174 ST': 'Bronx',
    'CROSS BX EXPWY SER RD': 'Bronx',
    'E 176 ST': 'Bronx',
    'FAIRMONT PL': 'Bronx',
    'THROGS NECK EXPWY SER RD': 'Bronx',
    'E 177 ST': 'Bronx',
    '8 AVE': 'Brooklyn',
    'ALBANY AVE': 'Brooklyn',
    'JAMAICA AVE': 'Queens',
    'WALTHAM STREET': 'Queens',
    'SHERIDANA AVENUE': 'Bronx',
    'Manhattan WEST 155 ST': 'Manhattan',
    'NOSTRAND AVENUE': 'Brooklyn',
    'LITTLE CLOVE ROAD': 'Staten Island',
    'LOUIS NINE BOULEVARD': 'Bronx',
    'BLOOMINGDALE ROAD': 'Staten Island',
    'ATLANTIC AVENUE': 'Brooklyn',
    'BRADDOCK AVE': 'Queens',
    '11th ST': 'Queens',
    'LINDEN BOULEVARD': 'Brooklyn',
    'KINGS HIGHWAY SERVICE': 'Brooklyn',
}

# Remove leading and trailing spaces from road names
df['Roadway Name'] = df['Roadway Name'].str.strip()

# Add 'Region' column based on 'Roadway Name' mapping
df['Region'] = df['Roadway Name'].map(roadway_to_region)

# creat hourly columns
hourly_columns = [col for col in df.columns if '-' in col]

# Extract time features
df['Date'] = pd.to_datetime(df['Date'])
df['Hour'] = df['Date'].dt.hour
df['DayOfWeek'] = df['Date'].dt.dayofweek
df['Month'] = df['Date'].dt.month

def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Fall'

df['Season'] = df['Month'].apply(get_season)


# Find peak time (hour) for traffic
hourly_avg = df[hourly_columns].mean().reset_index()
hourly_avg.columns = ['Time', 'AverageTrafficVolume']
peak_hour = hourly_avg.loc[hourly_avg['AverageTrafficVolume'].idxmax(), 'Time']
print(f"Peak Traffic Hour: {peak_hour}")

plt.figure(figsize=(12, 6))
sns.lineplot(data=hourly_avg, x='Time', y='AverageTrafficVolume')
plt.title('Average Traffic Volume by Hour')
plt.xticks(rotation=90)
plt.savefig('average_traffic_by_hour.png')
plt.close()

# Find peak day of the week for traffic
daily_traffic = df.groupby('DayOfWeek')[hourly_columns].mean().mean(axis=1)
peak_day = daily_traffic.idxmax()
day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(f"Peak Traffic Day: {day_names[peak_day]}")

daily_traffic_df = daily_traffic.reset_index()
daily_traffic_df.columns = ['DayOfWeek', 'AverageTrafficVolume']

plt.figure(figsize=(12, 6))
sns.lineplot(data=daily_traffic_df, x='DayOfWeek', y='AverageTrafficVolume')
plt.title('Patterns by Day of the Week')
plt.xticks(ticks=range(7), labels=day_names)
plt.savefig('patterns_by_day.png')
plt.close()

# Find peak location (roadway) for traffic
roadway_traffic = df.groupby('Roadway Name')[hourly_columns].sum().sum(axis=1)
peak_roadway = roadway_traffic.idxmax()
print(f"Peak Traffic Location: {peak_roadway}")

roadway_traffic_df = roadway_traffic.reset_index()
roadway_traffic_df.columns = ['Roadway Name', 'TotalTrafficVolume']

plt.figure(figsize=(12, 6))
sns.barplot(data=roadway_traffic_df, x='Roadway Name', y='TotalTrafficVolume')
plt.title('Total Traffic Volume by Roadway')
plt.xticks(rotation=90)
plt.savefig('total_traffic_by_roadway.png')
plt.close()

# Visualization: Traffic Volume by Hour
plt.figure(figsize=(12, 6))
sns.lineplot(data=hourly_avg, x='Time', y='AverageTrafficVolume')
plt.title('Traffic Volume by Hour')
plt.xticks(rotation=90)
plt.savefig('traffic_by_hour.png')
plt.close()

# Region-specific traffic analysis
region_daily_avg = df.groupby(['Region', 'DayOfWeek'])[hourly_columns].mean().mean(axis=1).reset_index()

# Visualizations: Average Traffic Volume by Region and Day of the Week
plt.figure(figsize=(12, 6))
sns.lineplot(data=region_daily_avg, x='DayOfWeek', y=0, hue='Region')
plt.title('Average Traffic Volume by Region and Day of the Week')
plt.xticks(ticks=range(7), labels=day_names)
plt.savefig('average_traffic_by_region_and_day.png')
plt.close()

# General region traffic analysis
overall_region_traffic = df.groupby('Region')[hourly_columns].mean().mean(axis=1).reset_index()
overall_region_traffic.columns = ['Region', 'AverageTrafficVolume']
busiest_region = overall_region_traffic.loc[overall_region_traffic['AverageTrafficVolume'].idxmax(), 'Region']
least_busy_region = overall_region_traffic.loc[overall_region_traffic['AverageTrafficVolume'].idxmin(), 'Region']

# Count number of streets in each region
streets_per_region = df['Roadway Name'].groupby(df['Region']).nunique().reset_index()
streets_per_region.columns = ['Region', 'NumberOfStreets']

# Find regions with fewer streets but high traffic
high_traffic_fewer_streets = overall_region_traffic.merge(streets_per_region, on='Region')
high_traffic_fewer_streets = high_traffic_fewer_streets.sort_values(by=['AverageTrafficVolume', 'NumberOfStreets'], ascending=[False, True])

# Visualizations: Average Traffic Volume by Region
plt.figure(figsize=(12, 6))
sns.barplot(data=overall_region_traffic, x='Region', y='AverageTrafficVolume')
plt.title('Average Traffic Volume by Region')
plt.xticks(rotation=90)
plt.savefig('average_traffic_by_region.png')
plt.close()

# Visualizations: Number of Streets by Region
plt.figure(figsize=(12, 6))
sns.barplot(data=streets_per_region, x='Region', y='NumberOfStreets')
plt.title('Number of Streets by Region')
plt.xticks(rotation=90)
plt.savefig('number_of_streets_by_region.png')
plt.close()

# Calculate the total traffic volume for each Season
seasonal_traffic = df.groupby('Season')[hourly_columns].sum().sum(axis=1).reset_index()
seasonal_traffic.columns = ['Season', 'TotalTrafficVolume']

# Visualizations: Season traffic patterns
plt.figure(figsize=(12, 6))
sns.lineplot(data=seasonal_traffic, x='Season', y='TotalTrafficVolume', sort=False)
plt.title('Total Traffic Volume Trend Over Seasons')
plt.savefig('traffic_volume_trend_over_seasons.png')
plt.close()

# Generate HTML report
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Traffic Analysis Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1, h2, h3 { color: #2c3e50; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
        th, td { border: 1px solid #dddddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        img { max-width: 100%; height: auto; }
    </style>
</head>
<body>
    <h1>Traffic Analysis Report</h1>
    <h2>1. Peak Traffic Hour</h2>
    <p>The hour with the highest average traffic volume is {{ peak_hour }}.</p>
    <h2>2. Peak Traffic Day</h2>
    <p>The day of the week with the highest average traffic volume is {{ peak_day_name }}.</p>
    <h2>3. Peak Traffic Location</h2>
    <p>The roadway with the highest total traffic volume is {{ peak_roadway }}.</p>
    <h2>Patterns by Day of the Week</h2>
    <img src="patterns_by_day.png" alt="Patterns by Day of the Week">
    <pre>{{ daily_traffic_df.to_string(index=False) }}</pre>
    <h2>Traffic Volume by Hour</h2>
    <img src="traffic_by_hour.png" alt="Traffic Volume by Hour">
    <pre>{{ hourly_avg.to_string(index=False) }}</pre>
    <h2>Total Traffic Volume by Roadway</h2>
    <img src="total_traffic_by_roadway.png" alt="Total Traffic by Roadway">
    <pre>{{ roadway_traffic_df.to_string(index=False) }}</pre>
    <h2>Average Traffic Volume by Region</h2>
    <img src="average_traffic_by_region.png" alt="Average Traffic by Region">
    <pre>{{ overall_region_traffic.to_string(index=False) }}</pre>
    <h2>Number of Streets by Region</h2>
    <img src="number_of_streets_by_region.png" alt="Number of Streets by Region">
    <pre>{{ streets_per_region.to_string(index=False) }}</pre>
    <h2>Average Traffic Volume by Region and Day of the Week</h2>
    <img src="average_traffic_by_region_and_day.png" alt="Average Traffic Volume by Region and Day of the Week">
    <pre>{{ region_daily_avg.to_string(index=False) }}</pre>
    <h2>Total Traffic Volume Trend Over Seasons</h2>
    <img src="traffic_volume_trend_over_seasons.png" alt="Total Traffic Volume Trend Over Seasons">
    <pre>{{ seasonal_traffic.to_string(index=False) }}</pre>
</body>
</html>
"""

template = Template(html_template)
html_content = template.render(
    peak_hour=peak_hour,
    peak_day_name=day_names[peak_day],
    peak_roadway=peak_roadway,
    daily_traffic_df=daily_traffic_df,
    overall_region_traffic=overall_region_traffic,
    roadway_traffic_df=roadway_traffic_df,
    streets_per_region=streets_per_region,
    high_traffic_fewer_streets=high_traffic_fewer_streets,
    region_daily_avg=region_daily_avg,
    hourly_avg=hourly_avg,
    seasonal_traffic=seasonal_traffic,
)

with open('traffic_analysis_report.html', 'w') as file:
    file.write(html_content)

print("Detailed traffic analysis report generated and saved as 'traffic_analysis_report.html'.")
