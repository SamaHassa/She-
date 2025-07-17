from flask import Flask, render_template, request, redirect, url_for,flash
import os
from models import db # import db instance and models
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///she.db'
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False


db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
  return render_template("home.html")










if __name__ == '__main__':
    app.run(debug=True)