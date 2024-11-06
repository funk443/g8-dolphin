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

import asyncio
from discord.ext.commands import Bot
from src.g8_dolphin.bot import setup_bot
import bot_config

bot: Bot = asyncio.run(setup_bot(bot_config=bot_config))
bot.run(token=bot.user_config.token)
