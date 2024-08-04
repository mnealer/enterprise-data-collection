from dotenv import find_dotenv, dotenv_values
import pathlib
import string


file_path = pathlib.Path().cwd()
static_dir = str(pathlib.Path(pathlib.Path().cwd(), "static"))
config = dotenv_values(find_dotenv(".test_fastapi_config.env"))

db_user = config.get("DB_USER")
db_password = config.get("DB_PASSWORD")
db_host = config.get("DB_HOST")
db_name = config.get("DB_NAME")
db_port = config.get("DB_PORT")
db_url = f"asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
db_modules = {"datacollector": ["auth.models"]}

max_age = 3600

session_choices = string.ascii_letters + string.digits + "=+%$#"


