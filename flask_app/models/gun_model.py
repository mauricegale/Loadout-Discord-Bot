from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

db = 'gun_loadout_schema'


class Gun:
    def __init__(self, data):
        self.gun_id = data['gun_id']
        self.muzzle = data['muzzle']
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
            INSERT INTO guns (muzzle, underbarrel, rear_grip, optic
            laser, gun_name, gun_type, magazine, stock, ammo, barrel, created_at,updated_at)
            VALUES (%(loadout_id)s, %(muzzle)s, %(underbarrel)s, %(rear_grip)s, %(optic)s
            %(laser)s, %(gun_name)s %(gun_type)s, %(magazine)s, %(stock)s, %(ammo)s, %(barrel)s, now(), now());
        """

        return connectToMySQL(db).query_db(query, data)

    @staticmethod
    def validate_info(data):
        if data['gun_type'] == '':
            flash('Must enter the type of gun', 'report')
            return False

        if data['gun_name'] == '':
            flash('Must Enter the name of gun', 'report')
            return False
