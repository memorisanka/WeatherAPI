from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class EntryForm(FlaskForm):
    localization = StringField('Enter the localization:', validators=[DataRequired()])
    submit = SubmitField('Confirm')