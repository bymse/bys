from flask import current_app


def get_val(key):
    return current_app.config[key]
