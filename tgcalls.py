import config
from pyrogram import Client

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
