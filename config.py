import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "18335748")) #optional
API_HASH = getenv("API_HASH", "01cdb99a00d9cd7610d992f655ffe97a") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5823310311").split()))
OWNER_ID = int(getenv("OWNER_ID", "5823310311"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://suhana:suhana@cluster0.2r604ar.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5974465653:AAGTIoawYwSsTA1eKLFZtgBvHkUzz_Tel9c")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAxb8ITt9mX-R0z72oqyJ8G_57WXd4dm-MzsMZgDuZj0X-WTeVcpmSGoEBg4iYTG7nddRas7LrRHh9NWc_zmO8JOhfO0T8dRo4ZTJqlbb9aDdoyDUpBsqtdMmUk6_0MnYPXYPrzgJnq1WUQNzue9T8SLfVQVqT8HDg5QQmqHeL4yJ43W-jndSBwqhtZgSn5rQsiBwZ3TW6Xtd6PbI-se3sondVcHWWpCTfCBmI3uSET4ANhZeMsOF-agdXsfxmxkvf4s9PyJIaf7oeva0Btd7F5ubmbWpmFvhhNr9pTMibpSRP1lP2mwZ_lVpN4Z3rUKhZdsrwZaQ42v6dPz0PhxZg1wAAAAFbGKnnAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
