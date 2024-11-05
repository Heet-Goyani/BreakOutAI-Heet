import requests

# Here we have to put our access token
ACCESS_TOKEN = "your_access_token"
BASE_URL = "https://api.upstox.com/live/options"

def get_option_chain(instrument_key, expiry_date):
    """Fetches the options chain data for a given instrument and expiry date."""
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Accept": "application/json"
    }
    params = {
        "instrument_key": instrument_key,
        "expiry_date": expiry_date
    }
    
    try:
        response = requests.get(f"{BASE_URL}/get-pc-option-chain", headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data.get("status") == "success":
            return data.get("data", [])
        else:
            print("Request failed:", data)
    except requests.RequestException as e:
        print(f"API request error: {e}")
    
    return None
