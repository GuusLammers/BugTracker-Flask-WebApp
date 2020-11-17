from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)


# renders the login page
@auth.route('/login')
def login():
    return render_template('login.html')


# logs user in if correct information is provided
@auth.route('/login', methods=['POST'])
def login_post():
    # read user input information from form
    email = request.form['email']
    password = request.form['password']

    # query database for user using email
    user = User.query.filter_by(email=email).first()

    # if email didn't exist in data base flash message
    if not user:
        flash('Please check your log in details and try again.')
        return redirect(url_for('auth.login'))

    # if email exists but password is incorrect flash message
    if not check_password_hash(user.password, password):
        flash('Please check your log in details and try again.')
        return redirect(url_for('auth.login'))

    # if email exists and password is correct log user in
    login_user(user)

    # redirect to active projects page
    return redirect(url_for('main.projects_active'))


# renders the signup page
@auth.route('/signup')
def signup():
    return render_template('register.html')


# user signup
@auth.route('/signup', methods=['POST'])
def signup_post():
    # read user input information from form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']

    # check to see if email already exists within database
    user = User.query.filter_by(email=email).first()

    # if account with submitted email already exists flash message
    if user:
        flash('Email address already exists in our system.')
        return redirect(url_for('auth.signup'))

    # create new user
    new_user = User(email=email, password=generate_password_hash(password, method='sha256'), first_name=first_name, last_name=last_name)
    db.session.add(new_user)
    db.session.commit()

    # redirect to login page
    return redirect(url_for('auth.login'))


# user logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
