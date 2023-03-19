import discord
from weapon_data.weapons import attachments
from discord.ui import View
from GunTypeSelection import GunTypeSelection


class LoadoutCreateView(View):

    def __init__(self):
        super().__init__()
        self.weapon_type = ""
        self.game_mode = ""


    GunTypeSelection

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

    @discord.ui.button(label="Submit", row=0, style=discord.ButtonStyle.primary)
    async def submit_button_callback(self, interaction, button):
        await interaction.response.defer()


    async def setup_ammo_view(self):
        ammos = attachments['ammo']
        options = []
        for i in range(20):
            options.append(discord.SelectOption(label=ammos[i], value=ammos[i], description="Ammo"))


        @discord.ui.select(
            custom_id="Ammo",
            placeholder="Ammo",
            options=options,
        )
        async def ammo_select_callback(self, interaction, select):
            self.response = select.values[0]
            await interaction.response.defer()
