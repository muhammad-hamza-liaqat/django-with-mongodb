from mongoengine import connect
from urllib.parse import urlparse
from decouple import config

def connect_to_mongo():
    try:
        uri = config("MONGODB_URI")  
        db_name = config("DB_NAME")  
        host = urlparse(uri).hostname  

        connect(
            db=db_name,
            host=uri
        )
        print(f"Connected to MongoDB successfully at host: {host}")
    except Exception as e:
        print(f"Failed to connect to MongoDB at host: {host}. Error: {e}")
