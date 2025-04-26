import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import test configuration
import test_config as config

from ZEFMUSIC.core.bot import KINGBot
from ZEFMUSIC.core.dir import dirr
from ZEFMUSIC.core.git import git
from ZEFMUSIC.core.userbot import Userbot
from ZEFMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = KINGBot()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
