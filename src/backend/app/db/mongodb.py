from pymongo import MongoClient
from pymongo.collection import Collection


class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.database = self.client[db_name]

    def get_collection(self, collection_name: str) -> Collection:
        return self.database[collection_name]

    def get_database(self):
        return self.database

    def close(self):
        self.client.close()
