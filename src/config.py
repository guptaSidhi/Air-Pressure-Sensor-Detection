import os 
import pymongo
from dataclasses import dataclass

from dotenv import load_dotenv
load_dotenv()

@dataclass
class EnvironmentVarible:
    mongo_db_url: str = os.getenv("MONGO_DB_URL")

env_var = EnvironmentVarible()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)

print(f"MongoDB URL: {env_var.mongo_db_url}")