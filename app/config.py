import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")
CEDULA_MIN_LENGTH = int(os.getenv("CEDULA_MIN_LENGTH", 6))
CEDULA_MAX_LENGTH = int(os.getenv("CEDULA_MAX_LENGTH", 15))