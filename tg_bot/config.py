from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1659580762  # my telegram ID
    OWNER_USERNAME = "Anandus"  # my telegram username
    API_KEY = "5862381673:AAFcmBM8sz6l-Ojc7gADdFr6m_nxwwCTBNQ"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:EmtEQRAdBOrAu1echnbj@containers-us-west-146.railway.app:7654/railway'  # sample db credentials
    MESSAGE_DUMP = '-1001881422749' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1659580762, 5166575484]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
