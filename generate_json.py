import os
import json
from git import Repo

repo_path = "../grab-tools.live"
file_name = "stats_data/all_verified.json"
alt_file_name = "public/stats_data/all_verified.json"
output_dir = "downloaded_versions"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

repo = Repo(repo_path)

def download_commit(commit, file_path):
    commit_hash = commit.hexsha
    commit_date = commit.committed_date
    commit_message = commit.message.strip()
    if f"{commit_date}_{commit_message}.json" in os.listdir(output_dir):
        print(f"Skipping {commit_date}_{commit_message}.json")
        return

    file_content = repo.git.show(f"{commit_hash}:{file_path}")
    version_filename = f"{commit_date}_{commit_message}.txt"
    version_filepath = os.path.join(output_dir, version_filename)

    with open(version_filepath, "w") as f:
        f.write(file_content)

    json_data = {
        "filename": file_path,
        "date": commit_date,
        "message": commit_message,
        "hash": commit_hash
    }
    json_filename = f"{commit_date}_{commit_message}.json"
    json_filepath = os.path.join(output_dir, json_filename)

    with open(json_filepath, "w") as f:
        json.dump(json_data, f, indent=4)

for commit in repo.iter_commits(paths=[file_name, alt_file_name]):
    try:
        if file_name in commit.stats.files:
            download_commit(commit, file_name)
        elif alt_file_name in commit.stats.files:
            download_commit(commit, alt_file_name)
    except Exception as e:
        print(f"Error: {e}")

print("All versions downloaded with metadata.")
