from pyrogram import filters
from io import BytesIO
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from szbot import sz, aiohttpsession as session
from szbot.helpers.fsub import ForceSub

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with session.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

BUTTON = InlineKeyboardMarkup(
      [
        [
        InlineKeyboardButton(text="β Add me to your group β", url=f"http://t.me/szimagebot?startgroup=botstart") 
        ],
        [
         InlineKeyboardButton(text="π£οΈJoin my updates", url=f"https://t.me/szteambots") 
        ]
      ]      
    )

TEXT=f"""
βοΈ **carbon Created Successfully** β
βββββββββββββββββ
π₯ **Created by** : [π¨ Imα₯²gα₯± Tooα₯£s Bot](https://t.me/szimagebot)
β‘οΈ **Powered By**  : `γSZβ’γΒ΄
βββββββββββββββββ
Β©2021γSZβ’γ team  **All Right Reserved**β οΈοΈ
"""


@sz.on_message(filters.command(["carbon", f"carbon@szimagebot"]))
async def carbon_func(client, message):
    FSub = await ForceSub(client, message)
    if FSub == 400:
        return
    if not message.reply_to_message:
        return await message.reply_text("Reply to a text message.")
    if not message.reply_to_message.text:
        return await message.reply_text("Reply to a text message.")
    m = await message.reply_text("Preparing")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("Uploading")
    await client.send_photo(message.chat.id, carbon,caption=TEXT,reply_markup= BUTTON)
    await m.delete()
    carbon.close()
