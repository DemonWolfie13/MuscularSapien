from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY']= 'qwerty'


from website import routes
