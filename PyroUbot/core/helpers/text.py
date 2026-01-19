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
<blockquote>
👋🏻 <b>ʜᴀʟᴏ —</b>  
<a href="tg://user?id={message.from_user.id}">
<b>{message.from_user.first_name} {message.from_user.last_name or ''}</b>
</a>

📚💎 <b>@{bot.me.username}</b>  
ᴀᴅᴀʟᴀʜ ʙᴏᴛ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴜᴀᴛ <b>ᴜsᴇʀʙᴏᴛ</b>  
ᴅᴇɴɢᴀɴ ᴍᴜᴅᴀʜ

🚀 ʙᴏᴛ ɪɴɪ ᴅɪᴋᴇᴍʙᴀɴɢᴋᴀɴ ᴏʟᴇʜ  
<a href="tg://openmessage?user_id={OWNER_ID}">
<b>@YUKALASTERA</b>
</a>

<b>𝐂𝐚𝐫𝐚 𝐒𝐞𝐰𝐚 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 :</b>

<b>Untuk menyewa userbot,</b>  
<b>silakan menekan tombol</b>  
<b>"Buat Userbot".</b>

<b>Jika belum melakukan transaksi,</b>  
<b>silakan memilih menu</b>  
<b>"Beli Userbot".</b>

<b>Selanjutnya, pilih masa aktif</b>  
<b>sesuai dengan hari atau bulan</b>  
<b>yang diinginkan.</b>

<b>Setelah itu, lakukan</b>  
<b>pembayaran sesuai</b>  
<b>instruksi yang tersedia.</b>

<b>Tunggu proses verifikasi</b>  
<b>dari admin.</b>

<b>Jika verifikasi telah selesai,</b>  
<b>Anda dapat menikmati</b>  
<b>layanan userbot kami.</b>

<b>Userbot ini sedang dalam tahap</b>  
<b>pengembangan.</b>

<b>Jika Anda ingin membeli userbot</b>  
<b>atau menjadi reseller,</b>  
<b>silakan menghubungi owner utama.</b>

<b>ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪʙᴀᴡᴀʜ</b>  
<b>ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ</b>
</blockquote>
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
            return "<b>❌ Userbot tidak ditemukan</b>"

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