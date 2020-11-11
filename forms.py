#this file is to write and remember login information 
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField ,SubmitField,BooleanField #fields
from wtforms.validators import DataRequired, Length, Email, EqualTo #fields formating

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
    validators =[DataRequired(), Length(min = 2, max = 20)]) #non empty and max 20 char username
    email = StringField('Email',
    validators = [DataRequired(), Email()]) 
    password = PasswordField('Password',validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',validators = [DataRequired(), Email()]) 
    password = StringField('Password',validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


    
