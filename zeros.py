import json
import os

def get_plays_over_time():
    levels = {}

    for filename in os.listdir("downloaded_versions"):
        if filename.endswith(".txt"):
            with open(os.path.join("downloaded_versions", filename), "r") as f:
                levels_data = json.load(f)
                for level in levels_data:
                    level_id = level["identifier"]
                    if level_id not in levels:
                        levels[level_id] = {
                            "levelId": level_id,
                            "title": level["title"],
                            "plays": []
                        }
                    
                    # Get the last-known plays for this level if available
                    last_known_plays = levels[level_id]["plays"][-1][-1] if levels[level_id]["plays"] else 0

                    # Append the plays data for the current file
                    levels[level_id]["plays"].append([filename.split("_")[0], level.get("statistics", {}).get("total_played", last_known_plays)])
        print(f"Processed {filename}.")

    with open("plays_over_time.json", "w") as f:
        json.dump(levels, f, indent=4)

get_plays_over_time()
