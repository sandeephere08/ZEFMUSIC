import time
from pyrogram import filters, Client
from pyrogram.types import Message

import config
from ZEFMUSIC.core.mongo import mongodb
from .logging import LOGGER

SUDOERS = filters.user()
_boot_ = time.time()

def dbb():
    global db
    db = {}
    LOGGER(__name__).info(f"Local Database Initialized.")

async def sudo():
    global SUDOERS
    SUDOERS.add(config.OWNER_ID)
    sudoersdb = mongodb.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    if config.OWNER_ID not in sudoers:
        sudoers.append(config.OWNER_ID)
        await sudoersdb.update_one(
            {"sudo": "sudo"},
            {"$set": {"sudoers": sudoers}},
            upsert=True,
        )
    if sudoers:
        for user_id in sudoers:
            SUDOERS.add(user_id)
    LOGGER(__name__).info(f"Sudoers Loaded.")

async def add_sudo(client: Client, message: Message):
    if not message.from_user.id == config.OWNER_ID:
        return await message.reply_text("Only owner can add sudo users!")
    
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text("Reply to a user's message or give username/user id.")
    
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        user_mention = message.reply_to_message.from_user.mention
    else:
        try:
            user = await client.get_users(message.command[1])
            user_id = user.id
            user_mention = user.mention
        except:
            return await message.reply_text("Invalid username/user id.")

    if user_id == config.OWNER_ID:
        return await message.reply_text("Owner is already a sudo user!")
    
    sudoersdb = mongodb.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    
    if user_id in sudoers:
        return await message.reply_text("User is already a sudo user!")
    
    sudoers.append(user_id)
    await sudoersdb.update_one(
        {"sudo": "sudo"},
        {"$set": {"sudoers": sudoers}},
        upsert=True,
    )
    SUDOERS.add(user_id)
    await message.reply_text(f"Added {user_mention} as sudo user.")
