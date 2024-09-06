from flask_wtf import FlaskForm
from wtforms import validators,StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,equal_to,Email




class RegisterForm(FlaskForm):
    username=StringField('username',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    conf_password=PasswordField('Confirm password',validators=[DataRequired(),equal_to('password')])
    submit=SubmitField('Register')



class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Login')
