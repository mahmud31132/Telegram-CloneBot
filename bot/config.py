

BOT_TOKEN = "1732637881:AAHsXbOhVe-Pi_hOxL4NzEBRg7gY4fPSVyE"
GDRIVE_FOLDER_ID = "12mC7czBa25dW_dnJ5uH1BSXsxgQ-3zBa"
# Default folder id.
OWNER_ID = 1042447527
# Example: OWNER_ID = 1042447527
AUTHORISED_USERS = [63055333,100483029,-1003943959]
# Example: AUTHORISED_USERS = [63055333, 100483029, -1003943959]
INDEX_URL = "https://mirror.mahmud-bot.workers.dev/0:/"
IS_TEAM_DRIVE = True
USE_SERVICE_ACCOUNTS = True
# --------------------------------------

# dont edit below this >



BOT_TOKEN = os.environ.get('BOT_TOKEN', BOT_TOKEN)
GDRIVE_FOLDER_ID = os.environ.get('GDRIVE_FOLDER_ID', GDRIVE_FOLDER_ID)
OWNER_ID = int(os.environ.get('OWNER_ID', OWNER_ID))
AUTHORISED_USERS = json.loads(os.environ.get('AUTHORISED_USERS', json.dumps(AUTHORISED_USERS)))
INDEX_URL = os.environ.get('INDEX_URL', INDEX_URL)
IS_TEAM_DRIVE = stb(os.environ.get('IS_TEAM_DRIVE', str(IS_TEAM_DRIVE)))
USE_SERVICE_ACCOUNTS = stb(os.environ.get('USE_SERVICE_ACCOUNTS', str(USE_SERVICE_ACCOUNTS)))
