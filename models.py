from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "users"
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80))
    phonenumber = db.Column(db.String(30))
    password = db.Column(db.String(100), nullable=False)

    orders = db.relationship('Orders', backref='user', lazy=True)
    checkouts = db.relationship('Checkout', backref='user', lazy=True)

class Admin(db.Model):
    __tablename__ = "admin"
    aid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    products = db.relationship("Product", backref='admin', lazy=True)

class Product(db.Model):
    __tablename__ = "product"
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    price = db.Column(db.Integer)
    img = db.Column(db.String(100))
    category = db.Column(db.String(50))
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.aid'))

    order_items = db.relationship('OrderItem', backref='product', lazy=True)

class Checkout(db.Model):
    __tablename__ = "checkout"
    cid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey("users.uid"))

    orders = db.relationship("Orders", backref='checkout', lazy=True)

class Orders(db.Model):
    __tablename__ = "orders"
    oid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.uid'))
    checkoutid = db.Column(db.Integer, db.ForeignKey('checkout.cid'))
    total_price = db.Column(db.Integer)

    order_items = db.relationship("OrderItem", backref='order', lazy=True)

class OrderItem(db.Model):
    __tablename__ = "orderitem"
    orderid = db.Column(db.Integer, db.ForeignKey('orders.oid'), primary_key=True)
    productid = db.Column(db.Integer, db.ForeignKey('product.pid'), primary_key=True)
    quantity = db.Column(db.Integer)


