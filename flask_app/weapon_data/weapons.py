file = open("flask_app/weapon_data/weapons.txt", "r")
temp = file.readlines()

weapons = [line.strip() for line in temp]
