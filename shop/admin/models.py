from shop import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=True, nullable=False)
    lastname = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=False, nullable=False)
    phone = db.Column(db.String(15), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    profile = db.Column(db.String(180), unique=True, nullable=False, default='profile.jpg')

    def __repr__(self):
        return '<User %r>' % self.username



db.create_all()