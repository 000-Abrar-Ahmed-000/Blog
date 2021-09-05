from flask import Flask
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '684fjfhj648468fghfgh'
app.config['CKEDITOR_PKG_TYPE'] = 'standard'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
ckeditor = CKEditor(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from Flask_App import routes
