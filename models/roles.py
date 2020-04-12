from db import db


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50))


    def __repr__(self):
        return '<User %r>' % self.rol