import os
import sys

import pyrogram
from pyrogram import filters
from pyrogram.types import Message

from config import OWNER_ID
from strings import get_command
from prime import app
from prime.misc import SUDOERS
from prime.utils.database.memorydatabase import (
    get_active_chats, get_active_video_chats)

# Commands
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")
FAST_AC = get_command("FAST_AC")
CLR_LOG = get_command("CLR_LOG")



@app.on_message(filters.command(ACTIVEVC_COMMAND) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text(
        "ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛs ʟɪsᴛ..."
    )
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛs ᴏɴ ᴍᴜsɪᴄʙᴏᴛ...")
    else:
        await mystic.edit_text(
            f"**ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛs ᴏɴ ᴍᴜsɪᴄ ʙᴏᴛ :-**\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(ACTIVEVIDEO_COMMAND) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text(
        "ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛs ʟɪsᴛ..."
    )
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛs ᴏɴ ᴍᴜsɪᴄ ʙᴏᴛ...")
    else:
        await mystic.edit_text(
            f"**ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛs ᴏɴ ᴍᴜsɪᴄ ʙᴏᴛ :-**\n\n{text}",
            disable_web_page_preview=True,
        )



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#From Here - Ayush Added some unique features here!!
#Please Do Not Kang My Code Without My Permission!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


@app.on_message(filters.command(FAST_AC) & SUDOERS)
async def littleac(_, message: Message):
    ac_audio = str(len(get_active_chats))
    ac_video = str(len(get_active_video_chats))
    await message.reply_text(f"𝗕𝗼𝘁 𝗔𝗰𝘁𝗶𝘃𝗲 𝗖𝗵𝗮𝘁𝘀 𝗜𝗻𝗳𝗼 • 🔊\n•━━━━━━━━━━━━━━━━━━•\n🎧 ᴀᴜᴅɪᴏ 🎧 » {ac_audio} Active\n•───────•\n🎥 ᴠɪᴅᴇᴏ 🎥 » {ac_video} Active\n•──────•", quote=True)


@app.on_message(filters.command(CLR_LOG) & SUDOERS)
async def clearLogs(_, message: Message):
    A = 'rm -rf downloads'
    B = 'rm -rf cache'
    try:
        os.system(A)
        os.system(B)
        os.system('rm Ashlogs.txt')
        for i in range(10):
            number = str(i)
            os.system(f'rm Ashlogs{number}.txt')
    except:
        await message.reply_text(f"**Failed To Delete Some Files !!**\nPlease Read\n{traceback.format_exc()}", quote=True)
    await message.reply_text(f"**Successfully Deleted Below Folders & Files**:\n -Downloads\n -Cache\n -Logs\n\n **PLUGIN MADE BY** - Ayush", quote=True)


@app.on_message(
    filters.command("link")
    & filters.user(OWNER_ID)
    & ~filters.forwarded
    & ~filters.via_bot
)
async def link_getter(client, message):
    if len(message.command) < 2:
        return await edit_or_reply(
            message, text="**Did You Give Me Chat ID ?**"
            )
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
        ch_lid = int(cmd)
    except IndexError:
        return await message.delete()

    try:
        linkkk = await app.export_chat_invite_link(ch_lid)
        await message.reply_text(f"Here Is This Chat's Link >>\n\n{linkkk}", quote=True)
    except:
        await message.reply_text(f"Some Fucking Error Occured!\n\n TRY /new_link", quote=True)



@app.on_message(
    filters.command("new_link")
    & filters.user(OWNER_ID)
    & ~filters.forwarded
    & ~filters.via_bot
)
async def new_link_getter(client, message):
    if len(message.command) < 2:
        return await edit_or_reply(
            message, text="**Did You Give Me Chat ID ?**"
            )
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
        ch_lid = int(cmd)
    except IndexError:
        return await message.delete()

    try:
        linkkk = await app.create_chat_invite_link(ch_lid)
        await message.reply_text(f"Here Is This Chat's Link >>\n\n{linkkk}", quote=True)
    except:
        await message.reply_text(f"Some Fucking Error Occured!\n\n TRY /new_link", quote=True)
