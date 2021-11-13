from pymongo import MongoClient
import pymongo

from flask import current_app
from flask import g

_db = None
urls = None


def init(config):
    global _db, urls
    client = MongoClient(
        host=config["MongoDB:Host"],
        port=config["MongoDB:Port"]
    )
    _db = client[config["MongoDB:Database"]]
    urls = _db.urls
