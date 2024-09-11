from secret import DOWNLOAD_SPEED, UPLOAD_SPEED
from internet_speed_twitter_bot import InternetSpeedTwitterBot

speedBot = InternetSpeedTwitterBot()

speedBot.get_internet_speed()

if speedBot.down < DOWNLOAD_SPEED or speedBot.up < UPLOAD_SPEED:
    speedBot.tweet_at_provider()