import requests
import pandas as pd 
import sqlite3
from datetime import datetime 
import plotly.express as px
import os

# WeatherStack API setup
api_key = os.getenv("WEATHERSTACK_API_KEY")
if not api_key:
    print("Error: WEATHERSTACK_API_KEY environment variable not set")
    exit()
# use: export WEATHERSTACK_API_KEY="your actual api key" 
# command in bash to set your api key, helping secure this from being leaked if static in code
# you can use command: echo $WEATHERSTACK_API_KEY 
# to verify that the key has been saved


city = "Seattle" # You can modify this location
url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"

# Fetch data
response = requests.get(url)
data = response.json()

# Check if request was successful
if "success" in data and data["success"] == False:
    print("Error fetching data:", data["error"]["info"])
    exit()

# Extract relevant fields for this project
weather_data = {
    "city": data["location"]["name"],
    "temperature": data["current"]["temperature"],
    "humidity": data["current"]["humidity"],
    "wind_speed": data["current"]["wind_speed"],
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# Convert to DataFrame
df = pd.DataFrame([weather_data])

# Print for debugging
print(df)

# Store in SQLite
conn = sqlite3.connect("weather_data.db")
df.to_sql("weather", conn, if_exists="append", index=False)
conn.close()

# Load data from SQLite
df = pd.read_sql("SELECT * FROM weather", sqlite3.connect("weather_data.db"))

# Create a line plot
fig = px.line(df, x="timestamp", y="temperature", title=f"Temperatrue in {city} Over Time")
fig.write_html("weather_dashboard.html")