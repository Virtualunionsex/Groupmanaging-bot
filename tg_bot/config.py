from tg_bot.sample_config import Config

class Development(Config):
    OWNER_ID = 1715348447  # my telegram ID
    OWNER_USERNAME = "cyellaku"  # my telegram username
    API_KEY = "5851945481:AAHyxkGMsxi0bOipQSJmcZTHv6tbabFu_UU"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://pfewsazv:NFJuP00vvb9dup3vS8jzp0ZpNYusWXtS@raja.db.elephantsql.com/pfewsazv'  # sample db credentials
    MESSAGE_DUMP = '-1001729142523' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1715348447, 1908660708]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
