from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

async def get_persona_by_cedula(cedula: str):
    return await collection.find_one({"cedula": cedula})