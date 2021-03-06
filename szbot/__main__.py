from sys import version as pyver
import subprocess
import shutil
import psutil
import time
import os
import random
import re

from szbot import sz, tele
from szbot import LOGGER
from pyrogram.errors import UserNotParticipant
from szbot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import Message, User

from config import BOT_TOKEN, SUDO_USERS
from szbot.plugins.menu import *
from szbot.helpers.fsub import ForceSub
from szbot.helpers.broadcast import broadcast_handler
from szbot.helpers.database.add_user import AddUserToDatabase
from szbot.helpers.database.access_db import db
from szbot.helpers.humanbytes import humanbytes


START_IMG = (
    "http://telegra.ph//file/6446461de37e64e66fa23.png",
    "http://telegra.ph//file/6f8b5760d0d3b6b2d13d6.png",
    "http://telegra.ph//file/9aaa3d6182bfa60c75719.png",
    "http://telegra.ph//file/eb9d3ceaddb80c8f54e0c.png",
    "http://telegra.ph//file/d6961d5ee000d19673aea.png",
    "http://telegra.ph//file/b84bdb7d085786752051d.png",
    "http://telegra.ph//file/330184a851ecf88b899a9.png",
    "http://telegra.ph//file/01c927f6ba69b0ee0e200.png",
    "http://telegra.ph//file/9b4ce9e507c491af3cecf.png",
    "http://telegra.ph//file/b6a00b71aee0610f13ac4.png",
)

@sz.on_message(filters.private & filters.incoming & filters.command(["start"]))
async def start(bot, update):
    await AddUserToDatabase(bot, update)
    FSub = await ForceSub(bot, update)
    if FSub == 400:
        return
    total_users = await db.total_users_count()
    START_TEXT = f"""
π Hello {update.from_user.mention} , π€

πββοΈ I am  π¨<b>Imagα₯± Tooα₯£s Bot</b>
<b>I specialize for logo design  Services with Amazing logo  Creator Platform & more tools</b>π
                                
πΆ <b>Powered by</b>:
β <code>Single Developers Logo Creator API</code>
β <code>Logo Generator Bot</code>
β <code>Gaming Lasith Random Logo Api</code>

π <b>Users</b> : {total_users}

Β©2021<a href=\"https://t.me/GL89X"> GL89X </a> π
"""
    await update.reply_photo(
                    photo=(random.choice(START_IMG)),
                    reply_markup=START_BTN,
                    caption=START_TEXT,
                    parse_mode="Html")

    
@sz.on_message(filters.command(["start", f"start@TheLogoGeneratorBot"]) & ~filters.private & ~filters.channel)
async def gstart(bot, update):
    await AddUserToDatabase(bot, update)
    FSub = await ForceSub(bot, update)
    if FSub == 400:
        return
    await update.reply_text(
                    text=START_TEXT.format(update.from_user.mention),
                    reply_markup=CLOSE_BTN,
                    parse_mode="Html",
                    disable_web_page_preview=True)

@sz.on_message(filters.command(["help", f"help@TheLogoGeneratorBot"]))
async def help(bot, update):
    await AddUserToDatabase(bot, update)
    FSub = await ForceSub(bot, update)
    if FSub == 400:
        return
    await update.reply_text(
        text=HELP_TEXT,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=CLOSE_BTN) 

@sz.on_message(filters.command(["about", f"about@TheLogoGeneratorBot"]))
async def about(bot, update):
    await AddUserToDatabase(bot, update)
    FSub = await ForceSub(bot, update)
    if FSub == 400:
        return
    await update.reply_text(
        text=ABOUT_TEXT,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=CLOSE_BTN)         

@sz.on_message(filters.private & filters.command("broadcast") & filters.user(SUDO_USERS) & filters.reply)
async def _broadcast(_, bot: Message):
    await broadcast_handler(bot)      
    
    
@sz.on_message(filters.command("stats") & filters.user(SUDO_USERS))
async def show_status_count(_, bot: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await bot.reply_text(
        text=f"**π½ Tα΄α΄α΄Κ DΙͺκ±α΄ Sα΄α΄α΄α΄:** {total} \n**πΏ Uκ±α΄α΄ Sα΄α΄α΄α΄:** `{used}({disk_usage}%)` \n**π FΚα΄α΄ Sα΄α΄α΄α΄:** `{free}` \n**Cα΄α΄ Uκ±α΄Ι’α΄:** `{cpu_usage}%` \n**Rα΄α΄ Uκ±α΄Ι’α΄:** `{ram_usage}%` \n\n**Tα΄α΄α΄Κ Uκ±α΄Κκ± π:** `{total_users}`\n\n**@TheLogoGeneratorBot π€**",
        parse_mode="Markdown",
        quote=True
    )       
    
@sz.on_message(filters.command(["ping", f"ping@TheLogoGeneratorBot"]))
async def ping(bot, update):
    await AddUserToDatabase(bot, update)
    FSub = await ForceSub(bot, update)
    if FSub == 400:
        return
    start_t = time.time()
    rm = await update.reply_text("**Checking..**")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"π½ `Pong!` \nβοΈ`{time_taken_s:.3f}` ms")    
    
sz.start()
tele.start(bot_token=BOT_TOKEN)
LOGGER.info("""

βββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββ
                                     
Β© @GL89X                                     
""")
idle()
