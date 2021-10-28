from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class registration_form(FlaskForm):
    """description of class"""
    username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
class login_form(FlaskForm):
    """description of class"""
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    member_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')

