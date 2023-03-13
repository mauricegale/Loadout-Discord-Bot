from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

db = 'gun_loadout_schema'


class Gun:
    def __init__(self, data):

        self.muzzle = data['muzzle']
        self.gun_id = data['gun_id']
        self.underbarrel = data['underbarrel']
        self.rear_grip = data['rear_grip']
        self.optic = data['optic']
        self.laser = data['laser']
        self.gun_name = data['gun_name']
        self.gun_type = data['gun_type']
        self.magazine = data['magazine']
        self.stock = data['stock']
        self.ammo = data['ammo']
        self.barrel = data['barrel']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_gun(cls, data):
        query = """
            INSERT INTO guns (muzzle, underbarrel, rear_grip, optic,
            laser, gun_name, gun_type, magazine, stock, ammo, barrel, created_at, updated_at)
            VALUES (%(muzzle)s, %(underbarrel)s, %(rear_grip)s, %(optic)s,
            %(laser)s, %(gun_name)s, %(gun_type)s, %(magazine)s, %(stock)s, %(ammo)s, %(barrel)s, now(), now());
        """

        return connectToMySQL(db).query_db(query, data)

    @staticmethod
    def validate_info(data):
        is_valid = True
        nulls = 0

        for attachment in data:
            if data[attachment] == '':
                nulls += 1

        if data['gun_type'] == '':
            flash('Must enter the type of gun', 'type')
            is_valid = False

        if data['gun_name'] == '':
            flash('Must enter the name of gun', 'name_of_gun')
            is_valid = False

        if nulls < 4:
            flash('Must enter at most 5 attachments', 'attachments')
            is_valid = False

        return is_valid
