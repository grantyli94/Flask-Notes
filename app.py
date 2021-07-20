"""Flask app for Users"""

from models import User, db, connect_db
from flask import Flask, request, jsonify, render_template, redirect
from forms import AddUserForm
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SECRET_KEY'] = "gfudhiaskhjl543278489grhuiger8934"
toolbar = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route('/')
def root():
    """Redirects to /register"""

    return redirect('/register')

@app.route('/register')
def show_register_form():
    form = AddUserForm()