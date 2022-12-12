from tg_bot.sample_config import Config

class Development(Config):
    OWNER_ID = 1659580762  # my telegram ID
    OWNER_USERNAME = "Gbotid"  # my telegram username
    API_KEY = "5862381673:AAFcmBM8sz6l-Ojc7gADdFr6m_nxwwCTBNQ"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:svLbmtihf65NIiz0B4UX@containers-us-west-155.railway.app:5476/railway'  # sample db credentials
    MESSAGE_DUMP = '-1001839097484' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [18673980, 83489514]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
