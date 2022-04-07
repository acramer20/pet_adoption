from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, URL, Optional, NumberRange


pets = ['dog', 'cat', 'hamster', 'bird', 'frog', 'guinea pig', 'lizard', 'snake']
class AddPetForm(FlaskForm):
    """Form for adding a new pet"""

    name = StringField('Name of Pet', validators=[InputRequired()])

    species = SelectField('Species of Pet', choices=[(p, p) for p in pets], validators=[InputRequired()])

    photo_url = StringField('URL to Picture of Pet', validators=[Optional(), URL()])

    age = IntegerField('Pet age', validators=[NumberRange(min=0,max=30)])

    notes = StringField('Notes about pet')

    available = BooleanField('Is Pet Available?')
