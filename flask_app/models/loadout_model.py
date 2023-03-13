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
        self.game_mode = data['game_mode']

    @staticmethod
    def validate_info(data):
        is_valid = True

        if data['game_mode'] == '':
            flash('Must enter game mode loadout is meant for', 'type')
            is_valid = False

        if data['creator'] == '':
            flash('Must enter creator or source of loadout', 'creator')
            is_valid = False

        return is_valid

    @classmethod
    def add_loadout(cls, data):
        query = """
            INSERT INTO loadouts (game_mode, creator, gun_id, created_at, updated_at)
            VALUES (%(game_mode)s, %(creator)s, %(gun_id)s, now(), now());
        """

        return connectToMySQL(db).query_db(query, data)

    # @classmethod
    # def add_multiple_loadouts(cls, creator, game_mode):
    #     loadout_data = {
    #         "gun_id": attachment_dict[gun_id],
    #         "creator": creator,
    #         "game_mode": game_mode
    #     }

    #     file = open("flask_app/weapon_data/text_files/loadouts.txt", "r")
    #     temp = file.readlines()

    #     loadouts = [line.strip() for line in temp]
    #     count = 0
    #     one_dict = {}

    #     for i in range(len(loadouts)):
    #         if loadouts[i] == "":
    #             one_dict.clear()
    #             count = 0
    #             continue
    #         if count % 2 == 0:
    #             one_dict[loadouts[i]] = ""
    #         else:
    #             one_dict[loadouts[i - 1]] = loadouts[i]
    #         count += 1
    #     print(loadout_dicts)
