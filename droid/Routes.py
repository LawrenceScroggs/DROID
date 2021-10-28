from droid.Models import Admins, Approval
from flask import render_template, url_for, flash, redirect
from droid.Forms import registration_form, login_form
from droid import app

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
@app.route('/home')
def home():
    """Renders a sample page."""
    return render_template('home.html')
@app.route('/register', methods=['GET','POST'])
def register():
    form = registration_form()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)
@app.route('/login', methods=['GET','POST'])
def login():
    form = login_form()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have successfully logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful please check username and password','danger')


    return render_template('login.html',title='Login', form=form)


