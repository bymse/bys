from .. import db as _db


def find_alphanum_code(full_url):
    return _db.urls.find_one({full_url}, {'alphanum_code': 1})


def num_code_exists(num_code):
    return _db.urls.count_documents({num_code}, limit=1) != 0


def save_url(num_code, alphanum_code, full_url):
    _db.urls.insert_one({num_code, alphanum_code, full_url})
