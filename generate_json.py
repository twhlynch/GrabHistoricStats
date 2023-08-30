import os
import json
from git import Repo

repo_path = "../grab-tools.live"
file_name = "public/stats_data/all_verified.json"
output_dir = "downloaded_versions"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

repo = Repo(repo_path)

for commit in repo.iter_commits(paths=file_name):
    commit_hash = commit.hexsha
    commit_date = commit.committed_date
    commit_message = commit.message.strip()

    file_content = repo.git.show(f"{commit_hash}:{file_name}")
    version_filename = f"{commit_date}_{commit_message}.txt"
    version_filepath = os.path.join(output_dir, version_filename)

    with open(version_filepath, "w") as f:
        f.write(file_content)

    json_data = {
        "filename": file_name,
        "date": commit_date,
        "message": commit_message,
        "hash": commit_hash
    }
    json_filename = f"{commit_date}_{commit_message}.json"
    json_filepath = os.path.join(output_dir, json_filename)

    with open(json_filepath, "w") as f:
        json.dump(json_data, f, indent=4)

print("All versions downloaded with metadata.")
