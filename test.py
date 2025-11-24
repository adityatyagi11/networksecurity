import pymongo, certifi, os
from dotenv import load_dotenv

load_dotenv()
client = pymongo.MongoClient(os.getenv("MONGO_DB_URL"), tls=True, tlsCAFile=certifi.where())

print(client.list_database_names())
