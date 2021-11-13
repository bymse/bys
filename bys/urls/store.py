from .. import db as _db


def find_short_url(url):
    doc = _db.urls.find_one({url})
    return doc.short_url if doc else None
