import discord


class LoadoutCreateModalPage2(discord.ui.Modal, title="Enter Loadout Information"):
    laser_type = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Laser",
        required=False,
        placeholder="Enter Laser Type"
    )

    magazine_type = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Magazine",
        required=False,
        placeholder="Enter Magazine Type"
    )

    optic_type = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Optic",
        required=False,
        placeholder="Enter Optic Type"
    )

    rear_grip = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Rear Grip",
        required=False,
        placeholder="Enter Rear Grip"
    )

    muzzle_type = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Muzzle",
        required=False,
        placeholder="Enter Muzzle Type"
    )

    # underbarrel_type = discord.ui.TextInput(
    #     style=discord.TextStyle.short,
    #     label="Underbarrel",
    #     required=False,
    #     placeholder="Enter UnderBarrel Type"
    # )
    #
    # comb_type = discord.ui.TextInput(
    #     style=discord.TextStyle.short,
    #     label="Comb",
    #     required=False,
    #     placeholder="Enter Comb Type"
    # )
