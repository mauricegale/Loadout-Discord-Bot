from flask import flash

db = 'gun_loadout_schema'


class Gun:
    def __init__(self, data):
        self.loadout_id = data['loadout_id']
        self.creator = data['creator']
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
