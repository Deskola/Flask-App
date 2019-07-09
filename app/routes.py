from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dennis', 'email':'denis@gmail.com'}
    post = [
        {
            'author':'Denis',
            'body':'This is a nice day mate'
        },
        {
            'author':'Tony',
            'body':'This is a nice day in Kenya @Denis'
        }
    ]
    return render_template('index.html',  user=user, post=post)