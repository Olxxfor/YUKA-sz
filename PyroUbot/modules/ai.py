from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴀɪ"
__HELP__ = """
<blockquote><b>Bantuan Untuk AI

perintah : <code>{0}ai</code>
buat pertanyaan contoh <code>{0}ai</code> halo</b></blockquote>
"""

@PY.UBOT("ai")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply(
                "<blockquote><emoji id=5019523782004441717>❌</emoji>mohon gunakan format\ncontoh : .ai halo</blockquote>"
            )
        else:
            prs = await message.reply(f"<blockquote><emoji id=6226405134004389590>🔍</emoji>proccesing Kingz....</blockquote>")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.botcahx.eu.org/api/search/openai-chat?text={a}&apikey=Boyy')

            try:
                if "message" in response.json():
                    x = response.json()["message"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply("<blockquote><b>❌ No 'results' key found in the response.</b></blockquote>")
            except KeyError:
                await message.reply("<blockquote><b>❌ Error accessing the response.</b></blockquote>")
    except Exception as e:
        await message.reply(f"<blockquote><b>❌ Error: {e}</b></blockquote>")
