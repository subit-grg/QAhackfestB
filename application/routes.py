from application import app, db
from application.models import *
from datetime import date, timedelta
from flask import request, redirect, url_for, render_template
from application.forms import *


@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/view-drivers')  
def view_all_driver():
    drivers = Driver.query.all()
    return render_template('view_all.html', entity='Driver', drivers=drivers)

@app.route('/add-driver', methods=['GET', 'POST'])
def add_new_driver():
    form = DriverForm()
    drivers = Driver.query.all()
    form.delievered_by.choices = [(driver.uid, f"{driver.forename} {driver.surname}") for driver in drivers]
    if form.validate_on_submit():
        d_forename = form.forename.data
        d_surname = form.surname.data
        uid = form.location.data
        new_driver = Driver(forname=d_forename, surname=d_surname, location=uid)
        db.session.add(new_driver)
        db.session.commit()
        return redirect(url_for('view_all_drivers'))
   
@app.route('/update-driver/<int:id>', methods=['GET', 'POST'])
def update_driver(id):
    driver_to_update = Driver.query.get(id)
    form = DriverForm()
    drivers = Driver.query.all()
    form.delievered_by.choices = [(driver.uid, f"{driver.forename} {driver.last_name}") for driver in drivers]
    if form.validate_on_submit():
        driver_to_update.forename= form.forename.data
        driver_to_update.surname = form.surname.data
        driver_to_update.location = form.location.data
        db.session.commit()
        return redirect(url_for('view_all_drivers'))
    form.driver.data = driver_to_update.forname
    form.driver.data = driver_to_update.surname
    form.review_date.data = driver_to_update.review_date
    return render_template('review_form.html', form=form)









##############

@app.route('/add-delivery', methods=['GET', 'POST'])
def create_new_delivery():
    form = DeliveryForm()
    drivers = Driver.query.all()
    form.delivered_by.choices = [(driver.did, f"{driver.forename} {driver.surname}") for driver in drivers]
    if form.validate_on_submit():
        customer_name = form.order_name.data
        order_items = form.ordered_items.data
        o_date = form.order_date.data
        d_date = form.delivery_date.data
        did = form.delivered_by.data
        new_delivery = Delivery(order_name=customer_name, ordered_item = order_items, order_date=o_date, delivery_date=d_date, delivered_by=did)
        db.session.add(new_delivery)
        db.session.commit()
        return redirect(url_for('view_all_deliveries'))
    form.due_date.data = date.today()
    errors = form.due_date.errors
    errors += form.delivery_name.errors
    return render_template('delivery_form.html', form = form, errors = errors)

@app.route('/update-delivery/<int:delid>', methods=['GET', 'POST'])
def update_delivery(id):
    delivery_to_update = Delivery.query.get(id)
    form = DeliveryForm()
    drivers = Driver.query.all()
    form.delivered_by.choices = [(driver.did, f"{driver.forename} {driver.surname}") for driver in drivers]
    if form.validate_on_submit():
        delivery_to_update.order_name = form.order_name.data
        delivery_to_update.ordered_items = form.ordered_items.data
        delivery_to_update.order_date = form.order_date.data
        delivery_to_update.delivery_date = form.delivery_date.data
        delivery_to_update.delivered_by = form.delivered_by.data
        db.session.commit()
        return redirect(url_for('view_all_deliveries'))
    form.order_name.data = delivery_to_update.order_name
    form.ordered_items.data = delivery_to_update.ordered_items
    form.order_date.data = delivery_to_update.order_date
    form.delivery_date.data = delivery_to_update.delivery_date
    form.order_date.data = delivery_to_update.order_date
    form.delivered_by = delivery_to_update.order_date
    return render_template('delivery_form.html', form=form)