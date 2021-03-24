from . import db

class Property(db.Model):
    # Uncomment the line below if you want to set your own table name
    __tablename__ = "property_profiles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(250))
    rooms = db.Column(db.Integer)
    bath = db.Column(db.Numeric)
    price = db.Column(db.Numeric)
    propType = db.Column(db.String(80))
    location = db.Column(db.String(100))
    photo = db.Column(db.String(100))

    def __init__(self, title,description,rooms,bath,price,propType,location,photo):
        self.title = title
        self.description = description
        self.rooms = rooms
        self.bath = bath
        self.price = price
        self.propType = propType
        self.location = location
        self.photo = photo

    def __repr__(self):
        return '<Property %r>' % self.title