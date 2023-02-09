from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, ValidationError, TextAreaField, SubmitField
from wtforms.validators import EqualTo, Email, DataRequired, Length
from .models import User
from flask import flash


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_email(self, email):
        email_exists = User.query.filter_by(email=email.data).first()
        if email_exists:
            flash('Email is already taken', category='error')
            raise ValidationError('Email is already taken')

    def validate_username(self, username):
        username_exists = User.query.filter_by(username=username.data).first()
        if username_exists:
            flash('Username is already taken', category='error')
            raise ValidationError('Username is already taken')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')



