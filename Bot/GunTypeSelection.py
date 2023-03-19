import discord
from discord.ui import Select


class GunTypeSelection(Select):
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
