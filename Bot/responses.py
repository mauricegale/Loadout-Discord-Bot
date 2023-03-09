from config.mysqlconnection import connectToMySQL
db = 'gun_loadout_schema'


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return "Yoooo"

    if p_message == "!help":
        return "`This is the help message`"

    if "!all loadouts" in p_message:
        return all_loadouts()

    if "!all" in p_message:
        return all_guns()

    if p_message[0] == "!" and ' ' not in p_message:
        return get_loadout_by_gun_name(p_message[1:])

    if "!type" in p_message and ' ' in p_message:
        return get_loadout_with_gun_type(p_message[p_message.index(" ") + 1:])


def convert_to_message(loadouts):
    loadout_info = ''

    for loadout in loadouts:
        for info in loadout:
            if loadout[info] != "":
                loadout_info += f"{info}: {loadout[info]}\n"
        loadout_info += "\n"

    return loadout_info


def convert_all_guns_to_message(loadouts):
    loadout_info = ''

    for loadout in loadouts:
        for info in loadout:
            if loadout[info] != "":
                loadout_info += f"{loadout[info]}\n"

    return loadout_info


def all_loadouts():
    query = f"""
        SELECT creator, gun_name, barrel, magazine, stock, rear_grip, underbarrel, muzzle, ammo, optic, laser FROM guns
        JOIN loadouts
        ON loadouts.gun_id = guns.gun_id;
    """

    results = connectToMySQL(db).query_db(query)
    loadouts = []

    for one_loadout in results:
        loadouts.append(one_loadout)

    return convert_to_message(loadouts)


def all_guns():
    query = f"""
        SELECT gun_name FROM guns
        JOIN loadouts
        ON loadouts.gun_id = guns.gun_id;
    """

    results = connectToMySQL(db).query_db(query)
    loadouts = []

    for one_loadout in results:
        loadouts.append(one_loadout)

    return convert_all_guns_to_message(loadouts)


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

    if not loadouts:
        return "No there are currently no loadouts associated with this gun"

    return convert_to_message(loadouts)


def get_loadout_with_gun_type(gun_type):
    query = f"""
        SELECT creator, gun_name, barrel, magazine, stock, rear_grip, underbarrel, muzzle, ammo, optic, laser FROM guns 
        JOIN loadouts
        ON loadouts.gun_id = guns.gun_id
        WHERE gun_type = "{gun_type}";
    """

    results = connectToMySQL(db).query_db(query)
    loadouts = []

    for one_loadout in results:
        loadouts.append(one_loadout)

    if not loadouts:
        return "No there are currently no loadouts associated with this type of gun"

    return convert_to_message(loadouts)
