"""Forms for Flask Notes app"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length, Email

class AddUserForm(FlaskForm):
    """Form for adding users"""

    username = StringField("Username",
                        validators=[InputRequired(), Length(1,20)])
    password = PasswordField("Password",
                           validators=[InputRequired()])
    email = EmailField("Email Address",
                            validators=[InputRequired(), Email(), Length(1,50)])
    first_name = StringField('First Name',
                             validators = [InputRequired(), Length(1,30)])
    last_name = StringField('Last Name',
                             validators = [InputRequired(), Length(1,30)])
    
class LoginForm(FlaskForm):
    """Form for logging in users"""

    username = StringField("Username",
                        validators=[InputRequired(), Length(1,20)])
    password = PasswordField("Password",
                           validators=[InputRequired()])


#TODO: change to AddOrEditForm
class AddNoteForm(FlaskForm):
    """Form for adding a note"""
    
    title = StringField("Title",
                        validators=[InputRequired(), Length(1,20)])
    content = StringField("Content",
                        validators=[InputRequired(), Length(1,20)])