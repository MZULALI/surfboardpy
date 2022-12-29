import api
import recommendations

def main():
    # Get the surf spot ID and number of days to forecast
    surf_spot_id = "5842041f4e65fad6a7708835"
    days = 2

    # Get the wave, wind, and tide data for the beach
    wave_data = api.get_wave_data(surf_spot_id, days)
    wind_data = api.get_wind_data(surf_spot_id, days)
    tides_data = api.get_tides_data(surf_spot_id, days)

    # Recommend a surfboard based on the conditions
    surfboard_recommendation = recommendations.recommend_surfboard(wave_data, wind_data, tides_data)
    print("Surfboard recommendation:", surfboard_recommendation)

    # Recommend a skill level based on the conditions
    skill_level_recommendation = recommendations.recommend_skill_level(wave_data, wind_data, tides_data)
    print("Skill level recommendation:", skill_level_recommendation)


if __name__ == "__main__":
    main()
