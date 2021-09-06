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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    reg_form = RegisterForm()
    if reg_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(reg_form.password.data).decode('UTF-8')
        user = User(
            username=reg_form.username.data,
            email=reg_form.email.data,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash(f'account created {reg_form.username.data}', 'success')
        return redirect(url_for('login'))
    return render_template('registration.html',
                           title='Register',
                           form=reg_form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user, remember=login_form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                flash('Login Successful. Welcome', 'success')
                return redirect(url_for('home'))

        else:
            flash('Incorrect Credentials', 'danger')
    return render_template('login.html',
                           title='User Login',
                           form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/profile', methods=['POST', 'GET'])
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


