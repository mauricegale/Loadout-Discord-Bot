from flask_app import app
from flask import render_template, redirect, request, session, flash


@app.route("/")
def home():

    return render_template("form.html")
