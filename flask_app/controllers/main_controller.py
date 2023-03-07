from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.loadout_model import Loadout
from flask_app.models.gun_model import Gun


@app.route("/")
def home():

    return render_template("form.html")


@app.route("/add_loadout", methods=['POST'])
def create_loadout():

    gun_data = {
        'muzzle': request.form['muzzle'],
        'barrel': request.form['barrel'],
        'underbarrel': request.form['underbarrel'],
        'rear_grip': request.form['rear_grip'],
        'optic': request.form['optic'],
        'laser': request.form['laser'],
        'ammo': request.form['ammo'],
        'magazine': request.form['magazine'],
        'created_at': request.form['created_at'],
        'updated_at': request.form['updated_at'],
        'stock': request.form['stock'],
        'gun_name': request.form['gun_name'],
        'gun_type': request.form['gun_type']
    }
    gun = Gun.add_loadout(gun_data)
    gun_id = gun['gun_id']

    loadout_data = {
        'gun_id': request.form['gun_id'],
        'creator': request.form['creator'],
        'created_at': request.form['created_at'],
        'updated_at': request.form['updated_at'],
    }

    Loadout.add_loadout(loadout_data)

    return redirect("/")
