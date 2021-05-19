from dotenv import load_dotenv
from src import AlkBot
from os import getenv


# Load environment variables.
load_dotenv()

# Instanciate and bootstrap the Alkbot and its commands.
alkbot = AlkBot()

# Finally, start the bot by giving the token.
alkbot.run(getenv('TOKEN'))
