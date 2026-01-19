from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PyroUbot import OWNER_ID, bot, ubot, get_expired_date


class MSG:

    def EXP_MSG_UBOT(X):
        return f"""
<blockquote>
<b>❏ ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>

<b>├ ᴀᴋᴜɴ :</b>  
<a href="tg://user?id={X.me.id}">
<b>{X.me.first_name} {X.me.last_name or ''}</b>
</a>

<b>├ ɪᴅ :</b>  
<code>{X.me.id}</code>

<b>╰ ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴛᴇʟᴀʜ ʜᴀʙɪs</b>
</blockquote>
"""

    def START(message):
        return f"""
<blockquote>𝐇𝐀𝐈 𝐇𝐀𝐈 👋🏻👋🏻
<a href="tg://user?id={message.from_user.id}"><b>{message.from_user.first_name} {message.from_user.last_name or ''}</b></a> 𝐒𝐄𝐋𝐀𝐌𝐀𝐓 𝐃𝐀𝐓𝐀𝐍𝐆 𝐃𝐈 <b>@{bot.me.username}</b>

𝐁𝐄𝐋𝐈𝐄𝐕𝐄 𝐈𝐍 𝐘𝐎𝐔𝐑 𝐏𝐎𝐖𝐄𝐑
𝐄𝐍𝐉𝐎𝐘 𝐄𝐀𝐂𝐇 𝐌𝐎𝐌𝐄𝐍𝐓
𝐆𝐎𝐃 𝐈𝐒 𝐖𝐈𝐓𝐇 𝐘𝐎𝐔 🕊️
</blockquote>

<blockquote>✘ 𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐏𝐀𝐊𝐄𝐓 / 𝐋𝐀𝐘𝐀𝐍𝐀𝐍 ✘

🖤 <b>Buat Userbot otomatis</b>
🖤 <b>Pilih masa aktif sesuai paket (hari/bulan)</b>
🖤 <b>Sistem pembayaran & verifikasi cepat</b>
🖤 <b>Bisa dijadikan reseller atau upgrade paket</b>
</blockquote>

<blockquote>✘ 𝐔𝐒𝐄𝐑 𝐈𝐍𝐅𝐎 ✘ ⚫

🃏 <b>ID :</b> <code>{message.from_user.id}</code>
🃏 <b>USERNAME :</b> <code>@{message.from_user.username or 'tidak ada'}</code>
🃏 <b>STATUS :</b> <code>belum membeli userbot</code>
</blockquote>

<blockquote>𝐂𝐑𝐄𝐀𝐓𝐄𝐃 𝐁𝐘
<a href="tg://openmessage?user_id={OWNER_ID}"><b>@YUKALASTERA</b></a> 🥷🏻
𝐍𝐀𝐌𝐀 𝐁𝐎𝐓 : <b>@{bot.me.username}</b></blockquote>
"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<blockquote>
<b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ</b>

<b>🎟️ ʜᴀʀɢᴀ :</b>  
<b>ʀᴘ {harga}.000 / ʙᴜʟᴀɴ</b>

<b>💳 ᴍᴇᴛᴏᴅᴇ :</b>  
<b>Qʀɪꜱ ᴀʟʟ ᴘᴀʏᴍᴇɴᴛ</b>

<b>🔖 ᴛᴏᴛᴀʟ :</b>  
<b>ʀᴘ {total}.000</b>

<b>🗓️ ᴅᴜʀᴀsɪ :</b>  
<b>{bulan}</b>

<b>ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ</b>  
<b>ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ</b>
</blockquote>
"""

    async def UBOT(count):
        count_int = int(count)
        if 0 <= count_int < len(ubot._ubot):
            userbot_obj = ubot._ubot[count_int]
            return f"""
<blockquote>
<b>╭〢 ᴜsᴇʀʙᴏᴛ ᴋᴇ :</b>  
<code>{count_int + 1}/{len(ubot._ubot)}</code>

<b>├〢 ᴀᴄᴄᴏᴜɴᴛ :</b>  
<a href="tg://user?id={userbot_obj.me.id}">
<b>{userbot_obj.me.first_name}</b>
</a>

<b>╰〢 ᴜsᴇʀ ɪᴅ :</b>  
<code>{userbot_obj.me.id}</code>
</blockquote>
"""
        else:
            return "<blockquote><b>❌ Userbot tidak ditemukan</b></blockquote>"

    def POLICY():
        return """
<blockquote>
⚠️ <b>ᴅɪsᴄʟᴀɪᴍᴇʀ ᴘᴇɴɢɢᴜɴᴀᴀɴ ᴜsᴇʀʙᴏᴛ</b> ⚠️

ᴘᴇɴɢɢᴜɴᴀᴀɴ ᴜsᴇʀʙᴏᴛ ᴍᴇᴍɪʟɪᴋɪ ʀɪsɪᴋᴏ  
ʏᴀɴɢ ᴡᴀᴊɪʙ ᴅɪᴘᴀʜᴀᴍɪ ᴏʟᴇʜ  
sᴇᴛɪᴀᴘ ᴘᴇɴɢɢᴜɴᴀ.

ᴛᴇʟᴇɢʀᴀᴍ ᴅᴀᴘᴀᴛ ᴍᴇʟᴀᴋᴜᴋᴀɴ  
ᴘᴇᴍʙᴀᴛᴀsᴀɴ (ʟɪᴍɪᴛ),  
ᴘᴇᴍʙʟᴏᴋɪʀᴀɴ sᴇᴍᴇɴᴛᴀʀᴀ,  
ʜɪɴɢɢᴀ ʙᴀɴɴᴇᴅ ᴘᴇʀᴍᴀɴᴇɴ  
ᴘᴀᴅᴀ ᴀᴋᴜɴ ᴊɪᴋᴀ ᴛᴇʀᴅᴇᴛᴇᴋsɪ  
ᴀᴋᴛɪᴠɪᴛᴀs ʏᴀɴɢ ᴍᴇʟᴀɴɢɢᴀʀ  
ᴋᴇʙɪᴊᴀᴋᴀɴ ᴛᴇʟᴇɢʀᴀᴍ, sᴇᴘᴇʀᴛɪ:

• sᴘᴀᴍ ʙᴇʀʟᴇʙɪʜᴀɴ  
• ꜰʟᴏᴏᴅ ᴍᴇssᴀɢᴇ  
• ᴘᴇɴʏᴀʟᴀʜɢᴜɴᴀᴀɴ ꜰɪᴛᴜʀ  
• ᴀᴋᴛɪᴠɪᴛᴀs ᴍᴇɴᴄᴜʀɪɢᴀᴋᴀɴ ʟᴀɪɴɴʏᴀ

❗ <b>ᴅᴇɴɢᴀɴ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴜsᴇʀʙᴏᴛ ɪɴɪ,  
ᴘᴇɴɢɢᴜɴᴀ ᴍᴇɴʏᴇᴛᴜᴊᴜɪ ʙᴀʜᴡᴀ:</b>

• sᴇɢᴀʟᴀ ʙᴇɴᴛᴜᴋ ʀɪsɪᴋᴏ  
  sᴇᴘᴇɴᴜʜɴʏᴀ ᴍᴇɴᴊᴀᴅɪ  
  ᴛᴀɴɢɢᴜɴɢ ᴊᴀᴡᴀʙ ᴘᴇɴɢɢᴜɴᴀ

• ᴀᴅᴍɪɴ / sᴇʟʟᴇʀ / ᴅᴇᴠᴇʟᴏᴘᴇʀ  
  <b>ᴛɪᴅᴀᴋ ʙᴇʀᴛᴀɴɢɢᴜɴɢ ᴊᴀᴡᴀʙ</b> ᴀᴛᴀs:
  – ᴀᴋᴜɴ ᴛᴇʀᴋᴇɴᴀ ʟɪᴍɪᴛ  
  – ᴀᴋᴜɴ ᴅɪʙʟᴏᴋɪʀ sᴇᴍᴇɴᴛᴀʀᴀ  
  – ᴀᴋᴜɴ ʙᴀɴɴᴇᴅ ᴘᴇʀᴍᴀɴᴇɴ  
  – ᴋᴇʀᴜɢɪᴀɴ ᴅᴀʟᴀᴍ ʙᴇɴᴛᴜᴋ ᴀᴘᴀ ᴘᴜɴ

📌 <b>ᴛɪɴɢᴋᴀᴛ ʀɪsɪᴋᴏ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ɪᴅ ᴀᴋᴜɴ</b>

<b>ɪᴅ 1 — 6</b>  
➜ ʀᴇʟᴀᴛɪꜰ ʟᴇʙɪʜ ᴀᴍᴀɴ  
➜ sᴇʟᴀᴍᴀ ᴘᴇɴɢɢᴜɴᴀᴀɴ ᴡᴀᴊᴀʀ  
➜ ᴛɪᴅᴀᴋ ᴍᴇʟᴀᴋᴜᴋᴀɴ sᴘᴀᴍ

<b>ɪᴅ 7 — 8</b>  
➜ ʀᴀᴡᴀɴ ʀɪsɪᴋᴏ  
➜ ᴊɪᴋᴀ ʙᴇʟᴜᴍ sɪᴀᴘ ᴍᴇɴᴇʀɪᴍᴀ ʀɪsɪᴋᴏ,  
   <b>ᴅɪʟᴀʀᴀɴɢ ᴍᴇɴᴄᴏʙᴀ</b>  
➜ ᴊɪᴋᴀ ᴀᴋᴜɴ ᴛᴇʀᴋᴇɴᴀ ʙᴀɴɴᴇᴅ,  
   <b>ᴊᴀɴɢᴀɴ ᴍᴇɴʏᴀʟᴀʜᴋᴀɴ ᴀᴅᴍɪɴ / sᴇʟʟᴇʀ</b>

📎 <b>ᴘᴇʀɪɴɢᴀᴛᴀɴ ᴘᴇɴᴛɪɴɢ</b>  
• ɢᴜɴᴀᴋᴀɴ ᴜsᴇʀʙᴏᴛ ᴅᴇɴɢᴀɴ ʙɪᴊᴀᴋ  
• ʜɪɴᴅᴀʀɪ sᴘᴀᴍ ʙᴇʀʟᴇʙɪʜᴀɴ  
• ɢᴜɴᴀᴋᴀɴ ᴅᴇʟᴀʏ ʏᴀɴɢ ᴡᴀᴊᴀʀ  
• sᴀɴɢᴀᴛ ᴅɪsᴀʀᴀɴᴋᴀɴ  
  ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴀᴋᴜɴ ᴄᴀᴅᴀɴɢᴀɴ  
• ᴊᴀɴɢᴀɴ ɢᴜɴᴀᴋᴀɴ  
  ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ / ᴀᴋᴜɴ ᴘᴇɴᴛɪɴɢ

⚠️ <b>ᴅᴇɴɢᴀɴ ᴍᴇʟᴀɴᴊᴜᴛᴋᴀɴ ᴘᴇɴɢɢᴜɴᴀᴀɴ ᴜsᴇʀʙᴏᴛ,  
ᴀɴᴅᴀ ᴅɪᴀɴɢɢᴀᴘ ᴛᴇʟᴀʜ ᴍᴇᴍᴀʜᴀᴍɪ  
ᴅᴀɴ ᴍᴇɴʏᴇᴛᴜᴊᴜɪ sᴇʟᴜʀᴜʜ ʀɪsɪᴋᴏ ᴅɪ ᴀᴛᴀs.</b>

<b>sᴇɢᴀʟᴀ ʀɪsɪᴋᴏ sᴇᴘᴇɴᴜʜɴʏᴀ  
ᴅɪᴛᴀɴɢɢᴜɴɢ ᴏʟᴇʜ ᴘᴇɴɢɢᴜɴᴀ.</b>
</blockquote>
"""