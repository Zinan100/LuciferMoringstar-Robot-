import logging
import asyncio
from info import LOG_CHANNEL
from pyrogram import Client, filters
from pyrogram.errors import RPCError
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

@Client.on_message(filters.command("autofilter"))
async def autofilter_set(c, m):
    if m.chat.type == "private":
        try:
            await m.reply("πππ ππππ πππππππ ππ π’πππ πππππ")
            return
        except Exception as e:
            LOGGER.exception(e)
    admin_check = await c.get_chat_member(m.chat.id, m.from_user.id)
    if not ((admin_check.status == "administrator") or (admin_check.status == "creator")):
        await m.reply("πππ πππ πππ ππ π°ππππ.")
        return
    if len(m.command) !=2:
        try:
            check = await get_session(int(m.chat.id))
            if check:
                await m.reply_text(
                    text=f"β π΅ππ½π²ππΈπΎπ½: <b>AUTO-FILTER</b>\nβ πππ°πππ: <b>#ON </b>π\nβ πΆππΎππΏ: <b>{m.chat.title}</b>",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton(
                            "TURN OFF π΄",
                            callback_data=f"auto_filter.off.{m.chat.id}"
                        )
                    ]])
                )
                m.continue_propogation()
            else:
                await m.reply_text(
                    text=f"β π΅ππ½π²ππΈπΎπ½: <b>AUTO-FILTER</b>\nβ πππ°πππ: <b>#OFF </b>π΄\nβ πΆππΎππΏ: <b>{m.chat.title}</b>",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton(
                            "TURN ON π",
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
            lel = await edit_or_reply(m, "πΏπππππππππ....")
            print("Processing..")
            lol = await add_chat(int(m.chat.id))
            if not lol:
                await lel.edit("π°πππππππππ ππ πππππππ’ πππππππ ππ ππππ π²πππ πππππ π.")
                return
            await lel.edit(f"π°πππππππππ ππππππ ππ β.\nπΆππππ: {m.chat.title}")
            await c.send_message(LOG_CHANNEL, text=f"#AUTOFILTER_ON\n\nπΆππππ: {m.chat.title}\nπ²πππ πΈπ³: `{m.chat.id}`\nπ±π’: {m.from_user.mention}")
            print(f"Autofilter turned on in {m.chat.title}")
        except Exception as e:
            LOGGER.exception(e)
    elif status == "off" or status == "OFF" or status == "Off":
        try:
            lel = await edit_or_reply(m, "πΏπππππππππ....")
            exo = await remove_chat(int(m.chat.id))
            if not exo:
                await lel.edit("π°πππππππππ ππ πππ πππππππ ππ ππππ ππππ πππππ π€·.")
                return
            await lel.edit(f"π°πππππππππ ππππππ πππ β.\nπΆππππ: {m.chat.title}.")
            await c.send_message(LOG_CHANNEL, text=f"#AUTOFILTER_OFF\n\nπΆππππ: {m.chat.title}\nπ²πππ πΈπ³: `{m.chat.id}`\nπ±π’: {m.from_user.mention}")
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
                f"β π΅ππ½π²ππΈπΎπ½: <b>AUTO-FILTER</b>\nβ πππ°πππ: <b>#OFF </b>π΄\nβ πΆππΎππΏ: <b>{q.message.chat.title}</b>",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                        "TURN ON π",
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
                f"β π΅ππ½π²ππΈπΎπ½: <b>AUTO-FILTER</b>\nβ πππ°πππ: <b>#ON </b>π\nβ πΆππΎππΏ: <b>{q.message.chat.title}</b>",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                        "TURN OFF π΄",
                        callback_data=f"auto_filter.off.{chat_id}"
                    )
                ]])
            )
        except RPCError as e:
            await q.answer(f"Error: {e}")
