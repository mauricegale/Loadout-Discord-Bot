file = open("flask_app/weapon_data/text_files/weapons.txt", "r")
temp = file.readlines()

weapons = [line.strip() for line in temp]
temp = []

file = open("flask_app/weapon_data/text_files/barrel.txt", "r")
temp = file.readlines()

barrels = [line.strip() for line in temp]
temp = []

file = open("flask_app/weapon_data/text_files/muzzle.txt", "r")
temp = file.readlines()

muzzles = [line.strip() for line in temp]
temp = []

file = open("flask_app/weapon_data/text_files/ammo.txt", "r")
temp = file.readlines()

ammo = [line.strip() for line in temp]
temp = []

file = open("flask_app/weapon_data/text_files/laser.txt", "r")
temp = file.readlines()

lasers = [line.strip() for line in temp]
temp = []

file = open("flask_app/weapon_data/text_files/magazine.txt", "r")
temp = file.readlines()

magazines = [line.strip() for line in temp]
temp = []

file = open("flask_app/weapon_data/text_files/rear_grip.txt", "r")
temp = file.readlines()

rear_grips = [line.strip() for line in temp]
temp = []

file = open("flask_app/weapon_data/text_files/stock.txt", "r")
temp = file.readlines()

stocks = [line.strip() for line in temp]
temp = []

file = open("flask_app/weapon_data/text_files/optic.txt", "r")
temp = file.readlines()

optics = [line.strip() for line in temp]
temp = []

file = open("flask_app/weapon_data/text_files/underbarrel.txt", "r")
temp = file.readlines()

underbarrels = [line.strip() for line in temp]
