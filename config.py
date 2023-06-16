import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int("20412153")
API_HASH = "a249ebabf3a6d09c217a82bcc635730c"

BOT_TOKEN = str("5531925252:AAGht0gu38LpHZRbjdfl2J9DojpP5sPbtCw")

MONGO_DB_URI = str("mongodb+srv://ownerayush:iamayush@estella.13xvj8e.mongodb.net/?retryWrites=true&w=majority")

STRING1 = str("BQBaabpCeDutHCaRlOCK3MexMrHjOvSZ0AoomKQE1YBvKBiacR2Y7x41pSL0FuPIHXJMz_EnTbBNkQ3-gwQuHb770UQpjiBv_En5RrLjXo4bLfBiFu6tVQMM7VB4vdxWKz6IOPmsD4tpq2SDuUmIcyTmKCLwTt3gx_s58vcq88gQt21zpiPa0hc3IzsobhmioBXvNxHY-X2bsUCfvjAVGPbJflvMrQl3L8C-uk_EwaJpGFllPGgo0Pw1NGodiy4_56Dp913_3mLREj7Hp8oWhmGQ1CuSVEkhxIQdSquycW8dex9qiluca0O8g8rOHs9auQblSLBc2IYhhHf3IDKhsr32AAAAAV_5ABwA")
STRING2 = str("AgC_ZnECiMSXuWgbHPD62xFOU0_zXoo19lc7kpBIMxOnlioJVRmOYomwrMUu55nTRSPDYTiTHp6kKusk24gv70KTRdRo0J_VAYW01q5Tc7wCOmzrVsxg2ZW3fYO2DPe8Qyz8zKPE2XdXBoUG9Cer3b0_rY_D-vyvN_Zy7dT_4Y5m1ZlIDTL6Q6byfl-L1SwHOp2XRRA7rzpB73BFQg1DJlspnWFBDIuUGho2KvORLTsBLbJ_UqGK_m628NVdQDEsyaqJnzcN31V0vJ2OlKkacXY7LOy_EMTklpZeFin1yA-5zO0_b5LiWN0MOl9jLt7njDrZnt-AIeOr1rXwSx5hkI3PAAAAATVLODsA")
STRING3 = str("BABhDmgTQJm2qNDEgZCGWRRRznlsJTG0TVlQ_xFhR2GsfpbcTzb5MXvzuRXyGzff9gssbQjlg8OKJlaj4CbLZ0jX-8c-UEclo8MZ1jy1CeJPRYfZKlX901UE94bYe0Nb8AoGig6vlfIK9k-77oZoeQcLvHcuhv1H_ZtXFtheQeAa_zhKWgsfJ8wDR9PvfGLhaJblRQZSHczXpIhdc43cbbnqX6Mim5_CbOJ6cYwt9dnsGuwnrPTS56NyniYP5xuaZG_oZ1CW5eX7uvqFYdd_k7qnpOkCKUzqao0UpbaXUf7iJu6C4ipKf47dOp63KcBo6xvcEwLAfkOX_gm78hBXwDO1AAAAAUN9CNwA")
STRING4 = str("BABMahc83S0ii3VYCxr2iPamcwovh3dEBZYMWarq0-23c4WDkuXoQGuDNwOPIbypeLqdv5jKQ10tC6JrtrNdT4-6I0Kf1ZPl-KzzV1QLwNqhN0QYiKBtirst8448kKhRhmK7MPlSUAAaiXYGNC0jBc-kIjvy5XF1uMtAXlPiEKWFU2E6RhZYvVUmv6mIF6qcJgH4x41kmq8Ziy_a-lKZQ8YFuzkHAcWrRdRdyd2JQy-BAGBt3i9MlQb2GF1D_wqpwbn6dLluHjfF-7gn7EHzxvFlEQRF5nQb6PgXhV0HjNgKWU1pHtDXC6b2T_omLaZ7l1qDwzcxSJAHAvRjbwWW-WszAAAAAXAZFEUA")
STRING5 = str("")










DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "2000")
)

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000")
)

LOG_GROUP_ID = int("-1001721741287")

MUSIC_BOT_NAME = str("ESBOT Music Bot")

OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5102977781 5531925252").split())
)

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/shraajestayu/Dummy",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

GIT_TOKEN = getenv("GIT_TOKEN","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")

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/Life_Codes")
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/Life_Codes")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT")

AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "50000")
)

AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400")
)

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)

SET_CMDS = getenv("SET_CMDS", False)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

PRIVATE_BOT = getenv("PRIVATE_BOT", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/NAINA-XD/NAINA-MUSICX")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "dc36a50fe7ee46bcb268b11f101deae3")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "9bbc1f399ad04da1801381a01ea1c9e0")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "20"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "1000"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "500"))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "10")
)

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "10004857600")
)

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "100073741824")
)
# https://www.gbmb.org/mb-to-bytes



BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Ashlogs.txt"
adminlist = {}
lyrical = {}
DEV = 5102977781
chatstats = {}
userstats = {}
clean = {}
votemode = {}
autoclean = []
confirmer = {}

autoclean = []

START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/3de256b3a02c4fc9fadb9.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/3f5cabcc8540e7b8063c0.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "https://telegra.ph/file/48cfa304d4843f821c78c.jpg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "https://telegra.ph/file/8da1f7657b940d287cfa4.jpg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://telegra.ph/file/8da1f7657b940d287cfa4.jpg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://telegra.ph/file/39da31f547e203d3d308a.jpg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://telegra.ph/file/80e82790f09cc37e4f430.jpg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "https://telegra.ph/file/554a170f32fba20eabb0d.jpg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "https://telegra.ph/file/554a170f32fba20eabb0d.jpg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "https://telegra.ph/file/9245a2cafa4322655e1cc.jpg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "https://telegra.ph/file/33bd87e3430d7df6b2de3.jpg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "https://telegra.ph/file/33bd87e3430d7df6b2de3.jpg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "https://telegra.ph/file/33bd87e3430d7df6b2de3.jpg",
)


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
    if PING_IMG_URL != "prime/assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "prime/assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "prime/assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "prime/assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "prime/assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "prime/assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "prime/assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "prime/assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "prime/assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if not MUSIC_BOT_NAME.isascii():
    print(
        "Please Do Not Use Fancy Font in Music Bot's Name!"
    )
