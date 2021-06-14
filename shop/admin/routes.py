from flask import render_template, session, request, redirect, url_for, flash

from shop import app, db, bcrypt
from .forms import RegistrationForm, LoginForm
from .models import User
from shop.products.models import Addpart, Brand, Make, Model, Engine, Year
import os 


@app.route('/admin')
def admin():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    parts = Addpart.query.all()
    return render_template('admin/index.html', title='Admin Page', parts=parts)


@app.route('/brands')
def brands():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    brands = Brand.query.order_by(Brand.id.desc()).all()
    return render_template('admin/brand.html', title='brands',brands=brands)


@app.route('/makes')
def makes():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    makes = Make.query.order_by(Make.id.desc()).all()
    return render_template('admin/make.html', title='makes',makes=makes)


@app.route('/models')
def models():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    models = Model.query.order_by(Model.id.desc()).all()
    return render_template('admin/model.html', title='models',models=models)


@app.route('/engines')
def engines():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    engines = Engine.query.order_by(Engine.id.desc()).all()
    return render_template('admin/engine.html', title='engines',engines=engines)


@app.route('/years')
def years():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    years = Year.query.order_by(Year.id.desc()).all()
    return render_template('admin/year.html', title='years',years=years)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(firstname=form.firstname.data,lastname=form.lastname.data,
        username=form.username.data,phone=form.phone.data,email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.username.data} Thank you for registering', 'success')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title="Registration Page")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method =="POST" and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Welcome {form.email.data} You are logedin now ','success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash(f'Wrong Password please try again', 'danger')
            
    return render_template('admin/login.html', form=form, title='Login Page')