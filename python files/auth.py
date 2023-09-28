from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# class RegistrationForm(FlaskForm):
#     username=StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
#     email=StringField('Email', validators=[DataRequired(), Email()])
#     password=PasswordField('Password', validators=[DataRequired(), Length(min=12, max=30)])
#     confirm_password=PasswordField('Confirm Password',
#                                    validators=[DataRequired(), EqualTo('password')])
#     # activation_code=
#     submit = SubmitField('Create Admin User')
    
class LoginForm(FlaskForm):
    email=StringField('Email', validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit = SubmitField('Login')