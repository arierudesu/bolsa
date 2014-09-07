from flask import Flask, request
from forms import LoginForm
__author__ = 'ariel'

#   Config
app = Flask(__name__)
app.config.from_object('config')


#   Routes

#   Homepage (Redirect to login.html)
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
