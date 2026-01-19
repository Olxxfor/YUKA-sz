import ast
from pyrogram import Client, filters
from PyroUbot import PY

__MODULE__ = "ᴄᴀʟᴄᴜʟᴀᴛᴏʀ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Kalkulator</b>

Perintah:
<code>{0}calc [ekspresi]</code> → Menghitung ekspresi matematika  
Contoh: <code>.calc 5 + 10 * 2</code>

Fitur ini bisa digunakan oleh siapa saja.</blockquote></b>
"""

@PY.UBOT("calc")
@PY.TOP_CMD
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        return await message.reply("<blockquote>❌ Format salah! Gunakan: <code>.calc [ekspresi]</code></blockquote>")

    expression = args[1]

    try:
        # Parsing ekspresi dengan AST (Agar lebih aman)
        result = eval(compile(ast.parse(expression, mode="eval"), "<string>", "eval"))
        await message.reply(f"<blockquote>✅ Hasil: <code>{result}</code></blockquote>")
    except Exception as e:
        await message.reply(f"<blockquote>❌ Error: {str(e)}</blockquote>")