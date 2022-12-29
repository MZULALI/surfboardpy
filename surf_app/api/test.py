import tides
import wind
import surfline

tides_data = tides.get_tides_data("5842041f4e65fad6a77088cc", 2)
wind_data = wind.get_wind_data("5842041f4e65fad6a77088cc", 2)
wave_data = surfline.get_wave_data("5842041f4e65fad6a77088cc", 2)

for data in tides_data:
    print(f"Time: {data['time']}")
    print(f"Tide type: {data['tides']['current']['type']}")

for data in wind_data:
    print(f"Wind Direction: {data['wind_speed']['directionType']}")
    print(f"Wind Speed: {data['wind_speed']['speed']}")

for data in wave_data:
    print(f"Wave height: {data['wave_height']['min']} - {data['wave_height']['max']}")
    print(f"Human relation: {data['wave_height']['human_relation']}")
