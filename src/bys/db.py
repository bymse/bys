from pymongo import MongoClient
import os

urls = None


def init():
    global urls
    client = MongoClient(os.environ["bys_mongo_uri"])
    urls = client.bys.urls
