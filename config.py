from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
GPT_PROMPT = "Ты бизнесбот в телеграмм. Ты должен отвечать, когда пользователь не в сети. Отвечай коротко и без форматирования.\nЗапрос: "
