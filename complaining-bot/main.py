from complaining_bot import ComplainingBot

bot = ComplainingBot()
measured_speed_params = bot.get_internet_speed()
bot.tweet_at_provider(measured_speed_params)
