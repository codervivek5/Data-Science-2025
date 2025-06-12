from mcp.server.fastmcp import FastMCP
import requests

# Initialize MCP server
mcp = FastMCP("WeatherServer")

API_KEY = "your_openweathermap_api_key"  # 🔐 Replace with your API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Add weather resource
@mcp.resource("weather://{city}")
def get_weather(city: str) -> str:
    """Get real-time weather info for a city"""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        return f"Current weather in {city}: {temp}°C, {weather}"
    else:
        return f"Could not fetch weather for {city}. Please check the city name."

