import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
if os.path.exists("Internal"):
    load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
admins = {}
que = {}

API_ID = int(getenv("API_ID", "11822563"))
API_HASH = getenv("API_HASH", "12bfd8057541544a482312319d7fe4ae")
BOT_TOKEN = getenv("BOT_TOKEN", "6687927759:AAHASknO5Z0atFRs67Z9EyvvX9BnFguKoEs")
STRING_SESSION = getenv("STRING_SESSION", "BAB3G-aJDgUBS69mGHlLqd2xCxeYM_iLl80eE_JhfKsPF2wzKKqVYK62_G-w4sMT5KGrzDQ4UP0FDNIXcZ2kWpoZaYU94zKYpnFrr-GBktCC2UUWspzLOO23X4zjW9XerJRVrwInNWNH1X61uDWxA7gtK6qgRjLCyc4qOGvWuUFwdP2g_Tx-Jcdkv1xdzaxQwSacO8OXZ3qUoSAH1kX0M7ToxW-v_6b3Y763kewfIuOlNgBbfYltvyXMaWKVdm9wIsv1hMbvB0hrLuRTQUn83iOzcFNEd0Mb5YQjZ4NJTeQjqbnpf6C0ALKI_R-eVnWaLmDXMxaGPCGmvDsvfl9I495vAAAAAUr8w8oA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ".").split())
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://yipilev790:yipilev790@cluster0.dtfedu0.mongodb.net/")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5553046474").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001905044159"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5553046474").split()))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/XdityaHalder/Genius-Userbot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "aditya")
