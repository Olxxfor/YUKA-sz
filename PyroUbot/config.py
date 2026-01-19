import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "7966814831").split()))

API_ID = int(os.getenv("API_ID", "29162625"))

API_HASH = os.getenv("API_HASH", "78456921dac89a0e056f844af35935a1")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8424405702:AAHkOO2aWC4akb-PwN8oNg4cu_pFiHvAZaA")

OWNER_ID = int(os.getenv("OWNER_ID", "7966814831"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002344868631").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://junofficial354:junofficial354@cluster0.9hz9uub.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", " -1002344868631"))
