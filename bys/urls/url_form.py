from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, URL


class UrlForm(FlaskForm):
    url = StringField('url', validators=[InputRequired(), URL()])
