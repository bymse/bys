from flask_wtf import FlaskForm
from wtforms import URLField
from wtforms.validators import DataRequired, URL


class UrlForm(FlaskForm):
    url = URLField('url', validators=[DataRequired(), URL()])
