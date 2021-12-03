from flask import render_template, request, redirect
from flask_login import login_required, login_user, current_user
from flask.helpers import flash, url_for
from flask_login.utils import logout_user
from app import app, db, loginm
from .forms import RegisterForm, LoginForm
from .database import User
from uuid import uuid4

loginm.login_view = "login"

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/signup/', methods=['get', 'post'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        pw = form.passw.data
        user = User(id = str(uuid4().hex)[:10],username = name, email = email)
        user.set_password(pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template("loginreg.html", form = form)

@app.route('/login/', methods=["get", "post"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("accpage"))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.name.data).first()
        if user.check(form.password.data):
            login_user(user, remember=form.rem.data)
            return redirect(url_for("accpage"))
        flash("Неправильное имя и/или пароль")
        return redirect(url_for("login"))
    return render_template("loginreg.html", form = form)  

@app.route('/accpage')
@login_required
def accpage():
    return render_template("accpage.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))    

