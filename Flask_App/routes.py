from Flask_App import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from Flask_App.forms import RegisterForm, LoginForm
from Flask_App.db_model import User, Post
from flask_login import login_user, current_user, logout_user, login_required

# dummy posts
blog_posts = [
    {'header': "Header 1",
     'title': "Article Title 1",
     'text': "This is a little summary for Article 1"
     },
    {'header': "Header 2",
     'title': "Article Title 2",
     'text': "This is a little summary for Article 2"
     },
    {'header': "Header 3",
     'title': "Article Title 3",
     'text': "This is a little summary for Article 3"
     },
    {'header': "Header 4",
     'title': "Article Title 4",
     'text': "This is a little summary for Article 4"
     },
    {'header': "Header 2",
     'title': "Article Title 2",
     'text': "This is a little summary for Article 2"
     },
    {'header': "Header 3",
     'title': "Article Title 3",
     'text': "This is a little summary for Article 3"
     },
    {'header': "Header 4",
     'title': "Article Title 4",
     'text': "This is a little summary for Article 4"
     }
]


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/posts')
def posts():
    return render_template("posts.html", posts=blog_posts)


@app.route('/register', methods=['POST', 'GET'])
def register():
    #   checking if user already logged in
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    #   initiating  reg_form class
    #   reg form contains input data --> email, username, password .. see forms.py
    reg_form = RegisterForm()
    if reg_form.validate_on_submit():
        #   hashing password before pushing it into Database
        hashed_password = bcrypt.generate_password_hash(reg_form.password.data).decode('UTF-8')
        user = User(
            username=reg_form.username.data,
            email=reg_form.email.data,
            password=hashed_password
        )
        #   adding user and closing DB session
        db.session.add(user)
        db.session.commit()
        flash(f'account created {reg_form.username.data}', 'success')
        #   redirect to login page after registration successful
        return redirect(url_for('login'))
    # form = reg_form allows form to be accessed from html pages - register.html
    return render_template('registration.html',
                           title='Register',
                           form=reg_form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        #   checking if user email actually exists
        user = User.query.filter_by(email=login_form.email.data).first()
        #   check if user has output and hashed pass matches login pass input
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user, remember=login_form.remember.data)
            #   if user has been redirected from user-only page to login
            #   next_page stores the url from which user was redirected
            #   if login success user is redirected to the initial page
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                flash('Login Successful. Welcome', 'success')
                return redirect(url_for('home'))
        #   if login creds are incorrect- fail message
        else:
            flash('Incorrect Credentials', 'danger')
    return render_template('login.html',
                           title='User Login',
                           form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    # logout option only visible to logged in users - see navbar.html
    return redirect(url_for('home'))


@app.route('/profile', methods=['POST', 'GET'])
#   decorator below requires user to login to access page
@login_required
def profile():
    pass


@app.route('/dashboard', methods=['POST', 'GET'])
@login_required
def dashboard():
    return render_template('dashboard.html',
                           title='Dashboard')


@app.route('/editor')
@login_required
def editor():
    pass


@app.route('/viewer')
def viewer():
    pass


