# recommendations/surfboard.py

def recommend_surfboard(wave_data, wind_data, tide_data):
    # Determine the average wave height and wind speed over the forecast period
    wave_height = sum([data['wave_height']['max'] for data in wave_data]) / len(wave_data)
    wind_speed = sum([data['wind_speed']['speed'] for data in wind_data]) / len(wind_data)
    tide = tide_data[0]['tides']['current']['type']

    # Recommend a surfboard based on the conditions
    if wave_height > 8 and wind_speed > 1:
        return "Looks like it's going to be pretty gnarly out there! You'll want to grab your big gun surfboard and hang on tight! The large waves and strong wind will require a more sturdy and powerful board to ride them."
    elif wave_height > 4 and wind_speed > 4:
        return "The waves look like they'll be pretty decent, but the wind is picking up. You might want to grab a mid-size surfboard to handle the conditions. The mid-size board will allow you to maneuver through the waves more easily and handle the gusty wind."
    elif wave_height < 3 and wind_speed < 5 and tide == "low":
        return "The waves are small and the wind is calm. This is the perfect time to grab your longboard and cruise the line-up! The longboard will provide a stable and smooth ride on the small waves, and the calm wind will allow you to easily paddle and catch them."
    elif wave_height < 3 and wind_speed < 5 and tide == "high":
        return "The waves are small and the wind is calm. This is the perfect time to grab your foamie and have some fun! The foamie is a great beginner's board that is easy to catch small waves with, and the calm wind won't interfere with your ride."
    else:
        return "The conditions are looking good for surfing! Grab any surfboard that you're comfortable with and go out there and shred!"
