import requests

params = {"access_key" : '000e2853e5a67fac630526f42e4ad9fe',"query":'New York'}

try:
    response = requests.get("https://api.weatherstack.com/current", timeout=5,params=params)
    print(response.status_code)
    weather = response.json()['current']

    for key , value in weather.items():
        print(f"{key} -> {value}")

except Exception as e:
    print(f"Error : {e}")

