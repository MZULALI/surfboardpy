import json

# Load the beach data from the JSON file
with open("beach_data.json", "r") as f:
    beach_data = json.load(f)

# Load the surfboard data from the JSON file
with open("surfboard_data.json", "r") as f:
    surfboard_data = json.load(f)

# Load the skill level data from the JSON file
with open("skill_level_data.json", "r") as f:
    skill_level_data = json.load(f)
