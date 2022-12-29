# surf_recommender/app.py
import json
from flask import Flask, render_template
import api
import recommendations

app = Flask(__name__)

@app.route('/')
def index():
    # Get the surf spot ID and number of days to forecast
    surf_spot_id = "5842041f4e65fad6a77088cc"
    days = 2

    # Get the wave, wind, and tide data for the beach
    wave_data = api.get_wave_data(surf_spot_id, days)
    wind_data = api.get_wind_data(surf_spot_id, days)
    tides_data = api.get_tides_data(surf_spot_id, days)

    # Recommend a surfboard based on the conditions
    surfboard_recommendation = recommendations.recommend_surfboard(wave_data, wind_data, tides_data)

    skill_level_recommendation = recommendations.recommend_skill_level(wave_data, wind_data, tides_data)


    # Recommend a skill level based on the conditions
     # Read the contents of the JSON files
    with open('data/beach_data.json', 'r') as f:
        beach_data = json.load(f)
    with open('data/surfboard_data.json', 'r') as f:
        surfboard_data = json.load(f)
    with open('data/skill_level_data.json', 'r') as f:
        skill_level_data = json.load(f)

    return render_template('index.html', surfboard_recommendation=surfboard_recommendation, tides_data=tides_data, beach_data=beach_data, skill_level_recommendation=skill_level_recommendation, surfboard_data=surfboard_data, skill_level_data=skill_level_data)
if __name__ == "__main__":
    app.run()
