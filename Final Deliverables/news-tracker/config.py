import os

from dotenv import load_dotenv

load_dotenv()

RAPID_API_KEY = os.getenv('RAPID_API_KEY')
API_URI = os.getenv('API_URI')
DB_URL = f'\
DATABASE={os.getenv("DATABASE")};\
HOSTNAME={os.getenv("HOSTNAME")};\
PORT={os.getenv("PORT")};\
SECURITY=SSL;\
SSLServerCertificate=DigiCertGlobalRootCA.crt;\
UID={os.getenv("UID")};\
PWD={os.getenv("PASSWORD")}'
SECRET_KEY = os.getenv('SECRET_KEY')