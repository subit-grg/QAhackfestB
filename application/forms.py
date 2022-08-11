from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired, ValidationError
from datetime import date



class checkDateInFuture():
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        if field.data is None or field.data < date.today():
            raise ValidationError(self.message)

class DriverForm(FlaskForm):
    forename = StringField('Enter Forename', validators=[DataRequired()])
    surname = StringField('Enter Surname', validators=[DataRequired()])
    location = SelectField('Select your warehouse', validators=[DataRequired()])
    submit = SubmitField('Enter')

class DeliveryForm(FlaskForm):
    order_name = StringField('Customer Name', validators=[DataRequired()])
    ordered_items = TextAreaField('Ordered Items', validators=[DataRequired()])
    destination = StringField('Destination Address', validators=[DataRequired()])
    order_date = DateField('Order Date')
    delivery_date = DateField('Delivery Date', validators=[checkDateInFuture("Please choose a date in the future")])
    delivered_by = SelectField('Delivered By', choices=[])
    submit = SubmitField('Enter')

class LocationForm(FlaskForm):
    warehouse_name = StringField('Warehouse Location', validators=[DataRequired()])