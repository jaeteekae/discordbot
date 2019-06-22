import secret
import os

TOKEN = secret.TOKEN
LC_CHANNEL_ID = secret.LC_CHANNEL_ID
RECEIPTS_CHANNEL_ID = secret.RECEIPTS_CHANNEL_ID
PREFIX = "!"

DATA_FOLDER = "data"

AWAY_FILE = os.path.join(DATA_FOLDER,"away.json")
AWAY_COLOR = 0x72FF7B

BDAY_FILE = os.path.join(DATA_FOLDER,"bdays.json")
BDAY_COLOR = 0x494ce5

GIF_FILE = os.path.join(DATA_FOLDER,"gif_shortcuts.json")
GIF_FOLDER = "gifs"
GIF_COLOR = 0xa175c4

LINKS_FILE = os.path.join(DATA_FOLDER,"gen_links.json")

STATS_FILE = os.path.join(DATA_FOLDER,"stats.json")