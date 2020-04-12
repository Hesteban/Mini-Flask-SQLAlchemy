from app import app
from db import db
from models.roles import Role
from models.users import User

with app.app_context():
    #admin = User(username='admin', password='admin', email='admin@test.com')
    #guest = User(username='guest', password='guest', email='guest@test.com')
    admin = Role(role='admin')
    user = Role(role='user')
    db.session.add(admin)
    db.session.add(user)
    db.session.commit()
    print(Role.query.all())
