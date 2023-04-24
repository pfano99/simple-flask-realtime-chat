from flask import Blueprint, redirect, url_for, render_template, abort
from flask_login import login_user, logout_user, login_required

from chat import bcrypt, db
from chat.auth.form import LoginForm, SignUpForm
from chat.models import User

auth = Blueprint('Auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
        return redirect(url_for('main.index'))
    return render_template("auth/login.html", form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        _password = bcrypt.generate_password_hash(form.password.data)
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data,
                    password=_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('Main.index'))
    return render_template("auth/signup.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("Main.index"))
