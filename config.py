"""
VC Music Player, Telegram Voice Chat Userbot
Copyright (C) 2021  ZauteKm <https://telegram.dog/ZauteKm>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "https://youtu.be/7zLgZdKAOgg")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '1847068212 1819814100 1907409985')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", '2749695'))
    CHAT = int(os.environ.get("CHAT", "-1001415962984"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "-1001543935568")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "N")
    ARQ_API=os.environ.get("ARQ_API", "ACKJQI-ZBQAKY-DLUJBU-ORWEPW-ARQ")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    EDIT_TITLE = os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "NO":
        EDIT_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 200))
    DELAY = int(os.environ.get("DELAY", 10))
    API_HASH = os.environ.get("API_HASH", "55ce46fea3a9b1b1f086a0748e9f9dd7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1884261620:AAF9ssJ0vB3_TwGExJ6yj-1Te67ILIbBEIU") 
    SESSION = os.environ.get("SESSION_STRING", "AQDDC7p0tcdf4-9ET3g8xY7BuywnUvyPzJHg35l-o8SSUnIejHmixCC2nqHpI4JNkhiPUv8OwwBWbaJArLyR5SbTslnrQ9Ct5o7x1BNJ1FDnTFqS_c-bljgBXKDuREeHtFXSx3T8o6H1vMFuuyk_DeP4GrQWkA7C87YRThKQeYRc_-IF10SdkjTaojRfdpkzCOAAflPlTw1OGeFpREkNNGEc7aJMwqgO0uhTwURj3kq8GRXfUdmoOnI1M115Esk86wYJQYK1ezMrLWb5nF5JProymEllOrA2raYzdsoOszKGOga3lzNNY7QLaGbL3Zftjt447UhImx-_VC-vKCIS3yo2a9OHQgA")
    playlist=[]
    msg = {}
