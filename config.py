import motor.motor_asyncio

MONGODB_URL = 'mongodb://localhost:27017/test'

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

#connect to database name

#database = client.python_db

database = client.test