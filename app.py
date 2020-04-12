import os

from flask import Flask, session,redirect, render_template, request, flash, get_flashed_messages
from flask_bootstrap import Bootstrap
from models.users import User
from models.roles import Role
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = "super secret key"


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            form = request.form
            username = form['username']
            password = form['pwd']
            email = form['email']
            rol = form['role']
            if rol not in ['admin', 'user']:
                flash("Role not valid", "danger")
                return render_template('form.html')
            add_user = User(username=username, password=generate_password_hash(password),
                            email=email, role=get_rol_id(rol))
            db.session.add(add_user)
            db.session.commit()
            flash("User inserted succesfully", "success")
            return redirect('/login')
        except:
            flash("User not inserted", "danger")
    return render_template('form.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            form = request.form
            username = form['username']
            password = form['pwd']
            user_login = User.query.filter_by(username=username).first()
            print(user_login)
            if check_password_hash(user_login.password, password):
                session['Login'] = True
                session['username'] = username
                session['admin'] = is_user_adming(user_login)
                print(session['admin'])
                flash("Welcome " + username + " you are logged in", "success")
                return redirect('/users')
            else:
                flash("Error not registered in the app ", "danger")
        except Exception as e:
            print(e)
            flash("User not logged correctly", "danger")

    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/users')
def users():
    if session['admin']:
        user_list = User.query.all()
    else:
        user_list = [User.query.filter_by(username=session['username']).first()]
    print(user_list)
    return render_template('list_users.html', users=user_list)


@app.route('/logout')
def logout():
    session.pop('Login', None)
    session.pop('username', None)
    session.pop('admin', None)

    flash( "You are logged out now", "success")
    return redirect('/')


def get_rol_id(role):
    return Role.query.filter_by(role=role).first()

def is_user_adming(user):
    return user.role.role == 'admin'


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
