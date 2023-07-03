import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "23737933"))
API_HASH = getenv("API_HASH", "de913d82c5e0cfdcdc08313c49304ae3")

BOT_TOKEN = getenv("BOT_TOKEN", "6139173699:AAEDPkAEOSMhUjg1QcrQER-Cu4X7u2Qxv4g")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://vibadef654:vibadef654@cluster0.xb6gmqo.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001969560344"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "─‌⃜𓆩ᴛ¢s 𝙓 𝐌υѕι¢𓆪ꭗ‌")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5665115127 5655799578").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Raichuop07/tcs")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", "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")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/about_tcs")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/tcs_chatting_hub_forever")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "5363619fbddd46bb80021085e46c620e")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "5d3180c8869847cebc15dab2a2586b90")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQBBLOcq-iopRcxa8fW7NZMXktmJIVCQrHMlJpYIZEjuvMgMpzIX0HYCqSSdvQtMzp134EEoDHMOYEcFE8QK8WEbihvZXuwYsLCBhuRtCS7fyniGotP4soH1YyrtNHYd3yeMFbnwtTCsDHFonCjVp9s447OX4fTeyGCklZTF8Hit8iVFKWNKLF9cYsQj7_rN04bknXZLQr9doTYIt0_lejZ8-mjAkXIBXoWNHyHYD4geNEcq9Zcy6yJXcPmSDTBLp74slX709WCJm15NCGy1RaMDc2K98yt1QOL-o5fNt838fUCcTrLSbZkulKbw2kW86iJxBVOGDbSBtbZZaunR_kSWAAAAAXInMzsA")
STRING2 = getenv("STRING_SESSION2", "BQBiu2eohqCXhvof55thF9AmFxbxEuS5QP0DVGmCSxEazumqvvTYrzfYnwUrgO8g6wG3dju4BOx3CVAHMjwKmp243-8YwRNhOZm_Lk5yeYK7ihTE2IfO5L29uGDItNO2fZ156JKTTvaqSqu7fwuLikK9dW8GTcZgOURAFe-xAZbuUbwCkSAijpWB4EGMgcyvldxaFCeNnG_-9gJqBr2J7F3q-8lPCGhY7tybZcOhLXVHl3o8PD365TM9FA4R2XKS2JHMuxAli0CW-QyJB1D4u24EZORQk8_gHVpEepaGDDrgYAUFpLP4COiA53SCUl0bIbvOo3CbrEZrHv_kZk1icfnsAAAAAXvVDmkA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/43888c2da0aed225b7c80.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/e49615f925591ad47f279.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://te.legra.ph/file/e49615f925591ad47f279.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/43888c2da0aed225b7c80.jpg"
