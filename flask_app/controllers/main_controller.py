from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.loadout_model import Loadout
from flask_app.models.gun_model import Gun


@app.route("/")
def home():

    return render_template("form.html")


@app.route("/add_loadout", methods=['POST'])
def create_loadout():

    data = {
        **request.form
    }
    Loadout.add_loadout(data)

    return redirect("/")
