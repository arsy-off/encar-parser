import os
import requests
import logging
from pymongo import MongoClient, database
from fake_useragent import UserAgent
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

SELENIUM_URL = os.getenv("SELENIUM_URL", "http://localhost:4444/wd/hub")
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://admin:admin@mongodb:27017/")
WEBSITE = "https://car.encar.com/"
API = "https://api.encar.com"
VERIFY_ENDPOINT = API + r"/pass/user/verify"
SEARCH_ENDPOINT = API + r"/search/car/list/premium?count=true&q=(And.Hidden.N.)&sr=%7CModifiedDate%7C0%7C20"


def verify(agent: str) -> None:
    logging.info(f"Starting verification process with remote ChromeDriver. Remote url: {SELENIUM_URL}")
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-webrtc")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    options.add_argument(f"--user-agent={agent}")
    driver = webdriver.Remote(
        command_executor=SELENIUM_URL,
        options=options
    )
    driver.get(WEBSITE)
    sleep(15)
    driver.close()


def get_cars(agent: str) -> requests.Response:
    headers = {
        "User-Agent": agent
    }
    logging.info(f"[GET] {SEARCH_ENDPOINT} with headers={headers}")
    return requests.get(SEARCH_ENDPOINT, headers=headers)


def connect_to_db(db_name: str) -> database.Database:
    logging.info("Connecting to mongo..")
    mongo_client = MongoClient(MONGODB_URL)

    return mongo_client.get_database(db_name)


if __name__ == "__main__":
    db = connect_to_db("encar")
    ua = UserAgent().chrome

    verify(ua)
    r = get_cars(ua)
    logging.info(f"Response code: {r.status_code}")
    if r.status_code != 200:
        raise Exception("Unsuccessful api call. Please check verification process")

    jsoned = r.json()
    if not jsoned.get("SearchResults"):
        raise Exception("Empty search result returned")

    db.premium.insert_many(jsoned["SearchResults"])
