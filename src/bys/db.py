from pymongo import MongoClient
from bys.config import get_mongo_uri

urls = None


def init():
    global urls
    client = MongoClient(get_mongo_uri())
    urls = client.bys.urls
