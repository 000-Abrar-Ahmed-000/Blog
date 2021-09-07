from flask import Flask
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '684fjfhj648468fghfgh'
app.config['CKEDITOR_PKG_TYPE'] = 'standard'

#   database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#   for editing blog posts
ckeditor = CKEditor(app)

#   database for storing user-info and posts
db = SQLAlchemy(app)

#   for password encryption
bcrypt = Bcrypt(app)

# managing logged in users
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


# this export must stay at the bottom
#   moving it up throws circular logic error
from Flask_App import routes
