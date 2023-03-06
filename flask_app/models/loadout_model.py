from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'gun_loadout_schema'


class Loadout:
    def __init__(self, data):
        self.id = data['id']
        self.creator = data['creator']
        self.gun_id = data['gun_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
