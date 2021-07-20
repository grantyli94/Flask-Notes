"""Flask app for Users"""

from models import User, db, connect_db
from flask import Flask, request, jsonify, render_template, redirect, session
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

@app.route('/register', methods=['POST',"GET"])
def show_register_form():
    form = AddUserForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        password = form.password.data
        email = form.email.data 

        user = User.register(username, 
                             password, 
                             first_name, 
                             last_name,
                             email)
        db.session.add(user)
        db.session.commit()

        session['username'] = user.username

        return redirect('/secret')  # will modify later
    
    else:
        return render_template('register.html',form=form)
