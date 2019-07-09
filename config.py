import os


class Config(object):
    #secret key to thwat Cross site Request Forgery no the app
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'