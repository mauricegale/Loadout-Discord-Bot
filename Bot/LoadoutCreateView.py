import discord
from weapon_data.weapons import attachments
from discord.ui import View
from LoadoutCreateModalPage1 import LoadoutCreateModalPage1
from LoadoutCreateModalPage2 import LoadoutCreateModalPage2


class LoadoutCreateView(View):

    # async def send(self, ctx):
    #     self.message = await interaction.response.send_modal(LoadoutCreateModal(title="Create Loadout"))
    @discord.ui.button(label="Create Loadout", row=0, style=discord.ButtonStyle.primary)
    async def button_callback(self, interaction, button):
        modal = LoadoutCreateModalPage1(title="Create Loadout Page(1/3)")
        await interaction.response.send_modal(modal)
