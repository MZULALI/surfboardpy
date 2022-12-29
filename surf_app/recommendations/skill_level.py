# recommendations/skill_level.py

def recommend_skill_level(wave_data, wind_data, tide_data):
    # Determine the average wave height, wind speed, and tide type over the forecast period
    wave_height = sum([data['wave_height']['max'] for data in wave_data]) / len(wave_data)
    wind_speed = sum([data['wind_speed']['speed'] for data in wind_data]) / len(wind_data)
    tide_type = tide_data[0]['tides']['current']['type']

    # Recommend a skill level based on the wave, wind, and tide data
    if wave_height > 6 and wind_speed > 15:
        return "5 stars (Advanced) - If you're not already a pro surfer, you might want to sit this one out. The waves are huge and the wind is strong, so you'll need to be at the top of your game to tackle these conditions."
    elif wave_height > 4 and wind_speed > 10:
        return "4 stars (Intermediate) - The waves are decent and the wind is picking up, so you'll need some intermediate skills to ride these conditions. Make sure you have a good handle on your board and are comfortable in choppy water before heading out."
    elif wave_height < 3 and wind_speed < 5 and tide_type == "low":
        return "2 stars (Beginner) - The waves are small and the wind is calm, so this is the perfect opportunity for beginners to get out and catch some easy rides. Just make sure to watch out for rocks and other hazards in the lineup."
    elif wave_height < 3 and wind_speed < 5 and tide_type == "high":
        return "3 stars (Intermediate) - The waves are small and the wind is calm, but the tide is high which can make it a bit more challenging to catch the waves. This is a good opportunity for intermediate surfers to practice their timing and positioning in the lineup."
    else:
        return "3 stars (Intermediate) - The waves and wind are looking average, so this is a good opportunity for intermediate surfers to get out and ride some fun waves. Just make sure to pay attention to the changing conditions and adjust your surfboard accordingly."
