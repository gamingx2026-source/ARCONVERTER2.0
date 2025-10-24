

from os import environ

API_ID = int(environ.get("API_ID", "29754330"))
API_HASH = environ.get("API_HASH", "6d58372712767f434c30ecfa3cb1951e")
BOT_TOKEN = environ.get("BOT_TOKEN", "8171758201:AAFJESOkn59rNi7NjmALEK-1UCS1HAV-6Rs")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "ARCONVERTER")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "ARCONVERTER")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "7052558926").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "7052558926"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")





