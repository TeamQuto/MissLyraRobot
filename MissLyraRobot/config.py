# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "6435225"  
    API_HASH = "4e984ea35f854762dcde906dce426c2d"
    TOKEN = "1240287427:AAFGwboI9iu83vKxDPIdPT0N1HVtXZm5uSc"
    OWNER_ID = "936481432"
    OWNER_USERNAME = "XeD_NitriC"
    MONGO_DB_URI = "mongodb+srv://Nitric:Nitric@cluster0.plap4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    MONGO_DB = "MissLyraRobot"
    SUPPORT_CHAT = "XCodeSupport"
    JOIN_LOGGER = "-1001774935713"
    EVENT_LOGS = "-1001774935713"
    ERROR_LOG = "-1001774935713"

    # RECOMMENDED
    INFOPIC = "https://telegra.ph/file/73337f3406d18b80a2683.jpg"   
    CF_API_KEY = ""
    LASTFM_API_KEY = ""
    BOT_USERNAME = "MissLyraRobot"
    WALL_API = ""
    OPENWEATHERMAP_ID = ""
    TEMP_DOWNLOAD_DIRECTORY = ""
    REM_BG_API_KEY = ""
    TIME_API_KEY = ""
    CASH_API_KEY = ""
    REM_BG_API_KEY = ""
    ARQ_API_KEY = "UIUXOY-NTKWDC-QHFFMD-DHHKVV-ARQ"
    ARQ_API = "UIUXOY-NTKWDC-QHFFMD-DHHKVV-ARQ"
    ARQ_API_URL = "aww"
    HEROKU_APP_NAME = ""
    HEROKU_API_KEY = ""
    BOT_ID = "1901951380"
    STRING_SESSION = "1BVtsOJsBu6ApoSjs00-4Gk0Z2iINDhinQOi_HZnedKddpSkbZrqiRL-xr6MPreYXJ8TvU46VxV2A9uPWjJGmtZBwJn6dEWTB23x0UJGbDwDnIrXqHyboWCSsfe0xQJAqVYvZUB0v0JZVNNpp_RUqw7Y7CRLvkXg8kw-IDv_hJcR1nnYIucxpF4Bc_0kjmroNaO4Qwn2Ci-9r5j86MKCUwkGJO3r8rEeDArGrFgOy5KYex_x5w-K8FK2Gm8HKVvWphFDCb7yf57n15qFKGPbnSENfeudlubK7Ei4S8LwIDyrpQokOLnK6C3s1-adZgrBFOO9l8B2EikY-aoBLCbIkncuMs4IsLqM="
    SESSION_STRING = "1BVtsOJsBu6ApoSjs00-4Gk0Z2iINDhinQOi_HZnedKddpSkbZrqiRL-xr6MPreYXJ8TvU46VxV2A9uPWjJGmtZBwJn6dEWTB23x0UJGbDwDnIrXqHyboWCSsfe0xQJAqVYvZUB0v0JZVNNpp_RUqw7Y7CRLvkXg8kw-IDv_hJcR1nnYIucxpF4Bc_0kjmroNaO4Qwn2Ci-9r5j86MKCUwkGJO3r8rEeDArGrFgOy5KYex_x5w-K8FK2Gm8HKVvWphFDCb7yf57n15qFKGPbnSENfeudlubK7Ei4S8LwIDyrpQokOLnK6C3s1-adZgrBFOO9l8B2EikY-aoBLCbIkncuMs4IsLqM="
    SQLALCHEMY_DATABASE_URI = "postgres://xkncmhpw:9f1Z_dF2OMcgWejkDDsJuaPq4MdkSu5u@lallah.db.elephantsql.com/xkncmhpw"
    DATABASE_URL = "postgres://xkncmhpw:9f1Z_dF2OMcgWejkDDsJuaPq4MdkSu5u@lallah.db.elephantsql.com/xkncmhpw"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = "1669178360"
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = "1669178360"
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = "1669178360"
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = "1669178360"
    WOLVES = "1669178360"
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    ALLOW_CHATS = True
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
