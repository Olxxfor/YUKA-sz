# Konsultasi Profile Command
# Menampilkan informasi user dengan style YUKA OPEN SOURCE

from pyrogram.types import *
from PyroUbot import *
from PyroUbot.core.database.variabel import get_list_from_vars


@PY.UBOT("konsul")
async def _(client, message):
    """Tampilkan profil konsultasi user"""
    
    try:
        user = message.from_user
        
        # Ambil ADMIN_USERS list untuk cek status
        admin_list = await get_list_from_vars(client.me.id, "ADMIN_USERS")
        
        # Tentukan status
        if user.id == OWNER_ID:
            status = "👑 OWNER"
            status_color = "🔴"
        elif user.id in admin_list:
            status = "🛡️ ADMIN"
            status_color = "🔴"
        else:
            status = "👤 USER"
            status_color = "🔵"
        
        # Ambil username bot
        bot_username = (await bot.me()).username
        
        # Format message dengan styling
        message_text = f"""
╔═══════════════════════════════════════════╗
║                                           ║
║      🔴  YUKA OPEN SOURCE  🔴            ║
║                                           ║
╚═══════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>👤 USERNAME :</b>
<code>{user.username or "N/A"}</code>

<b>{status_color} STATUS :</b>
<code>{status}</code>

<b>🆔 ID :</b>
<code>{user.id}</code>

<b>🤖 BOT :</b>
<code>@{bot_username}</code>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        
        await message.reply(message_text)
        
    except Exception as e:
        await message.reply(
            f"""
<blockquote>
<b>❌ ᴇʀʀᴏʀ</b>

<b>ɢᴀɢᴀʟ ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ ᴋᴏɴsᴜʟ:</b>
<code>{str(e)}</code>
</blockquote>
"""
        )


@PY.BOT("konsul")
async def _(client, message):
    """Bot version - Tampilkan profil konsultasi user"""
    
    try:
        user = message.from_user
        
        # Ambil ADMIN_USERS list untuk cek status
        admin_list = await get_list_from_vars(OWNER_ID, "ADMIN_USERS")
        
        # Tentukan status
        if user.id == OWNER_ID:
            status = "👑 OWNER"
            status_color = "🔴"
        elif user.id in admin_list:
            status = "🛡️ ADMIN"
            status_color = "🔴"
        else:
            status = "👤 USER"
            status_color = "🔵"
        
        # Ambil username bot
        bot_username = (await bot.me()).username
        
        # Format message dengan YUKA OPEN SOURCE BESAR
        message_text = f"""
╔════════════════════════════════════════════════╗
║                                                ║
║                                                ║
║        🔴  YUKA OPEN SOURCE  🔴               ║
║                                                ║
║                                                ║
╚════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>👤 USERNAME :</b>
<code>{user.username or "N/A"}</code>

<b>{status_color} STATUS :</b>
<code>{status}</code>

<b>🆔 ID :</b>
<code>{user.id}</code>

<b>🤖 BOT :</b>
<code>@{bot_username}</code>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        
        await message.reply(message_text)
        
    except Exception as e:
        await message.reply(
            f"""
<blockquote>
<b>❌ ᴇʀʀᴏʀ</b>

<b>ɢᴀɢᴀʟ ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ ᴋᴏɴsᴜʟ:</b>
<code>{str(e)}</code>
</blockquote>
"""
        )
