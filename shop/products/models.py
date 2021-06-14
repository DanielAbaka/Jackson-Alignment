from shop import db
from datetime import datetime

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)


class Year(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)


class Make(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)


class Engine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    

class Addpart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    number = db.Column(db.String(80), nullable=False)
    front_oenumber = db.Column(db.String(80), nullable=False)
    rear_oenumber = db.Column(db.String(80), nullable=False)
    sub_model = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, nullable=False)
    colors = db.Column(db.Text, nullable=False)
    location = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),nullable=False)
    brand = db.relationship('Brand',backref=db.backref('brands', lazy=True))

    make_id = db.Column(db.Integer, db.ForeignKey('make.id'),nullable=False)
    make = db.relationship('Make',backref=db.backref('makes', lazy=True))

    model_id = db.Column(db.Integer, db.ForeignKey('model.id'),nullable=False)
    model = db.relationship('Model',backref=db.backref('models', lazy=True))

    year_id = db.Column(db.Integer, db.ForeignKey('year.id'),nullable=False)
    year = db.relationship('Year',backref=db.backref('years', lazy=True))

    engine_id = db.Column(db.Integer, db.ForeignKey('engine.id'),nullable=False)
    engine = db.relationship('Engine',backref=db.backref('engines', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')


    def __repr__(self):
        return '<Addpart %r>' % self.name



db.create_all()