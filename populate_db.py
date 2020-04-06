from models.users import User
from app import app
from db import db


#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
with app.app_context():
    admin = User(username='admin', password='admin', email='admin@test.com')
    guest = User(username='guest', password='guest', email='guest@test.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    print(User.query.all())
