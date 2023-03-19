import discord
from weapon_data.weapons import attachments
from discord.ui import View


class LoadoutCreateView(View):

    def __init__(self):
        super().__init__()
        self.weapon_type = ""
        self.game_mode = ""

    @discord.ui.select(
        placeholder="Select a Gun Type",
        options=[
            discord.SelectOption(label="AR", value="AR", description="Assault Rifle"),
            discord.SelectOption(label="SMG", value="SMG", description="Submachine Gun"),
            discord.SelectOption(label="LMG", value="LMG", description="Light Machine Gun"),
            discord.SelectOption(label="BR", value="BR", description="Battle Rifle"),
            discord.SelectOption(label="MR", value="MR", description="Marksman Rifle"),
            discord.SelectOption(label="SR", value="SR", description="Sniper Rifle"),
            discord.SelectOption(label="Pistol", value="Pistol", description="Pistol"),
            discord.SelectOption(label="Shotgun", value="Shotgun", description="Shotgun")],
    )
    async def gun_type_select_callback(self, interaction, select):
        self.response = select.values[0]
        await interaction.response.defer()

    @discord.ui.select(
        custom_id="game_mode",
        placeholder="Select Game Mode",
        options=[
            discord.SelectOption(label="Multiplayer", value="MP", description="Multiplayer"),
            discord.SelectOption(label="DMZ", value="DMZ", description="DMZ"),
            discord.SelectOption(label="WZ", value="WZ", description="Warzone")],
    )
    async def game_mode_select_callback(self, interaction, select):
        self.response = select.values[0]
        await interaction.response.defer()

    ammos = attachments['ammo']
    options = []
    for ammo in ammos:
        options.append(discord.SelectOption(label=ammo, value=ammo, description="Ammo"))
    @discord.ui.select(
        custom_id="Ammo",
        placeholder="Ammo",
        options= options,
    )
    async def ammo_select_callback(self, interaction, select):
        self.response = select.values[0]
        await interaction.response.defer()

    @discord.ui.button(label="Submit", row=0, style=discord.ButtonStyle.primary)
    async def submit_button_callback(self, interaction, button):
        await interaction.response.defer()
