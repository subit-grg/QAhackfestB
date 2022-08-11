from application import db



class Driver(db.Model):

    driver_id = db.Column(db.Integer, primary_key = True)

    driver_surname = db.Column(db.String(50), nullable= False)

    driver_forename = db.Column(db.String(50), nullable= False)

    location = db.Column(db.String(50), nullable= False)

    driver_delivery = db.relationship('Delivery', backref='Driver')

    def __str__(self):

        return f"{self.driver_surname}, {self.driver_forename}"



class Order(db.Model):

    order_id = db.Column(db.Integer, primary_key = True)

    delivery_id = db.Column(db.Integer, db.ForeignKey('delivery.delivery_id'), nullable=False)

    order_name = db.Column(db.String(50), nullable= False)

    order_date = db.Column(db.Date, nullable=False)

    ordered_items = db.Column(db.String(50), nullable=False)

    def __str__(self):

        return f"{self.order_date}, {self.ordered_items}"




class Delivery(db.Model):

    delivery_id = db.Column(db.Integer, primary_key = True)

    order_number = db.Column(db.Integer, db.ForeignKey('orders.order_id'), nullable=False)

    delivered_by = db.Column(db.Integer, db.ForeignKey('driver.driver_id'), nullable=False)

    delivery_date = db.Column(db.Date, nullable=False)

    destination = db.Column(db.String(50), nullable=False)

    weight = db.Column(db.Float, nullable=False)

    def __str__(self):

        return f"{self.delivery_date}, {self.destination}, {self.weight}"