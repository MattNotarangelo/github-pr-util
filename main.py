"""
Get all PRs for a given user
"""

import collections
import datetime
import json
import os
import dotenv
import requests


### User supplied values
GITHUB_USER = "MattNotarangelo"
OPTIONAL_QUERY_ARGS = ["user:ROKT", "merged:2023-11-20..2024-02-22"]


dotenv.load_dotenv()

GRAPHQL_URL = "https://api.github.com/graphql"
API_TOKEN = os.getenv("GITHUB_API_TOKEN")
OUTPUT_FILE_NAME = "out.json"
OUTPUT_MD_NAME = "out.md"

if not API_TOKEN:
    raise SystemExit("GITHUB_API_TOKEN must be provided in a .env file")


### TODO
# output formatting


def send_query(query_args, pagination_cursor):
    query = f"""query
    {{
        search(query: "{' '.join(query_args)}", type: ISSUE, first: 100, after: {pagination_cursor}) {{
            edges {{
                node {{
                    ... on PullRequest {{
                    title
                    repository {{
                        nameWithOwner
                    }}
                    createdAt
                    mergedAt
                    url
                    }}
                }}
            }}
            pageInfo {{
                endCursor
                hasNextPage
            }}
        }}
    }}"""

    # print(query)
    r = requests.post(
        GRAPHQL_URL,
        headers={
            "Authorization": f"bearer {API_TOKEN}",
        },
        json={"query": query},
        timeout=10,
    )

    return r.json()


def transform_data(d):
    new = collections.defaultdict(list)
    for i in d:
        repo = i["node"]["repository"]["nameWithOwner"]
        i["node"]["repository"] = repo  # rename field
        i["node"]["comment"] = ""  # add comment field
        new[repo].append(i["node"])

    return new


# REFACTOR THIS
def merge_with_existing_data(d):
    existing = {}
    existing_urls = set()
    if os.path.isfile(OUTPUT_FILE_NAME):
        with open(OUTPUT_FILE_NAME, "r", encoding="utf-8") as f:
            existing = json.load(f)
            for i in existing:
                for j in existing[i]:
                    existing_urls.add(j["url"])

    for i in d:
        for j in d[i]:
            if j["url"] not in existing_urls:
                if j["repository"] not in existing:
                    existing[j["repository"]] = []
                existing[j["repository"]].append(j)

        existing[i].sort(key=lambda x: datetime.datetime.strptime(x["createdAt"], "%Y-%m-%dT%H:%M:%SZ"), reverse=True)

    return existing


def write_newline(fp):
    fp.write("\n")


def write_h2_header(fp, text):
    fp.write(f"## {text}")
    write_newline(fp)
    write_newline(fp)


def write_table_header(fp):
    fp.write("Pull request|Impact")
    write_newline(fp)
    fp.write("---|---")
    write_newline(fp)


def write_table_content(fp, d):
    for i in d:
        if i["comment"] != "skip":
            fp.write(f"[{i['title']}]({i['url']})|{i['comment']}")
            write_newline(fp)


def output_markdown(d):
    with open(OUTPUT_MD_NAME, "w") as f:
        f.write("# Github pull requests")
        write_newline(f)
        write_newline(f)

        for i in d:
            write_h2_header(f, i)
            write_table_header(f)
            write_table_content(f, d[i])
            write_newline(f)


if __name__ == "__main__":
    query_arguments = [
        "is:pr",
        "is:closed",
        "is:merged",
        "sort:created-desc",
        f"author:{GITHUB_USER}",
        *OPTIONAL_QUERY_ARGS,
    ]

    has_next_page = True
    cursor = "null"
    data = []
    while has_next_page:
        resp = send_query(query_arguments, cursor)
        page_info = resp["data"]["search"]["pageInfo"]
        has_next_page = page_info["hasNextPage"]
        cursor = f'"{page_info["endCursor"]}"'

        data.extend(resp["data"]["search"]["edges"])

    data = transform_data(data)
    data = merge_with_existing_data(data)
    with open(OUTPUT_FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f)

    output_markdown(data)
