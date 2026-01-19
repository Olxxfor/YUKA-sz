from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴜsᴇʀ ᴅᴀɴᴀ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴜsᴇʀ ᴅᴀɴᴀ ⦫</b>

<blockquote><b>⎆ ᴘᴇʀɪɴᴛᴀʜ :
ᚗ <code>{0}cekdana</code> 085xxxx

⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:
ᚗ cek username dana dari nomor</blockquote>

"""

@PY.UBOT("chekdana")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply(
                "<emoji id=5019523782004441717>❌</emoji>mohon gunakan format\ncontoh : .checkdana 085xxx"
            )
        else:
            prs = await message.reply(f"<blockquote><emoji id=6226405134004389590>🔍</emoji>proccesing Kingz....</blockquote>")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.siputzx.my.id/api/check/dana?account_number={a}')

            try:
                if "data" in response.json():
                    x = response.json()["data"]                  
                    await prs.edit(
                      f"<blockquote>BERIKUT DATA DARI PAYMENT DANA           {x}</blockquote>"
                    )
                else:
                    await message.reply("<blockquote>No 'results' key found in the response.</blockquote>")
            except KeyError:
                await message.reply("<blockquote>Error accessing the response.</blockquote>")
    except Exception as e:
        await message.reply(f"<blockquote>{e}</blockquote>")
