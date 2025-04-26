import os
import time
import logging
from config import BOT_USERNAME, OWNER_ID
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pyrogram import filters, Client
from pyrogram.types import Message

import config
from ZEFMUSIC.core.mongo import mongodb

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler(
            "zefmusic.log", maxBytes=50000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

# Bot start time
bot_start_time = time.time()

SUDOERS = filters.user()
_boot_ = time.time()

def dbb():
    global db
    db = {}
    LOGGER.info(f"Local Database Initialized.")

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
    LOGGER.info(f"Sudoers Loaded.")

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

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

def get_file_id(msg):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            "sticker"
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj
