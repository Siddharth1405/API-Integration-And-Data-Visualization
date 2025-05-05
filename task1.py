import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator

API_KEY = 'API_KEY'
CITY = 'Mumbai'
UNITS = 'metric'
BASE_URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units={UNITS}'

def fetch_weather_data():
    """Fetch weather data from OpenWeatherMap API"""
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        data = response.json()
        
        if data.get('cod') != '200':
            raise ValueError(f"API Error: {data.get('message', 'Unknown error')}")
            
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def process_data(data):
    """Process API data into DataFrame"""
    if not data or 'list' not in data:
        print("Invalid data structure received from API")
        return None
        
    processed_data = []
    for forecast in data['list']:
        processed_data.append({
            'DateTime': forecast['dt_txt'],
            'Temperature (°C)': forecast['main']['temp'],
            'Humidity (%)': forecast['main']['humidity'],
            'Wind Speed (m/s)': forecast['wind']['speed']
        })
    
    return pd.DataFrame(processed_data)

def create_visualizations(df):
    """Create professional weather visualizations"""
    if df is None or df.empty:
        print("No data to visualize")
        return
    
    df['DateTime'] = pd.to_datetime(df['DateTime'])
    df.sort_values('DateTime', inplace=True)
    
    plt.style.use('default') 
    plt.rcParams.update({
        'axes.facecolor': 'white',
        'axes.grid': True,
        'grid.color': '#eeeeee',
        'axes.edgecolor': '#cccccc',
        'axes.linewidth': 0.8,
        'font.size': 11
    })
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle(f'5-Day Weather Forecast for {CITY}', y=0.98, fontsize=16)
    
    ax1.plot(df['DateTime'], df['Temperature (°C)'], 
            color='#ff7f0e', 
            linewidth=2.5,
            marker='o',
            markersize=6)
    
    ax1.set_title('Temperature Trend', fontsize=14, pad=15)
    ax1.set_ylabel('Temperature (°C)', fontsize=12)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%a\n%b %d'))
    ax1.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    ax1.grid(True, alpha=0.6)
    
    bars = ax2.bar(df['DateTime'], df['Humidity (%)'],
                  color='#1f77b4',
                  width=0.03,
                  edgecolor='white',
                  linewidth=0.7)
    
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height+1.5,
                f'{int(height)}%',
                ha='center', va='bottom',
                fontsize=10,
                color='#1f77b4')
    
    ax2.set_title('Humidity Levels', fontsize=14, pad=15)
    ax2.set_ylabel('Humidity (%)', fontsize=12)
    ax2.set_ylim(0, 100)
    ax2.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%a\n%b %d'))
    ax2.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    ax2.grid(True, alpha=0.6, axis='y')
    
    for ax in [ax1, ax2]:
        ax.tick_params(axis='both', which='major', labelsize=10)
        ax.set_xlabel('Date', fontsize=12)
        plt.setp(ax.get_xticklabels(), rotation=0, ha='center')
    
    plt.tight_layout()
    plt.savefig('professional_weather_forecast.png', 
               dpi=300, 
               bbox_inches='tight',
               facecolor='white')
    plt.show()

if __name__ == "__main__":
    weather_data = fetch_weather_data()
    if weather_data:
        weather_df = process_data(weather_data)
        if weather_df is not None:
            create_visualizations(weather_df)
