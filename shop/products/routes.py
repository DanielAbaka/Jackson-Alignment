from flask import render_template,session, request,redirect,url_for,flash, current_app
from shop import app,db,photos
from .models import Brand, Year, Make, Engine, Model, Addpart
from .forms import Addparts
import secrets, os


@app.route('/')
def home():
    parts = Addpart.query.filter(Addpart.stock > 0)
    brands = Brand.query.join(Addpart, (Brand.id == Addpart.brand_id)).all()
    return render_template('products/index.html', parts=parts, brands=brands)


@app.route('/brand/<int:id>')
def get_brand(id):
    brand = Addpart.query.filter_by(brand_id=id)
    brands = Brand.query.join(Addpart, (Brand.id == Addpart.brand_id)).all()
    return render_template('products/index.html', brand=brand, brands=brands)



@app.route('/addbrand', methods=['GET','POST'])
def addbrand():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    if request.method=="POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The Brand {getbrand} was added to your database','success')
        db.session.commit()
        return redirect(url_for('brands'))

    return render_template('products/addbrand.html', brands='brands')


@app.route('/updatebrand/<int:id>', methods=['GET','POST'])
def updatebrand(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method =="POST":
        updatebrand.name = brand
        flash(f'Your brand has been updated','success')
        db.session.commit()
        return redirect(url_for('brands'))
    return render_template('products/updatebrand.html', title='Update Brand Page', updatebrand=updatebrand)


@app.route('/deletebrand/<int:id>', methods=['GET','POST'])
def deletebrand(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    brand = Brand.query.get_or_404(id)
    if request.method =="POST":
        db.session.delete(brand)
        db.session.commit()
        flash(f'The brand {brand.name} has been deleted from your database','success')
        return redirect(url_for('brands'))
    flash(f'The brand {brand.name} cant not be deleted','warning')
    return redirect(url_for('brands'))



@app.route('/addyear', methods=['GET','POST'])
def addyear():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    if request.method=="POST":
        getyear = request.form.get('year')
        year = Year(name=getyear)
        db.session.add(year)
        flash(f'The Year {getyear} was added to your database','success')
        db.session.commit()
        return redirect(url_for('years'))

    return render_template('products/addyear.html', years='years')


@app.route('/updateyear/<int:id>', methods=['GET','POST'])
def updateyear(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    updateyear = Year.query.get_or_404(id)
    year = request.form.get('year')
    if request.method =="POST":
        updateyear.name = year
        flash(f'Your year has been updated','success')
        db.session.commit()
        return redirect(url_for('years'))
    return render_template('products/updateyear.html', title='Update Year Page', updateyear=updateyear)



@app.route('/deleteyear/<int:id>', methods=['GET','POST'])
def deleteyear(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    year = Year.query.get_or_404(id)
    if request.method =="POST":
        db.session.delete(year)
        db.session.commit()
        flash(f'The year {year.name} has been deleted from your database','success')
        return redirect(url_for('years'))
    flash(f'The year {year.name} cant not be deleted','warning')
    return redirect(url_for('years'))



@app.route('/addmake', methods=['GET','POST'])
def addmake():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    if request.method=="POST":
        getmake = request.form.get('make')
        make = Make(name=getmake)
        db.session.add(make)
        flash(f'The Make {getmake} was added to your database','success')
        db.session.commit()
        return redirect(url_for('makes'))

    return render_template('products/addmake.html', makes='makes')



@app.route('/updatemake/<int:id>', methods=['GET','POST'])
def updatemake(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    updatemake = Make.query.get_or_404(id)
    make = request.form.get('make')
    if request.method =="POST":
        updatemake.name = make
        flash(f'Your make has been updated','success')
        db.session.commit()
        return redirect(url_for('makes'))
    return render_template('products/updatemake.html', title='Update Make Page', updatemake=updatemake)


@app.route('/deletemake/<int:id>', methods=['GET','POST'])
def deletemake(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    make = Make.query.get_or_404(id)
    if request.method =="POST":
        db.session.delete(make)
        db.session.commit()
        flash(f'The make {make.name} has been deleted from your database','success')
        return redirect(url_for('makes'))
    flash(f'The make {make.name} cant not be deleted','warning')
    return redirect(url_for('makes'))



@app.route('/addmodel', methods=['GET','POST'])
def addmodel():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    if request.method=="POST":
        getmodel = request.form.get('model')
        model = Model(name=getmodel)
        db.session.add(model)
        flash(f'The Model {getmodel} was added to your database','success')
        db.session.commit()
        return redirect(url_for('models'))

    return render_template('products/addmodel.html', models='models')


@app.route('/updatemodel/<int:id>', methods=['GET','POST'])
def updatemodel(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    updatemodel = Model.query.get_or_404(id)
    model = request.form.get('model')
    if request.method =="POST":
        updatemodel.name = model
        flash(f'Your model has been updated','success')
        db.session.commit()
        return redirect(url_for('models'))
    return render_template('products/updatemodel.html', title='Update Model Page', updatemodel=updatemodel)


@app.route('/deletemodel/<int:id>', methods=['GET','POST'])
def deletemodel(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    model = Model.query.get_or_404(id)
    if request.method =="POST":
        db.session.delete(model)
        db.session.commit()
        flash(f'The model {model.name} has been deleted from your database','success')
        return redirect(url_for('models'))
    flash(f'The model {model.name} cant not be deleted','warning')
    return redirect(url_for('models'))


@app.route('/addengine', methods=['GET','POST'])
def addengine():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    if request.method=="POST":
        getengine = request.form.get('engine')
        engine = Engine(name=getengine)
        db.session.add(engine)
        flash(f'The Engine {getengine} was added to your database','success')
        db.session.commit()
        return redirect(url_for('engines'))

    return render_template('products/addengine.html', engines='engines')


@app.route('/updateengine/<int:id>', methods=['GET','POST'])
def updateengine(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    updateengine = Engine.query.get_or_404(id)
    engine = request.form.get('engine')
    if request.method =="POST":
        updateengine.name = engine
        flash(f'Your engine has been updated','success')
        db.session.commit()
        return redirect(url_for('engines'))
    return render_template('products/updateengine.html', title='Update Engine Page', updateengine=updateengine)


@app.route('/deleteengine/<int:id>', methods=['GET','POST'])
def deleteengine(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    engine = Engine.query.get_or_404(id)
    if request.method =="POST":
        db.session.delete(engine)
        db.session.commit()
        flash(f'The engine {engine.name} has been deleted from your database','success')
        return redirect(url_for('engines'))
    flash(f'The engine {engine.name} cant not be deleted','warning')
    return redirect(url_for('engines'))



@app.route('/addpart', methods=['POST', 'GET'])
def addpart():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    brands = Brand.query.all()
    makes = Make.query.all()
    years = Year.query.all()
    engines = Engine.query.all()
    models = Model.query.all()
    form = Addparts(request.form)
    if request.method =="POST":
        name = form.name.data
        number = form.number.data
        front_oenumber = form.front_oenumber.data
        rear_oenumber = form.rear_oenumber.data
        sub_model = form.sub_model.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        location = form.location.data
        desc = form.discription.data
        brand = request.form.get('brand')
        make = request.form.get('make')
        model = request.form.get('model')
        year = request.form.get('year')
        engine = request.form.get('engine')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        addpart = Addpart(name=name, number=number, front_oenumber=front_oenumber, rear_oenumber=rear_oenumber, sub_model=sub_model, price=price, discount=discount, stock=stock, colors=colors, location=location, desc=desc,
         brand_id=brand, make_id=make, model_id=model, year_id=year, engine_id=engine, 
        image_1=image_1, image_2=image_2, image_3=image_3)
        db.session.add(addpart)
        flash(f'The product {name} was added in database','success')
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('products/addpart.html', title='Add Part Page', form=form, brands=brands, makes=makes, years=years, 
    engines=engines, models=models)



@app.route('/updatepart/<int:id>', methods=['GET','POST'])
def updatepart(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    brands = Brand.query.all()
    makes = Make.query.all()
    years = Year.query.all()
    engines = Engine.query.all()
    models = Model.query.all()
    part = Addpart.query.get_or_404(id)
    brand = request.form.get('brand')
    make = request.form.get('make')
    year = request.form.get('year')
    engine = request.form.get('engine')
    model = request.form.get('model')
    form = Addparts(request.form)
    if request.method =="POST":
        part.name = form.name.data
        part.number = form.number.data
        part.front_oenumber = form.front_oenumber.data
        part.rear_oenumber = form.rear_oenumber.data
        part.sub_model = form.sub_model.data
        part.brand_id = brand
        part.make_id = make
        part.year_id = year
        part.model_id = model
        part.engine_id = engine
        part.price = form.price.data
        part.discount = form.discount.data
        part.colors = form.colors.data
        part.location = form.location.data
        part.desc = form.discription.data
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + part.image_1))
                part.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                part.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")

        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + part.image_2))
                part.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            except:
                part.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        
        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + part.image_3))
                part.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
            except:
                part.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        db.session.commit()
        flash(f'Your Product has been updated','success')
        return redirect(url_for('admin'))

    form.name.data = part.name
    form.number.data = part.number
    form.front_oenumber.data = part.front_oenumber
    form.rear_oenumber.data = part.rear_oenumber
    form.sub_model.data = part.sub_model
    form.price.data = part.price
    form.discount.data = part.discount
    form.stock.data = part.stock
    form.colors.data = part.colors
    form.location.data = part.location
    form.discription.data = part.desc
    return render_template('products/updatepart.html', form=form, brands=brands, makes=makes, years=years, 
    engines=engines, models=models, part=part)



@app.route('/deletepart/<int:id>', methods=['POST'])
def deletepart(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    part = Addpart.query.get_or_404(id)
    if request.method == "POST":
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + part.image_1))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + part.image_2))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + part.image_3))
        except Exception as e:
            print(e)
        db.session.delete(part)
        db.session.commit()
        flash(f'The product {part.name} was deleted from your database','success')
        return redirect(url_for('admin'))
    flash(f'Cant delete part','danger')
    return redirect(url_for('admin'))