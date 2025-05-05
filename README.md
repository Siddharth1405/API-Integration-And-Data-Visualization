# API-Integration-And-Data-Visualization
Fetch, analyze, and visualize real-time weather forecasts using Python, OpenWeatherMap API, and Matplotlib.

**COMPANY**: CODETECH IT SOLUTIONS

**Name**: Siddharth Patel

**INTERN ID**: CT04DL819

**Domain**: Python Programming

**BATCH Duration**: 4 Weeks

**Mentor**: Neela Santhosh Kumar

**PROJECT**: API INTEGRATION AND DATA VISUALIZATION

# Weather Forecast Visualization Project

## Overview
This Python project fetches 5-day weather forecast data from the OpenWeatherMap API and creates professional visualizations showing temperature trends and humidity levels for Mumbai, India.

## Features
- **API Integration**: Connects to OpenWeatherMap's forecast API to retrieve weather data
- **Data Processing**: Transforms JSON API responses into a structured pandas DataFrame
- **Visualizations**:
  - Line chart showing temperature trends over 5 days
  - Bar chart displaying humidity percentages with value labels
- **Professional Styling**: Clean, modern visual design with:
  - Custom grid styling
  - Proper date formatting
  - Optimal color choices
  - Responsive layout

## Technical Details
- **Python Libraries Used**:
  - `requests` for API calls
  - `pandas` for data manipulation
  - `matplotlib` for visualizations
- **Configuration**:
  - Easily change city by modifying the `CITY` variable
  - Supports metric or imperial units
- **Output**:
![Image](https://github.com/user-attachments/assets/8724d74d-b21f-409d-974e-6c50600d33ee)

## Setup Instructions
1. Get an API key from [OpenWeatherMap](https://openweathermap.org/)
2. Replace `API_KEY` in the script with your actual key
3. Install required packages:
   ```bash
   pip install requests pandas matplotlib
   ```
4. Run the script:
   ```bash
   python task1.py
   ```

## Sample Output
The script generates a professional-looking visualization showing:
- Left panel: Temperature trend line chart
- Right panel: Humidity percentage bar chart
- Clean date formatting on x-axis
- Properly labeled axes with units

## Customization
- Change `CITY` to visualize weather for different locations
- Modify `UNITS` to switch between metric/imperial

## License
- **This project**: [MIT License](LICENSE) - Free for any use  
