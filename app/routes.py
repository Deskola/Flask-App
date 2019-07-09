from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dennis', 'email':'denis@gmail.com'}
    post = [
        {
            'author':{'username':'Denis'},
            'body':'This is a nice day mate'
        },
        {
            'author':{'username':'Tony'},
            'body':'This is a nice day in Kenya @Denis'
        }
    ]
    return render_template('index.html',  user=user, post=post)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)