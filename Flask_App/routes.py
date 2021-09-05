from Flask_App import app, db, bcrypt
from flask import render_template, url_for, flash, redirect
from Flask_App.forms import RegisterForm, LoginForm
from Flask_App.db_model import User, Post

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


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
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


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/editor')
def editor():
    return render_template('blog_editor.html')
