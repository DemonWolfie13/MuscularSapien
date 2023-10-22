from website import app
from flask import render_template, url_for, redirect, flash
from website.forms import RegistrationForm, LoginForm

@app.route("/")
def homepage():
    return render_template('homepage.html', title = 'Home Page' )

@app.route("/about")
def about():
    return render_template('about.html', title = 'About Page' )

@app.route("/account")
def account():
    return render_template('account.html', title = 'Account' )

'''
@app.route('/register', methods=['POST','GET'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created successfully', category='success')
        return redirect(url_for('homepage'))
    return render_template('register.html', title = 'Register', form=form)





@app.route('/login', methods=['POST','GET'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='user1@gmail.com' and form.password.data == 'password':
            flash(f'Login successful', category='success')
            return redirect(url_for("account"))
        else:
            flash(f'Login failed', category='danger')
    
    return render_template('login.html', title='Login', form=form)

    '''
