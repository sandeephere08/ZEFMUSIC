import os
from dotenv import load_dotenv

load_dotenv()

# Bot credentials
API_ID = int(os.getenv("API_ID", "11550139"))
API_HASH = os.getenv("API_HASH", "75080c7b5c6503ad1309a19e055f1524")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7680697190:AAGk1LWo6tlwOopZ10JOLwwHU4Zd_y6IWNQ")
STRING_SESSION = os.getenv("STRING_SESSION", "BQCwPbsAH5Yh_Pb4-L7Rrcv7lA9AhhYsV9J9uR2aa_pnNPwfh-1Ka_VMGhCsNDNKOsLdgoR3aZzaQ9rO24edu9VgwdwoeQXpYHQpu3CreiD_KnNrN7bF5zRGOXVTARBr9jsw3rb3YQiFdsul3iloa7d6fyFrmVoBRgVnAgl3CSoKF3a2tPsiV9JG3azmA11Abavj45oC5dbNKDYQOoon68kZJGomrrcH4XDDLAZ2m2Ej74fGDxNfd8h_aLJ6R8NZhvr70T6r3z06zMTKZiDanhsEtUeBRGjy6O1pAH-SIOWF-NMY0Re6_tXgux07UcBHKEaR6B7GYf2S8a8DTDIPGaiB_W7J-AAAAAHKofbkAA")

# Bot settings
DURATION_LIMIT = int(os.getenv("DURATION_LIMIT", "60"))
OWNER_ID = int(os.getenv("OWNER_ID", "7694579428"))
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "7694579428 1356469075").split()))

# Media settings
PING_IMG = os.getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = os.getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")
FAILED = os.getenv("FAILED", "https://te.legra.ph/file/4c896584b592593c00aa8.jpg")

# Support
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/zefronmusic")
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/ZEFRONAssociation")

# Bot name and username
BOT_NAME = "Radharani Music Bot"
BOT_USERNAME = "radharani_musicbot"

# MongoDB (using a dummy URI for testing)
MONGO_DB_URI = "mongodb+srv://test:test@cluster0.mongodb.net/test?retryWrites=true&w=majority"

# Logger ID (using a dummy ID for testing)
LOGGER_ID = -1001234567890 