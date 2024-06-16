from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.form
        email = data.get("email")
        password = data.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash("Вход выполнен", category="success")
                return redirect(url_for("views.home"))
            else:
                flash("Неверный email/пароль", category="error")
        else:
            flash("Неверный email/пароль", category="error")
    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))


@auth.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        data = request.form
        email = data.get("email")
        firstName = data.get("firstName")
        password1 = data.get("password1")
        password2 = data.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Пользователь с таким email уже зарегистрирован", category="error")
        elif len(firstName) < 3:
            flash("Введите корректное имя", category="error")
        elif len(password1) < 5:
            flash("Пароль должен содержать от 5 символов", category="error")
        elif password1 != password2:
            flash("Пароли не совпадают", category="error")
        else:
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Регистрация успешна", category="success")
            return redirect(url_for("views.home", user=new_user))

    return render_template("signup.html", user=current_user)

