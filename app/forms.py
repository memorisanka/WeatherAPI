from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class EntryForm(FlaskForm):
    localization = StringField(validators=[DataRequired()])
    submit = SubmitField('Confirm')
