from telethon import events, Button, custom, version
from telethon.tl.types import ChannelParticipantsAdmins
import asyncio
import os, re
import requests
import datetime
import time
from datetime import datetime
import random
from PIL import Image
from io import BytesIO
from MissLyraRobot import telethn as bot
from MissLyraRobot import telethn as tgbot
from MissLyraRobot.events import register
from MissLyraRobot import dispatcher
from telegram import ParseMode

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/979500203d6fcf1924130.jpg"
file2 = "https://telegra.ph/file/6b09f8642d1890e4d67c8.jpg"
file3 = "https://telegra.ph/file/abf580ada4818ab99f9c0.jpg"
file4 = "https://telegra.ph/file/ab410f256673c3001307b.jpg"
file5 = "https://telegra.ph/file/398e8cb58bff53c59ee19.jpg"
""" =======================CONSTANTS====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    chat = await event.get_chat()
    current_time = datetime.utcnow()
    smexy = event.sender.first_name
    button = [[custom.Button.inline("[► Click Here ◄]", data="information")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"➣ **Hey** {smexy} **I'm Lyra.**\n➣ **Powered By @TheXCodeTeam**\n➣ **Click The Button Below To Get Your Info! In Lyra.**",
        parse_mode=ParseMode.MARKDOWN,
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        HOTTIE = "➢ YOUR DETAILS BY LYRA \n\n"
        HOTTIE += f"• FIRST NAME : {PRO.first_name} \n"
        HOTTIE += f"• LAST NAME : {PRO.last_name}\n"
        HOTTIE += f"• RESTRICTED : {PRO.restricted} \n"
        HOTTIE += f"• USER ID : {boy}\n"
        HOTTIE += f"• USERNAME : {PRO.username}\n"
        await event.answer(HOTTIE, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__help__ = """
/myinfo: shows your info in inline
"""

__mod_name__ = "Myinfo"
__command_list__ = ["myinfo"]
