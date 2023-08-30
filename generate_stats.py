import json, os

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
                        # statistics total_played
                    if "statistics" in level:
                        levels[level_id]["plays"].append([filename.split("_")[0], level["statistics"].get("total_played", 0)])
        print(f"Processed {filename}.")

    with open("plays_over_time.json", "w") as f:
        json.dump(levels, f, indent=4)

get_plays_over_time()