import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

# Читаем переменную DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./bank.db")