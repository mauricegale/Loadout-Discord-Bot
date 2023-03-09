from config.mysqlconnection import connectToMySQL
db = 'gun_loadout_schema'


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return "Yoooo"

    if p_message == "!help":
        return "`This is the help message`"

    if p_message[0] == "!":
        loadouts = get_loadout_by_gun_name(p_message[1:])
        loadout_info = ''
        for loadout in loadouts:
            for info in loadout:
                if loadout[info] != "":
                    loadout_info += f"{info}: {loadout[info]}\n"
            loadout_info += "\n"

        return loadout_info


def get_loadout_by_gun_name(name):
    query = f"""
            SELECT creator, gun_name, barrel, magazine, stock, rear_grip, underbarrel, muzzle, ammo, optic, laser FROM guns 
            JOIN loadouts
            ON loadouts.gun_id = guns.gun_id
            WHERE gun_name LIKE "%{name}%";
        """

    results = connectToMySQL(db).query_db(query)
    loadouts = []

    for one_loadout in results:
        loadouts.append(one_loadout)

    return loadouts
