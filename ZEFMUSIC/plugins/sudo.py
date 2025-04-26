from pyrogram import Client, filters
from pyrogram.types import Message

from ZEFMUSIC.misc import SUDOERS, add_sudo
import config

@Client.on_message(filters.command("addsudo") & filters.user(config.OWNER_ID))
async def add_sudo_handler(client: Client, message: Message):
    await add_sudo(client, message) 