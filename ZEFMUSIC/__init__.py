import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import test configuration
import config

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

from ZEFMUSIC.core.mongo import mongodb
from ZEFMUSIC.core.call import ZEFMUSICCall
from ZEFMUSIC.misc import sudo
from ZEFMUSIC.utils import time_to_seconds
from ZEFMUSIC.utils.database import get_db
from ZEFMUSIC.utils.decorators import language
from ZEFMUSIC.utils.extraction import extract_user
from ZEFMUSIC.utils.formatters import get_readable_time
from ZEFMUSIC.utils.inline import help_pannel, play_pannel
from ZEFMUSIC.utils.inlinequery import inline_query
from ZEFMUSIC.utils.pastebin import paste
from ZEFMUSIC.utils.stream import stream
from ZEFMUSIC.utils.thumbnails import get_thumb
from ZEFMUSIC.utils.ytdl import ytdl
