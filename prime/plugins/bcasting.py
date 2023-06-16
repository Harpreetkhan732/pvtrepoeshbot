import asyncio
import time

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from config import OWNER_ID
from prime import app, userbot
from prime.utils.database import (get_served_chats, get_served_users)





@app.on_message(filters.command("bcast_chats") & filters.user(OWNER_ID))
async def broadcastingchats(_, message):
    if message.reply_to_message:
        x = message.reply_to_message.message_id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(
                "**Usage**:\n/broadcast [MESSAGE] or [Reply to a Message]"
            )
        query = message.text.split(None, 1)[1]
    sent = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))

    time.sleep(60)
    chcount = int(len(chats))
    try:
        await message.reply_text(f"{chcount} chats loaded✅\nBroadcast started now...🚀")
    except:
        print("Broadcast_Chats Loaded!")

    for i in chats:
        try:
            await app.forward_messages(
                i, y, x
            ) if message.reply_to_message else await app.send_message(
                i, text=query
            )
            sent += 1
        except FloodWait as e:
            flood_time = int(e.x)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
    try:
        await message.reply_text(
            f"**Broadcasted Message In {sent} Chats.**"
        )
    except:
        pass

@app.on_message(filters.command("bcast_users") & filters.user(OWNER_ID))
async def broadcastingusers(_, message):
    if message.reply_to_message:
        x = message.reply_to_message.message_id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(
                "**Usage**:\n/broadcast [MESSAGE] or [Reply to a Message]"
            )
        query = message.text.split(None, 1)[1]
    sent = 0
    susrs = []
    schas = await get_served_users()
    for userlol in schas:
        susrs.append(int(userlol["user_id"]))

    time.sleep(20)
    chacount = int(len(susrs))
    try:
        await message.reply_text(f"{chacount} users loaded✅\nBroadcast started now...🚀")
    except:
        print("Broadcast_Users Loaded!")

    for i in susrs:
        try:
            await app.forward_messages(
                i, y, x
            ) if message.reply_to_message else await app.send_message(
                i, text=query
            )
            sent += 1
        except FloodWait as e:
            flood_time = int(e.x)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
    try:
        await message.reply_text(
            f"**Broadcasted Message To {sent} Users.**"
        )
    except:
        pass
