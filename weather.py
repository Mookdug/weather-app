import requests

API_KEY = "86f4a2bf5ea812a0e17c773480b18637"  # Replace this with your real API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'imperial'  # Change to 'metric' for Celsius
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"🌤️ {city.title()} — {desc}, {temp}°F")
    else:
        print(f"⚠️ Error: {data.get('message', 'Could not fetch weather')}")

def main():
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
