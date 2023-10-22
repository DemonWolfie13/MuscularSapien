#same as views but this is rather for authentication

from flask import Flask, Blueprint, render_template, request, flash

import mysql.connector as s

co=s.connect(host="localhost", user="root", password="ENDr",auth_plugin='mysql_native_password')
cu=co.cursor()

from flask import Blueprint, render_template, request, flash, url_for
#this has the blueprint(urls) of the website and to make it organise

auth=Blueprint('auth',__name__)


@auth.route('/login', methods=["GET","POST"])
def login():
    if request.method=="POST":
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        cu.execute("use members")
        q=("select * from signin where Username='{}'").format(username)
        cu.execute(q)
        t=cu.fetchall()
        q1=("select password from signin where Username='{}' and password='{}'").format(username,password)
        cu.execute(q1)
        v=cu.fetchall()
        q2 = ("select Email from signin where Username='{}' and Email='{}'").format(username,email)
        cu.execute(q2)
        y=cu.fetchall()

        if len(email) < 3:
            flash("Email must be greater than 3 characters", category='error')
        elif len(username) < 5:
            flash("Username must be greater than 5 characters", category='error')
        elif len(password) < 5:
            flash("Password must be greater than 5 characters", category='error')
        elif t != []:
            if v != [] and y != []:
                flash("Logged in successfully", category='success')
                return render_template("home.html")
            else:
                flash("Username or Password entered is wrong. Please retry", category='error')


        elif t==[]:
            flash("No acc with mentioned username found. Please try again or sign up", category='error')
            url_for("auth.login")
    return render_template("login.html")

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=="POST":
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 3:
            flash("Email must be greater than 3 characters", category='error')
        elif len(username) < 5:
            flash("Username must be greater than 5 characters", category='error')
        elif password1 != password2:
            flash("Passwords dont match!!", category='error')
        elif len(password1) < 5:
            flash("Password must be greater than 5 characters", category='error')
        else:
            flash("Account created", category='success')

        cu.execute("use user_info")
        q='insert into signin values("{}","{}","{}")'.format(username,email, password1)
        cu.execute(q)
        co.commit()
        url_for("auth.register")
    return render_template("register.html")
