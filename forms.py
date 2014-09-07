from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf import Form
__author__ = 'ariel'


class LoginForm(Form):
    user = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
