from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from Flask_App.db_model import User


class RegisterForm(FlaskForm):
    username = StringField('Username',
                           validators=[
                               DataRequired(),
                               Length(min=2, max=30)
                           ])

    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ])

    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                                 Length(min=5, max=30)
                             ])

    confirm_password = PasswordField('Confirm Password',
                                     validators=[
                                         DataRequired(),
                                         EqualTo('password')
                                     ])

    submit = SubmitField('Sign Up')
    nav_button = SubmitField('Sign Up')

    # to check if entered username/email exists in DB
    # functions must have validate in its name
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('User name already exists.')

    def validate_email(self, email):
        email_id = User.query.filter_by(email=email.data).first()
        if email_id:
            raise ValidationError('Email address already in use.')


class LoginForm(FlaskForm):

    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ])

    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                                 Length(min=5, max=30)
                             ])

    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')