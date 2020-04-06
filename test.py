from models.users import User
from app import app


with app.app_context():
    users = User.query.all()
    for user in users:
        print("username: {}".format(user.username))
        print("password: {}".format(user.password))
        print("email: {}".format(user.email))