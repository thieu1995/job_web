from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SECRET_KEY'] = 'NguyeN.thieu.2102'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://thieunv:NguyeN.thieu.2102@127.0.0.1/jobweb'

db = SQLAlchemy(app)

from jobweb import routes
