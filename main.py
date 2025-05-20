from internetspeedtwitterbot import InternetSpeedTwitterBot
import os

PROMISED_RATES = {"Up": 15, "Down": 125}
TWITTER_USERNAME = os.environ.get("TWITTER_USERNAME")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

if int(bot.upload_speed) < PROMISED_RATES["Up"] or int(bot.download_speed) < PROMISED_RATES["Down"]:
    bot.tweet_at_provider(TWITTER_USERNAME, TWITTER_PASSWORD)
