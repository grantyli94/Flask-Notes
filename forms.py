"""Forms for Flask Notes app"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, PasswordField
from wtforms.validators import InputRequired, Optional, URL, Length, Email

class AddUserForm(FlaskForm):
    """Form for adding users"""

    username = StringField("Username",
                        validators=[InputRequired(), Length(1,20)])
    password = PasswordField("Password",
                           validators=[InputRequired()])
    email = StringField("Email Address",
                            validators=[InputRequired(), Email(), Length(1,50)])
    first_name = StringField('First Name',
                             validators = [InputRequired(), Length(1,30)])
    last_name = StringField('Last Name',
                             validators = [InputRequired(), Length(1,30)])
    
    