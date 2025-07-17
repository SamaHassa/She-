from app import db
from models import Users, Admin, Product, Orders, Checkout, Orderitem
from werkzeug.security import generate_password_hash 


# -------- Dummy Users --------
user1 = Users(username="sama", email="sama@example.com", address="Giza", phonenumber="01111111111", password=generate_password_hash("123456"))
user2 = Users(username="ali", email="ali@example.com", address="Cairo", phonenumber="01222222222", password=generate_password_hash("password"))

# -------- Dummy Admins --------
admin1 = Admin(username="admin1", email="admin1@example.com", password=generate_password_hash("adminpass"))

# -------- Dummy Products --------
product1 = Product(name="Lipstick", price=150, img="lipstick.jpg", category="Makeup", admin=admin1)
product2 = Product(name="Shampoo", price=70, img="shampoo.jpg", category="Hair", admin=admin1)
product3 = Product(name="Perfume", price=300, img="perfume.jpg", category="Fragrance", admin=admin1)

# -------- Dummy Checkouts --------
checkout1 = Checkout(user=user1)
checkout2 = Checkout(user=user2)

# -------- Dummy Orders --------
order1 = Orders(proid=product1.pid, checkout=checkout1, user=user1, total_price=150)
order2 = Orders(proid=product2.pid, checkout=checkout2, user=user2, total_price=70)

# -------- Dummy Order Items (M:N) --------
order_item1 = Orderitem(order=order1, product=product1, quantity=2)
order_item2 = Orderitem(order=order1, product=product3, quantity=1)
order_item3 = Orderitem(order=order2, product=product2, quantity=3)


db.session.add_all([user1, user2, admin1, product1, product2, product3, checkout1, checkout2, order1, order2, order_item1, order_item2, order_item3])
db.session.commit() 