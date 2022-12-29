import datetime
import requests

def get_wind_data(surf_spot_id, days):
    api_url = f"https://services.surfline.com/kbyg/spots/forecasts/wind?spotId={surf_spot_id}&days={days}&intervalHours=4"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    }

    data = requests.get(api_url, headers=headers).json()

    wind_data = []
    for day in data["data"]["wind"]:
        time = (
            datetime
            .datetime
            .fromtimestamp(day['timestamp'])
            .strftime('%Y-%m-%d %H:%M:%S')
        )
        wind_data.append({
            "time": time,
            "wind_speed": {
                "directionType": day["directionType"],
                "speed": int(day["speed"]),
            }
        })
    return wind_data
