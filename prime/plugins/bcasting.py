import asyncio
from datetime import datetime, timedelta
import time

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types

import config
from config import adminlist, chatstats, clean, userstats, OWNER_ID
from strings import get_command
from prime import app, userbot
from prime.misc import SUDOERS
from prime.utils.database import (get_served_chats,get_served_users)
from prime.utils.decorators.language import language
from prime.utils.formatters import alpha_to_int


BUSER_COMMAND = get_command("BUSER_COMMAND")
BCAST_COMMAND = get_command("BCAST_COMMAND")



@app.on_message(filters.command(BUSER_COMMAND) & filters.user(OWNER_ID))
async def send_to_users(client, message, _):
    if message.reply_to_message:
        x = message.reply_to_message.message_id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text("Please Reply To A message!\nThis Plugin Works Only For Forwarding Messages To Every Chats & Users!")

    susr = 0
    served_users = []
    susers = await get_served_users()
    for user in susers:
        served_users.append(int(user["user_id"]))

    time.sleep(20)
    countIDD = int(len(served_users))
    try:
        await message.reply_text(f"{countIDD} User's ID loaded✅\nBroadcast started now...🚀")
    except:
        print("Broadcasting now to users")
    for userId in served_users:
        try:
            await app.forward_messages(userId, y, x)
            susr += 1
        except FloodWait as e:
            flood_time = int(e.x)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            print("This User ID invalid or user not found! Maybe Bot is Blocked by user!")

    try:
        await message.reply_text(f"ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ᴛᴏ {susr} ᴜsᴇʀs.")
    except:
        print("Proccess Done Of Broadcasting to users")





@app.on_message(filters.command(BCAST_COMMAND) & filters.user(OWNER_ID))
async def send_to_chats(client, message, _):
    if message.reply_to_message:
        x = message.reply_to_message.message_id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(_["broad_5"])

    sent = 0
    chats = []
    schats = await get_served_chats()

    for chat in schats:
        chats.append(int(chat["chat_id"]))

    time.sleep(20)
    countCIDD = int(len(chats))

    try:
        await message.reply_text(f"{countCIDD} Chat's ID loaded✅\nBroadcast started now...🚀")
    except:
        print("Broadcasting To Chats")


    for chatId in chats:
        try:
            await app.forward_messages(chatId, y, x)
            sent += 1
        except FloodWait as e:
            flood_time = int(e.x)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            print("Group Chat ID not found!")

    try:
        await message.reply_text(f"ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪɴ {sent}  ᴄʜᴀᴛs ᴡɪᴛʜ 0 ᴘɪɴs ꜰʀᴏᴍ ʙᴏᴛ.")
    except:
        print(f"ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪɴ {sent}  ᴄʜᴀᴛs ᴡɪᴛʜ 0 ᴘɪɴs ꜰʀᴏᴍ ʙᴏᴛ.")