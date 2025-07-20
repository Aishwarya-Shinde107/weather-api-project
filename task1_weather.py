import requests

city = input("Enter city name: ")
api_key = "05563d58b2e8a85cbd34042b24bca6b9"  # 👈 Replace with your API key
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    print(f"\nWeather in {city}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Condition: {data['weather'][0]['description']}")
else:
    print("❌ City not found or error in API!")