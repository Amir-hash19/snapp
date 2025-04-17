import requests


def get_route_from_neshan(origin_lat, origin_lng, dest_lat, dest_lng):
    api_key = 'YOUR_API_KEY'
    url = f"https://api.neshan.org/v4/direction?origin={origin_lat},{origin_lng}&destination={dest_lat},{dest_lng}"
    
    headers = {
        'Api-Key': api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}
