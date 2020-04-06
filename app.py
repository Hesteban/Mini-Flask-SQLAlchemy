import os

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from models.users import User
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['pwd']
        email = form['email']
        add_user = User(username=username, password=password, email=email)
        db.session.add(add_user)
        db.session.commit()
    return render_template('form.html')



@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    from db import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
