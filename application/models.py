from application import db



class Driver(db.Model):
    driver_id = db.Column(db.Integer, primary_key = True)
    driver_surname = db.Column(db.String(50), nullable= False)
    driver_forename = db.Column(db.String(50), nullable= False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.location_id'), nullable=False)
    delivery_id = db.Column(db.Integer, db.ForeignKey('delivery.delivery_id'), nullable=False)
    driver_delivery = db.relationship('Delivery', backref='Driver')
    driver_location = db.relationship('Location', backref='Driver')
    def __str__(self):
        return f"{self.driver_surname}, {self.driver_forename}"

class Location(db.Model):
    location_id = db.Column(db.Integer, primary_key = True)
    delivery_id = db.Column(db.Integer, db.ForeignKey('delivery.delivery_id'), nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.driver_id'), nullable=False)
    warehouse_name = db.Column(db.String(50), nullable= False)
    distance = db.Column(db.String(50), nullable= False)
    def __str__(self):
        return f"{self.warehouse_name}, {self._distance_items}"
    
class Delivery(db.Model):
    delivery_id = db.Column(db.Integer, primary_key = True)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.driver_id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.location_id'), nullable=False)
    delivery_date = db.Column(db.Date, nullable=False)
    destination = db.Column(db.String(50), nullable=False)
    order_date = db.Column(db.Date, nullable=False)
    ordered_items=db.Column(db.String(50), nullable=False)
    def __str__(self):
        return f"{self.delivery_date}, {self.destination}, {self.order_date}, {self.ordered_items}"