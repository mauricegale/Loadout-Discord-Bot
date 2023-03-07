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

    @classmethod
    def add_loadout(cls, data):
        query = """
            INSERT INTO loadouts (creator, gun_id, created_at, updated_at)
            VALUES (%(creator)s, %(gun_id)s, %(release_date)s, now(), now());
        """

        return connectToMySQL(db).query_db(query, data)
