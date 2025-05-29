import requests

API = "https://api.encar.com"
SEARCH_ENDPOINT = API + r"/search/car/list/premium?count=true&q=(And.Hidden.N.)&sr=%7CModifiedDate%7C0%7C20"


def get_cars(url: str) -> requests.Response:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
    }
    return requests.get(url, headers=headers)


if __name__ == "__main__":
    r = get_cars(SEARCH_ENDPOINT)
    jsoned = r.json()
    if not jsoned.get("SearchResults"):
        raise Exception("Empty search result returned")

    for car in jsoned["SearchResults"]:
        print(car)
