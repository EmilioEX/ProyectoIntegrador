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

@app.route("/actualizarPaciente")
def actualizarPaciente():
    return render_template("ActualizarPaciente.html")

@app.route("/historialGeneral")
def historialGeneral():
    return render_template("HistorialGeneral.html")

@app.route("/historialUsuario")
def historialUsuario():
    return render_template("HistorialUsuario.html")

@app.route("/historialUsuario/admin")
def historialUsuarioAdmin():
    return render_template("HistorialUsuarioAdmin.html")

@app.route("/home/admin")
def homeAdmin():
    return render_template("HomeAdmin.html")

@app.route("/home/medico")
def homeMedico():
    return render_template("HomeMedico.html")

@app.route("/home/usuario")
def homeUsuario():
    return render_template("HomeUsuario.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/modificarDatos/admin")
def modificarDatosAdmin():
    return render_template("ModificarDatosAdmin.html")

@app.route("/modificarDatos/medico")
def modificarDatosMedico():
    return render_template("ModificarDatosMedico.html")

@app.route("/modificarDatos/usuario")
def modificarDatosUsuario():
    return render_template("ModificarDatosUsuario.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/registrarCita/altruista")
def registrarCitaAltruista():
    return render_template("RegistrarCitaAltruista.html")

@app.route("/registrarCita/familiar")
def registrarCitaFamiliar():
    return render_template("RegistrarCitaFamiliar.html")

@app.route("/verCitas/medico")
def verCitasMedico():
    return render_template("VerCitasMedico.html")

if __name__ == "__main__":
    app.run(port=5000)
