#!/usr/bin/env python3

from flask import Flask, redirect, render_template, url_for
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")
app.secret_key = os.getenv("secret_key")

mysql = MySQL(app)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(port=5000)
