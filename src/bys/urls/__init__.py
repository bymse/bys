from flask import (
    Blueprint, redirect, render_template, abort
)

from bys.urls import handlers
from bys.urls import url_form

bp = Blueprint('urls', __name__, template_folder='../../templates')


@bp.route('/', methods=['GET'])
def index():
    form = url_form.UrlForm()
    return render_template('index.html', form=form)


@bp.route('/', methods=['POST'])
def create():
    form = url_form.UrlForm()
    short_url = handlers.handle_create(form.url.data) if form.validate_on_submit() else None
    return render_template('index.html', form=form, short_url=short_url)


@bp.route('/<code>', methods=['GET'])
def redirect_short_url(code):
    full_url = handlers.handle_short_url(code)
    if not full_url:
        abort(404)

    return render_template('redirect-page.html', url=full_url)
