import requests

api_key = '30d4741c779ba94c470ca1f63045390a'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.status_code == 404:
    print("No City Found")
else:
    weather_json = weather_data.json()
    weather = weather_json['weather'][0]['main']
    temp = round(weather_json['main']['temp'])
    
    # Check if rain information is available
    if 'rain' in weather_json:
        rain = weather_json['rain'].get('1h', 0)  # 1-hour rain volume in mm
        print(f"Rain (1hr): {rain} mm")
    else:
        print("No rain information available.")
    
    # Check if visibility information is available
    if 'visibility' in weather_json:
        visibility = weather_json['visibility']  # Visibility in meters
        print(f"Visibility: {visibility} meters")
    else:
        print("Visibility information not available.")
    
    # Check if haze information is available
    if 'weather' in weather_json:
        for item in weather_json['weather']:
            if 'haze' in item['description'].lower():
                print("Haze: Yes")
                break
        else:
            print("Haze: No")
    
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºF")
