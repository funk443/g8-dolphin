# g8-dolphin: A general-purpose Discord bot.
# Copyright (C) 2024  CToID <funk443@yahoo.com.tw>

# This file is part of g8-dolphin.

# g8-dolphin is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# g8-dolphin is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with g8-dolphin.  If not, see <https://www.gnu.org/licenses/>.

from discord import Interaction, app_commands
from discord.ext.commands import Bot, Cog


class Ping(Cog):

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @app_commands.command(name="ping", description="Pong!")
    async def ping(self, interaction: Interaction) -> None:
        await interaction.response.send_message("Pong!")


async def setup(bot: Bot) -> None:
    await bot.add_cog(Ping(bot), override=True)
