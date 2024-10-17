import json
import os

import requests
from dotenv import load_dotenv


def get_secrets():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    return api_key


def load_footballdata(api_key=get_secrets()):
    # TODO: where to put these? .env?
    TEAMID = 7397  # Como FC
    COMPETITION = "SA"  # Serie A
    uri = "https://api.football-data.org/v4/"

    headers = {"X-Auth-Token": f"{api_key}"}

    resources = [
        f"teams/{TEAMID}",  # Team details
        f"teams/{TEAMID}/matches",  # Team's matches
        f"competitions/{COMPETITION}/standings",  # Competition standings
    ]

    for resource in resources:
        response = requests.get(uri + resource, headers=headers)
        yield response.json()  # using generator to avoid keep everything in memory


def main():
    data = load_footballdata()

    while True:
        try:
            result = next(data)
            print(json.dumps(result, indent=4))
        except StopIteration:
            break


if __name__ == "__main__":
    main()
