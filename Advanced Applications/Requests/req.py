import requests

my_headers = {'User-Agent':'Agent-Essam'}
my_params = {'ID':'107','Type':'INT'}
my_secret_data = {'Status':'Misson_Complete'}

try :

    posted_data = requests.post("https://httpbin.org/post",headers=my_headers,params=my_params,data=my_secret_data,timeout=5)

    posted_data.raise_for_status()

    response = posted_data.json()

    for key,value in response.items():
        print(f"{key} -> {value}")

except Exception as e:
    print(f"Error : {e}")




