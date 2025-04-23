from os import getenv

from dotenv import load_dotenv

load_dotenv()

api_id = int(getenv("api_id", "26913421"))
api_hash = getenv("api_hash", "9b7c98742c17d8f7a6a3fa700284f4d6")
session = getenv("session", "BQGaqo0ACzmBxnO0pu9JfM0lAT2jfvpX_AZ46qqPkNRyXN4rBRStDGVhbgFM4GShzPJYQDx06Fw3U5KbtkJO_MAqPRycOs659WHVz3ORWIm8LU9OzGruXpYLlfTBj7MX_1wEDdXfoJ1B3re7z13tVRjB0X8uAwi9x02TkwD5Iej8V3lVz_p-02OCUnzbTZqNw2QSlZfV1EHxRuLmt9c6R6Hk_OPOcSgxXLEWx4G8r4L_5pllN7QkjTM495d2aUcGKKN8vG068DTPlfGJqosv8A95iMMo9W_fXu_ugbVkupbNOERVgnK0HmfiCHqS1QAjKKePPhmAuzP8tJ2WoBPrdc8QjPgItwAAAAEyyZkdAA")
bot_token = getenv("bot_token", "7785094383:AAFNPRy6SeJcDFArAAS2161C42IMIQOA56E")
db_name = getenv("db_name", "zii")
mongo_uri = getenv("mongo_uri", "mongodb+srv://ziobot:1234@cluster0.cj2dp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
def_bahasa = getenv("def_bahasa", "toxic")
log_pic = getenv("log_pic", "https://files.catbox.moe/pcrvfl.jpg")
heroku_api = getenv("heroku_api")
heroku_app_name = getenv("heroku_app_name")
upstream_repo = getenv(
    "upstream_repo",
    "https://github.com/lusiap/kaelbot24",
)
upstream_branch = getenv("upstream_branch", "final")
git_token = getenv("git_token", None)
log_channel = getenv("log_channel", None)
genius_api = getenv(
    "genius_api",
    "zhtfIphjnawHBcLFkIi-zE7tp8B9kJqY3xGnz_BlzQM9nhJJrD7csS1upSxUE0OMmiP3c7lgabJcRaB0hwViow",
)
# scheme = getenv("scheme", None)
# hostname = getenv("hostname", None)
# port = int(getenv("port", None))
# username = getenv("username", None)
# password = getenv("password", None)
