from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from ZEFMUSIC import app
from ZEFMUSIC.misc import SUDOERS
from ZEFMUSIC.utils.database import add_sudo, remove_sudo, get_sudoers
from ZEFMUSIC.utils.decorators.language import language
from ZEFMUSIC.utils.extraction import extract_user
from ZEFMUSIC.utils.inline import close_markup
from config import BANNED_USERS, OWNER_ID


@app.on_message(filters.command(["addsudo"]) & filters.user(OWNER_ID))
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id in SUDOERS:
        return await message.reply_text(_["sudo_1"].format(user.mention))
    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(_["sudo_2"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(filters.command(["delsudo", "rmsudo"]) & filters.user(OWNER_ID))
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id not in SUDOERS:
        return await message.reply_text(_["sudo_3"].format(user.mention))
    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text(_["sudo_4"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(filters.command(["sudolist", "listsudo", "sudoers"]) & ~BANNED_USERS)
@language
async def sudoers_list(client, message: Message, _):
    text = _["sudo_5"]
    user = await app.get_users(OWNER_ID)
    user = user.first_name if not user.mention else user.mention
    text += f"1➤ {user}\n"
    count = 0
    smex = 0
    for user_id in SUDOERS:
        if user_id != OWNER_ID:
            try:
                user = await app.get_users(user_id)
                user = user.first_name if not user.mention else user.mention
                if smex == 0:
                    smex += 1
                    text += _["sudo_6"]
                count += 1
                text += f"{count}➤ {user}\n"
            except:
                continue
    if not text:
        await message.reply_text(_["sudo_7"])
    else:
        await message.reply_text(text, reply_markup=close_markup(_))


def sudoers_list():
    sudoers = SUDOERS
    text = "**Sudo Users List:**\n\n"
    for user_id in sudoers:
        try:
            user = app.get_users(user_id)
            user_name = user.first_name if not user.last_name else f"{user.first_name} {user.last_name}"
            text += f"• {user_name} [`{user_id}`]\n"
        except:
            text += f"• [`{user_id}`]\n"
    return text


def sudoers_markup():
    sudoers = SUDOERS
    markup = InlineKeyboardMarkup()
    for user_id in sudoers:
        try:
            user = app.get_users(user_id)
            user_name = user.first_name if not user.last_name else f"{user.first_name} {user.last_name}"
            markup.add(InlineKeyboardButton(text=user_name, user_id=user_id))
        except:
            markup.add(InlineKeyboardButton(text=str(user_id), user_id=user_id))
    return markup
