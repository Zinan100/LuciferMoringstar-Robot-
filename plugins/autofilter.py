# Give Credits if u Like 😜 # Ok Done 👍

import logging
import asyncio
from info import LOG_CHANNEL
from pyrogram import Client, filters
from pyrogram.errors import RPCError
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from database.autofilter_db import *
# LOGGING ERRORS
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

@Client.on_message(filters.command("autofilter"))
async def autofilter_set(c, m):
    if m.chat.type == "private":
        try:
            await m.reply("𝚄𝚜𝚎 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚒𝚗 𝚢𝚘𝚞𝚛 𝚐𝚛𝚘𝚞𝚙")
            return
        except Exception as e:
            LOGGER.exception(e)
    admin_check = await c.get_chat_member(m.chat.id, m.from_user.id)
    if not ((admin_check.status == "administrator") or (admin_check.status == "creator")):
        await m.reply("𝚈𝚘𝚞 𝚊𝚛𝚎 𝚗𝚘𝚝 𝚊𝚗 𝙰𝚍𝚖𝚒𝚗.")
        return
    if len(m.command) !=2:
        try:
            check = await get_session(int(m.chat.id))
            if check:
                await m.reply_text(
                    text=f"❍ 𝙵𝚄𝙽𝙲𝚃𝙸𝙾𝙽: <b>AUTO-FILTER</b>\n❍ 𝚂𝚃𝙰𝚃𝚄𝚂: <b>#ON </b>🔆\n❍ 𝙶𝚁𝙾𝚄𝙿: <b>{m.chat.title}</b>",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton(
                            "TURN OFF 📴",
                            callback_data=f"auto_filter.off.{m.chat.id}"
                        )
                    ]])
                )
                m.continue_propogation()
            else:
                await m.reply_text(
                    text=f"❍ 𝙵𝚄𝙽𝙲𝚃𝙸𝙾𝙽: <b>AUTO-FILTER</b>\n❍ 𝚂𝚃𝙰𝚃𝚄𝚂: <b>#OFF </b>📴\n❍ 𝙶𝚁𝙾𝚄𝙿: <b>{m.chat.title}</b>",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton(
                            "TURN ON 🔆",
                            callback_data=f"auto_filter.on.{m.chat.id}"
                        )
                    ]])
                )
                m.continue_propogation()
        except Exception as e:
            LOGGER.exception(e)
    status = m.text.split(None, 1)[1]
    chat_id = m.chat.id
    if status == "ON" or status == "On" or status == "on":
        try:
            lel = await edit_or_reply(m, "𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐....")
            print("Processing..")
            lol = await add_chat(int(m.chat.id))
            if not lol:
                await lel.edit("𝙰𝚞𝚝𝚘𝚏𝚒𝚕𝚝𝚎𝚛 𝚒𝚜 𝚊𝚕𝚛𝚎𝚊𝚍𝚢 𝚎𝚗𝚊𝚋𝚕𝚎𝚍 𝚒𝚗 𝚝𝚑𝚒𝚜 𝙲𝚑𝚊𝚝 𝚐𝚛𝚘𝚞𝚙 🙇.")
                return
            await lel.edit(f"𝙰𝚞𝚝𝚘𝚏𝚒𝚕𝚝𝚎𝚛 𝚃𝚞𝚛𝚗𝚎𝚍 𝚘𝚗 ✅.\n𝙶𝚛𝚘𝚞𝚙: {m.chat.title}")
            await c.send_message(LOG_CHANNEL, text=f"#AUTOFILTER_ON\n\n𝙶𝚛𝚘𝚞𝚙: {m.chat.title}\n𝙲𝚑𝚊𝚝 𝙸𝙳: `{m.chat.id}`\n𝙱𝚢: {m.from_user.mention}")
            print(f"Autofilter turned on in {m.chat.title}")
        except Exception as e:
            LOGGER.exception(e)
    elif status == "off" or status == "OFF" or status == "Off":
        try:
            lel = await edit_or_reply(m, "𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐....")
            exo = await remove_chat(int(m.chat.id))
            if not exo:
                await lel.edit("𝙰𝚞𝚝𝚘𝚏𝚒𝚕𝚝𝚎𝚛 𝚒𝚜 𝚗𝚘𝚝 𝚎𝚗𝚊𝚋𝚕𝚎𝚍 𝚒𝚗 𝚝𝚑𝚒𝚜 𝚌𝚑𝚊𝚝 𝚐𝚛𝚘𝚞𝚙 🤷.")
                return
            await lel.edit(f"𝙰𝚞𝚝𝚘𝚏𝚒𝚕𝚝𝚎𝚛 𝚃𝚞𝚛𝚗𝚎𝚍 𝚘𝚏𝚏 ✅.\n𝙶𝚛𝚘𝚞𝚙: {m.chat.title}.")
            await c.send_message(LOG_CHANNEL, text=f"#AUTOFILTER_OFF\n\n𝙶𝚛𝚘𝚞𝚙: {m.chat.title}\n𝙲𝚑𝚊𝚝 𝙸𝙳: `{m.chat.id}`\n𝙱𝚢: {m.from_user.mention}")
            print(f"Autofilter turned off in {m.chat.title}")
        except Exception as e:
            LOGGER.exception(e)

async def edit_or_reply(message, text, parse_mode="md"):
    if message.from_user.id:
        if message.reply_to_message:
            kk = message.reply_to_message.message_id
            return await message.reply_text(
                text, reply_to_message_id=kk, parse_mode=parse_mode
            )
        return await message.reply_text(text, parse_mode=parse_mode)
    return await message.edit(text, parse_mode=parse_mode)

@Client.on_callback_query(filters.regex(r'^auto_filter'))
async def atfltr_cb(c: Client, q: CallbackQuery):
    query = q.data.split(".")
    action = query[1]
    chat_id = query[2]
    if action == "off":
        try:
            st = await c.get_chat_member(chat_id, q.from_user.id)
            if not ((st.status == "administrator") or (st.status == "creator")):
               await q.answer("You are not an Admin", show_alert=True)
               return
            lol = await q.message.edit_text("Processing...")
            exo = await remove_chat(int(chat_id))
            await lol.edit_text(
                f"❍ 𝙵𝚄𝙽𝙲𝚃𝙸𝙾𝙽: <b>AUTO-FILTER</b>\n❍ 𝚂𝚃𝙰𝚃𝚄𝚂: <b>#OFF </b>📴\n❍ 𝙶𝚁𝙾𝚄𝙿: <b>{q.message.chat.title}</b>",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                        "TURN ON 🔆",
                        callback_data=f"auto_filter.on.{chat_id}"
                    )
                ]])
            )
        except RPCError as e:
            await q.answer(f"Error: {e}")
    elif action == "on":
        try:
            st = await c.get_chat_member(chat_id, q.from_user.id)
            if not ((st.status == "administrator") or (st.status == "creator")):
               await q.answer("You are not an Admin", show_alert=True)
               return
            lol = await q.message.edit_text("Processing...")
            exo = await add_chat(int(chat_id))
            await lol.edit_text(
                f"❍ 𝙵𝚄𝙽𝙲𝚃𝙸𝙾𝙽: <b>AUTO-FILTER</b>\n❍ 𝚂𝚃𝙰𝚃𝚄𝚂: <b>#ON </b>🔆\n❍ 𝙶𝚁𝙾𝚄𝙿: <b>{q.message.chat.title}</b>",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                        "TURN OFF 📴",
                        callback_data=f"auto_filter.off.{chat_id}"
                    )
                ]])
            )
        except RPCError as e:
            await q.answer(f"Error: {e}")
