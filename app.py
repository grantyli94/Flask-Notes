"""Flask app for Users"""

from models import User, db, connect_db
from flask import Flask, request, jsonify, render_template, redirect, session, flash
from forms import AddUserForm, LoginForm
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

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

########################### User Login/Logout #################################
@app.route('/register', methods=['POST',"GET"])
def show_register_form():
    """Shows registration page and handles user creation"""
    
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

        return redirect(f'/users/{user.username}')
    
    else:
        return render_template('register.html',form=form)

@app.route('/login', methods=['POST','GET'])
def show_login_form():
    """Produce login form or handle login"""

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        pwd = form.password.data

        user = User.authenticate(username, pwd)
        
        if user:
            session['username'] = user.username
            return redirect(f'/users/{user.username}')
        else:
            form.username.errors = ['Invalid username/password']
    
    return render_template('login.html', form=form)

@app.route('/logout')
def log_user_out():
    """Logs user out."""

    session.pop('username', None)
    return redirect('/')

########################### User Info ######################################

@app.route('/users/<username>')
def show_user_info(username):
    """Shows user info for logged in user"""

    if "username" in session:
        user = User.query.get(username)
        return render_template('user_info.html', user=user)
    else:
        flash("You must be logged in to view!")
        return redirect('/')

@app.route('/users/<username>/delete', methods=["POST"])
def delete_user(username):

    user = User.query.get_or_404(username)
    db.session.delete(user)
    db.session.commit()
    
    
