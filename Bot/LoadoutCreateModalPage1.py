import discord
from LoadoutCreateModalPage2 import LoadoutCreateModalPage2


class LoadoutCreateModalPage1(discord.ui.Modal, title="Enter Loadout Information"):
    def __init__(self, view):
        self.view = view
        super().__init__()

    creator_name = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Creator's Name",
        required=True,
        placeholder="Enter Creator's Name"
    )

    gun_name = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Gun Name",
        required=True,
        placeholder="Enter Gun Name"
    )

    ammo_type = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Ammo",
        required=False,
        placeholder="Enter Ammo Type"
    )

    stock_type = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Stock",
        required=False,
        placeholder="Enter Stock Type"
    )

    barrel_type = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Barrel",
        required=False,
        placeholder="Enter Barrel Type"
    )

    async def on_submit(self, interaction):
        await interaction.response.defer(thinking=False)

        button1 = discord.ui.Button(label="Next", style=discord.ButtonStyle.primary)
        self.view.add_item(button1)

        # modal2 = LoadoutCreateModalPage2(title="Create Loadout Page(2/3)")
        # await interaction.response.follow_up(modal2)
        # await interaction.response.send_m(f'Thanks for your response, {self.creator_name}!', ephemeral=True)
        # await interaction.response.send_modal(modal2)
        # modal2 = LoadoutCreateModalPage2(title="Create Loadout Page(2/3)")
        # await interaction.response.send_modal(modal2)

        @discord.ui.button(label="Next", row=0, style=discord.ButtonStyle.primary)
        async def button_callback(self, interaction, button):
            modal2 = LoadoutCreateModalPage2(title="Create Loadout Page(2/3)")
            await interaction.response.send_modal(modal2)

        # @discord.ui.button(label="Page 2", row=0, style=discord.ButtonStyle.primary)
        # async def button_callback(self, interaction, button):
        #     modal2 = LoadoutCreateModalPage2(title="Create Loadout Page(2/3)")
        #     await interaction.response.send_modal(modal2)
