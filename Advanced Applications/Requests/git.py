import requests


url = "https://api.github.com/search/users?q=Q"

query_params = {
    "q": "user", 
    "sort": "followers",       
    "order": "desc"         
}

try:

    response = requests.get(url, params=query_params, timeout=10)
    response.raise_for_status() 
    
    data = response.json()
    users = data['items']
    print(f" We Get {len(users)} ✅ :")

    print("-" * 50)

    for user in users:
        if user['type'] == 'User':

            username = user['login']
            profile_url = user['html_url']
            user_id = user['id']
            if int(user_id) > 1000 :
                print(f"👤 User: {username} | ID: {user_id}")
                print(f"🔗 Link: {profile_url}")
            print("-" * 20)

except Exception as e:
    print(f" Error Found ❌ : {e}")