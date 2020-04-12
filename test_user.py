from app import app
from models.roles import Role
from models.users import User

with app.app_context():
    test = Role.query.filter_by(role='admin').first()
    print("-- {}".format(test.id))
    roles = Role.query.all()
    for rol in roles:
        print(rol.id)
        print(rol.role)

    users = User.query.all()
    for user in users:
        print("username: {}".format(user.username))
        print("password: {}".format(user.password))
        print("email: {}".format(user.email))
        print("rol: {}".format(user.role))

