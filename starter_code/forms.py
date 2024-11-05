from datetime import datetime
from flask import request
from flask_wtf import FlaskForm as Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField, ValidationError
from wtforms.validators import DataRequired, AnyOf, URL
from enums import Genre, State
import re
from models import Venue, Artist

# Method to validate phone number
def is_valid_phone(number):
    # Compile the regex of allowed input for number 
    # [3 digits followed by -.space then 3 digits followed by -.space then 4 digits]
    regex = re.compile(r'^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$')
    # returns if given number matches regex
    return regex.match(number)

def is_valid_artist(artist_id):
    is_valid = True
    try:
        if Artist.query.get(int(request.form['artist_id'])) is None:
            raise Exception()
    except:
        is_valid = False
    return is_valid

def is_valid_venue(venue_id):
    is_valid = True
    try:
        if Venue.query.get(int(request.form['venue_id'])) is None:
            raise Exception()
    except:
        is_valid = False
    return is_valid

class ShowForm(Form):
    artist_id = StringField(
        'artist_id', validators=[DataRequired()],
    )
    venue_id = StringField(
        'venue_id', validators=[DataRequired()],
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

    # Methods to validate the different form fields
    def validate_artist_id(self, field):
        if not is_valid_artist(field.data):
            raise ValidationError('Invalid artist ID.')
        
    def validate_venue_id(self, field):
        if not is_valid_venue(field.data):
            raise ValidationError('Invalid venue ID.')

    def validate(self, **kwargs):
        return super(ShowForm, self).validate(**kwargs)

class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=State.choices()
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=Genre.choices()
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )
    website_link = StringField(
        'website_link'
    )

    seeking_talent = BooleanField( 'seeking_talent' )

    seeking_description = StringField(
        'seeking_description'
    )

    # Methods to validate the different form fields
    def validate_phone(self, field):
        if not is_valid_phone(field.data):
            raise ValidationError('Invalid number.')
    
    def validate_state(self, field):
        if field.data not in dict(State.choices()).keys():
            raise ValidationError('Invalid state.')
        
    def validate_genres(self, field):
        if not set(field.data).issubset(dict(Genre.choices()).keys()):
            raise ValidationError('Invalid genres.')
        
    def validate(self, **kwargs):
        return super(VenueForm, self).validate(**kwargs)



class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=State.choices()
    )
    phone = StringField(
        # TODO implement validation logic for phone 
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=Genre.choices()
     )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[URL()]
     )

    website_link = StringField(
        'website_link'
     )

    seeking_venue = BooleanField( 'seeking_venue' )

    seeking_description = StringField(
            'seeking_description'
     )
    
    # Methods to validate the different form fields
    def validate_phone(self, field):
        if not is_valid_phone(field.data):
            raise ValidationError('Invalid number.')
        
    def validate_state(self, field):
        if field.data not in dict(State.choices()).keys():
            raise ValidationError('Invalid state.')
        
    def validate_genres(self, field):
        if not set(field.data).issubset(dict(Genre.choices()).keys()):
            raise ValidationError('Invalid genres.')
        
    def validate(self, **kwargs):
        return super(ArtistForm, self).validate(**kwargs)

