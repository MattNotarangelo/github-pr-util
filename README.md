# Github-PR-util

This is a tool which gets all the PRs made by a user and exports them to json and md.

## Usage

Add github api token to `.env` file (requires repo scope and organization access if you want PRs within that org)
```
GITHUB_API_TOKEN=ghp_xxx
```

Fill in the user supplied values section in main.py
```py
### User supplied values
GITHUB_USER = "Github_username"
# OPTIONAL_QUERY_ARGS = ["user:ROKT"] # get PRs in org:ROKT
OPTIONAL_QUERY_ARGS = ["user:ROKT", "merged:2024-03-01..2024-10-03"] # get PRs in org:ROKT within a specified time range
```

Run with `poetry install --no-root && poetry run python3 main.py`

This will generate a json and md file in the project directory.

## JSON file

This file is designed to be cumulatively added to, meaning other runs of the program will add to the file and not overwrite it. For that reason, each JSON entry has a `comment` field which can be used to outline the impact of the PR. This will show up in the md file when the program is rerun. If you would like the PR to not show up in the md file, you can add `"comment": "skip"` to the desired entries.
