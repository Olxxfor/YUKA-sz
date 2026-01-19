# Update Start Photo Command
# Command: /upfoto <reply to photo>
# Function: Upload/ganti foto di /start message

from pyrogram.types import *
from PyroUbot import *
from PyroUbot.core.database.variabel import get_vars, set_vars


@PY.UBOT("upfoto")
@PY.OWNER
async def _(client, message):
    """Upload/ganti foto untuk /start message"""
    
    if not message.reply_to_message:
        return await message.reply(
            """
<blockquote>
<b>❌ ᴇʀʀᴏʀ</b>

<b>ᴛᴇᴋ ʙᴀʟᴀs ᴘᴇsᴀɴ ʏᴀɴɢ ʙᴇʀɪsɪ ꜰᴏᴛᴏ ᴀᴛᴀᴜ ɢᴀᴍʙᴀʀ ɢᴀɴᴛɪ</b>

<b>ᴄᴏɴᴛᴏʜ:</b>
<code>/upfoto</code> <b>ᴠsᴀɪʟᴀs ʀᴇʙᴀʟɪ ᴋᴇ ꜰᴏᴛᴏ</b>
</blockquote>
"""
        )
    
    replied_msg = message.reply_to_message
    
    # Cek apakah pesan adalah foto
    if replied_msg.photo:
        try:
            photo_file_id = replied_msg.photo.file_id
            
            # Simpan ke database
            await set_vars(OWNER_ID, "START_PHOTO", photo_file_id)
            
            return await message.reply(
                """
<blockquote>
<b>✅ ʙᴇʀʜᴀsɪʟ</b>

<b>ꜰᴏᴛᴏ ᴅɪ /sᴛᴀʀᴛ ᴛᴇʟᴀʜ ᴅɪᴘᴇʀʙᴀʀᴜɪ</b>

<b>ᴄᴇᴋ ᴋᴇ /sᴛᴀʀᴛ ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴛᴀᴍᴘɪʟᴀɴɴʏᴀ</b>
</blockquote>
"""
            )
        except Exception as e:
            return await message.reply(
                f"""
<blockquote>
<b>❌ ᴇʀʀᴏʀ</b>

<b>ɢᴀɢᴀʟ ᴍᴇɴʏɪᴍᴘᴀɴ ꜰᴏᴛᴏ</b>

<b>ᴘᴇsᴀɴ ᴇʀʀᴏʀ:</b>
<code>{str(e)}</code>
</blockquote>
"""
            )
    else:
        return await message.reply(
            """
<blockquote>
<b>❌ ᴇʀʀᴏʀ</b>

<b>ᴘᴇsᴀɴ ʏᴀɴɢ ᴀɴᴅᴀ ʙᴀʟᴀs ʙᴜᴋᴀɴ ꜰᴏᴛᴏ</b>

<b>ᴄᴀʀᴀ ᴘᴇɴɢɢᴜɴᴀᴀɴ:</b>
<code>/upfoto</code> <b>ᴠsᴀɪʟᴀs ʀᴇʙᴀʟɪ ᴋᴇ ꜰᴏᴛᴏ</b>
</blockquote>
"""
        )


@PY.UBOT("delfoto")
@PY.OWNER
async def _(client, message):
    """Hapus foto dari /start message (kembali ke text saja)"""
    
    try:
        from PyroUbot.core.database.variabel import remove_vars
        
        await remove_vars(OWNER_ID, "START_PHOTO")
        
        return await message.reply(
            """
<blockquote>
<b>✅ ʙᴇʀʜᴀsɪʟ</b>

<b>ꜰᴏᴛᴏ ᴅɪ /sᴛᴀʀᴛ ᴛᴇʟᴀʜ ᴅɪʜᴀᴘᴜs</b>

<b>/sᴛᴀʀᴛ ᴀᴋᴀɴ ᴍᴇɴᴀᴍᴘɪʟᴋᴀɴ ᴛᴇxᴛ sᴀᴊᴀ</b>
</blockquote>
"""
        )
    except Exception as e:
        return await message.reply(
            f"""
<blockquote>
<b>❌ ᴇʀʀᴏʀ</b>

<b>ɢᴀɢᴀʟ ᴍᴇɴɢʜᴀᴘᴜs ꜰᴏᴛᴏ</b>

<b>ᴘᴇsᴀɴ ᴇʀʀᴏʀ:</b>
<code>{str(e)}</code>
</blockquote>
"""
        )
