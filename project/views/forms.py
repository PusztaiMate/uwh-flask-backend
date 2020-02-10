from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class RegisterPlayerForm(FlaskForm):
    fname = StringField("Keresztnév", validators=[DataRequired()])
    lname = StringField("Vezetéknév", validators=[DataRequired()])
