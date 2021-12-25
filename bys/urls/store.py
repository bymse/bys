from .. import db as _db


def find_alphanum_code(full_url):
    data = _db.urls.find_one({'full_url': full_url}, {'alphanum_code': 1})
    return data and data["alphanum_code"]


def num_code_exists(num_code):
    return _db.urls.count_documents({'num_code': num_code}, limit=1) != 0


def save_url(num_code, alphanum_code, full_url):
    _db.urls.insert_one({'num_code': num_code, 'alphanum_code': alphanum_code, 'full_url': full_url})


def find_full_url(code):
    data = _db.urls.find_one({'alphanum_code': code}, {'full_url': 1})
    return data and data["full_url"]
