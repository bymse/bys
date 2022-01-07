from flask import current_app
import os


def get_val(key):
    return current_app.config[key]


def get_base_url():
    return os.environ["BYS_BASE_URL"]


def get_mongo_uri():
    return os.environ["BYS_MONGO_URI"]
