import os
from PyroUbot import *
import requests

__MODULE__ = "ᴘʟᴀʏʙᴜᴛᴛᴏɴ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʟᴀʏʙᴜᴛᴛᴏɴ ⦫</b>
<blockquote><b>
⎆ ᴘᴇʀɪɴᴛᴀʜ :
ᚗ <code>{0}ytgold</code>
⊷ untuk membuat gold playbutton youtube

ᚗ <code>{0}ytsilver</code>
⊷ untuk membuat silver playbutton youtube

ᚗ <code>{0}iggold</code>
⊷ untuk membuat gold playbutton youtube

ᚗ <code>{0}igsilver</code>
⊷ untuk membuat silver playbutton youtube

ᚗ <code>{0}fbgold</code>
⊷ untuk membuat gold playbutton youtube

ᚗ <code>{0}fbsilver</code>
⊷ untuk membuat silver playbutton youtube

ᚗ <code>{0}twgold</code>
⊷ untuk membuat gold playbutton youtube

ᚗ <code>{0}twsilver</code>
⊷ untuk membuat silver playbutton youtube

"""

def tweet(text):
    url = "https://api.botcahx.eu.org/api/ephoto/twtsilverbutton"
    params = {
        "text": text,
        "apikey": "moire"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
def tweets(text):
    url = "https://api.botcahx.eu.org/api/ephoto/twtgoldbutton"
    params = {
        "text": text,
        "apikey": "moire"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None        
def fb(text):
    url = "https://api.botcahx.eu.org/api/ephoto/fbsilverbutton"
    params = {
        "text": text,
        "apikey": "moire"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
        
def fbs(text):
    url = "https://api.botcahx.eu.org/api/ephoto/fbgoldbutton"
    params = {
        "text": text,
        "apikey": "moire"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
        
def robott(text):
    url = "https://api.botcahx.eu.org/api/ephoto/ytsilverbutton"
    params = {
        "text": text,
        "apikey": "moire"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
        
def robottt(text):
    url = "https://api.botcahx.eu.org/api/ephoto/igsilverbutton"
    params = {
        "text": text,
        "apikey": "moire"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
def robotttg(text):
    url = "https://api.botcahx.eu.org/api/ephoto/iggoldbutton"
    params = {
        "text": text,
        "apikey": "moire"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None                    
def horor(text):
    url = "https://api.botcahx.eu.org/api/ephoto/ytgoldbutton"
    params = {
        "text": text,
        "apikey": "moire"
    }                       
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None

# YOYTUBE        
@PY.UBOT("ytgold")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply("<blockquote>contoh : .ytgold moire</blockquote>")
        return

    request_text = args[1]
    await message.reply("<blockquote>sedang memproses, mohon tunggu...</blockquote>")

    image_content = horor(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply("<blockquote>apikey sedang bermasalah</blockquote>")
                              
@PY.UBOT("ytsilver")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply("<blockquote>contoh : .ytsilver moire</blockquote>")
        return

    request_text = args[1]
    await message.reply("<blockquote>sedang memproses, mohon tunggu...</blockquote>")

    image_content = robott(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply("<blockquote>apikey sedang bermasalah</blockquote>")
  
# INSTAGRAM                                
@PY.UBOT("iggold")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply("<blockquote>contoh : .iggold moire</blockquote>")
        return

    request_text = args[1]
    await message.reply("<blockquote>sedang memproses, mohon tunggu...</blockquote>")

    image_content = robotttg(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply("<blockquote>apikey sedang bermasalah</blockquote>")
                                  
@PY.UBOT("igsilver")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply("<blockquote>contoh : .igsilver moire</blockquote>")
        return

    request_text = args[1]
    await message.reply("<blockquote>sedang memproses, mohon tunggu...</blockquote>")

    image_content = robottt(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply("<blockquote>apikey sedang bermasalah</blockquote>")

# FACEBOOK                                   
@PY.UBOT("fbsilver")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply("<blockquote>contoh : .fbsilver moire</blockquote>")
        return

    request_text = args[1]
    await message.reply("<blockquote>sedang memproses, mohon tunggu...</blockquote>")

    image_content = fb(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply("<blockquote>apikey sedang bermasalah</blockquote>")

@PY.UBOT("fbgold")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply("<blockquote>contoh : .fbgold moire</blockquote>")
        return

    request_text = args[1]
    await message.reply("<blockquote>sedang memproses, mohon tunggu...</blockquote>")

    image_content = fbs(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply("<blockquote>apikey sedang bermasalah</blockquote>")

# TWITTER
@PY.UBOT("twtsilver")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply("<blockquote>contoh : .twtsilver moire</blockquote>")
        return

    request_text = args[1]
    await message.reply("<blockquote>sedang memproses, mohon tunggu...</blockquote>")

    image_content = tweet(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply("<blockquote>apikey sedang bermasalah</blockquote>")

@PY.UBOT("twtgold")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply("<blockquote>contoh : .twtgold moire</blockquote>")
        return

    request_text = args[1]
    await message.reply("<blockquote>sedang memproses, mohon tunggu...</blockquote>")

    image_content = tweets(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply("<blockquote>apikey sedang bermasalah</blockquote>")
 