from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import Form, IntegerField, StringField, FloatField, BooleanField, TextAreaField, validators, DecimalField


class Addparts(Form):
    name = StringField('Product Name', [validators.DataRequired()])
    number = StringField('Part Number', [validators.DataRequired()])
    front_oenumber = StringField('Front OE Number', [validators.DataRequired()])
    rear_oenumber = StringField('Rear OE Number', [validators.DataRequired()])
    sub_model = StringField('Sub Model', [validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('In Stock', [validators.DataRequired()])
    colors = StringField('Colors', [validators.DataRequired()])
    location = StringField('Location', [validators.DataRequired()])
    discription = TextAreaField('Discription', [validators.DataRequired()])

    image_1 = FileField('Image 1', validators=[FileAllowed(['jpg','png','gif','jpeg'])])
    image_2 = FileField('Image 2', validators=[FileAllowed(['jpg','png','gif','jpeg'])])
    image_3 = FileField('Image 3', validators=[FileAllowed(['jpg','png','gif','jpeg'])])