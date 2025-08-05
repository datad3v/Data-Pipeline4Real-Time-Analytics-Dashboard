Data-Pipeline4Real-Time-Analytics-Dashboard

A Python-based ETL pipeline that fetches weather data from the WeatherStack API, stores it in SQLite, and visualizes temperature trends with Plotly. Built to demonstrate data management and system integration skills.

Architecture:

mermaid
graph TD
    A[WeatherStack API] --> B[Python Script]
    B --> C[SQLite Database]
    C --> D[Plotly Dashboard]

Setup:
-Install dependencies: pip3 install -r requirements.txt
-Get a free WeatherStack API key from https://weatherstack.com
-Update api_key in weather_pipeline.py
-Run: python3 weather_pipeline.py

Files:
-weather_pipeline.py: Main ETL and visualization script
-weather_data.db: SQLite database
-weather_dashboard.html: Generated visualization
-requirements.txt: Python Dependencies

Future Improvements:
-Deploy to AWS Lambda for automation
-Support multiple cities
-Add real-time data streaming
-Add an interactive dashboard with Flask
