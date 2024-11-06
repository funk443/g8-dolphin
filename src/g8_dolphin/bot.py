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

import logging
import os
from types import ModuleType
from discord import Intents
from discord.ext.commands import Bot


async def load_features(bot: Bot) -> None:
    for filename in os.listdir(bot.features_dir):
        if filename.startswith("__"):
            continue

        name = filename[:-3]
        await bot.load_extension(
            name=f".{name}", package=f"{__package__}.features"
        )
        bot.logger.info(f"Loaded feature '{name}'.")


async def setup_bot(bot_config: ModuleType) -> Bot:
    bot = Bot(command_prefix="$", intents=Intents.all())
    bot.user_config = bot_config
    bot.features_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "features"
    )

    bot.logger = logging.getLogger("bot_logger")
    bot.logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter(
            fmt="%(asctime)s %(levelname)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    bot.logger.addHandler(handler)

    @bot.event
    async def on_ready() -> None:
        bot.logger.info("Successfully connected.")
        await bot.tree.sync()

    await load_features(bot=bot)
    return bot
