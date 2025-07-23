import datetime
from connection import collections
from pymongo.errors import ConnectionError, DuplicateKeyError

class CollectionController:
    def __init__(self):
        try:
            self.collection = collections

        except ConnectionError as e:
            print(f"Failed to connect to MongoDB: {e}")
            raise

    async def create_collection(self, name: str, description: str) -> bool:
        try:
            self.collection.insert_one({
                "name": name.strip(),
                "desc": description,
                "created_at": datetime.utcnow()
            })
            print(f"Created collection '{name}'")
            
            return True
        except DuplicateKeyError:
            print(f"Duplicate collection name '{name}'")
            return False
        except Exception as e:
            print(f"Error creating collection: {e}")
            raise

    async def get_collections(self, ) -> list[dict]:
        try:
            collections = list(self.collection.find())
            
            return collections
        except Exception as e:
            print(f"Error retrieving collections: {e}")
            raise

    async def get_collection(self, name: str) -> dict:
        try:
            collection = self.collection.find_one({"name": name})
            
            return collection
        except Exception as e:
            print(f"Error retrieving collection '{name}': {e}")
            raise

    async def update_collection(self, old_name: str, new_name: str) -> bool:
        try:
            result = self.collection.update_one(
                {"name": old_name},
                {"$set": {"name": new_name.strip(), "updated_at": datetime.utcnow()}}
            )
            
            if result.modified_count > 0:
                print(f"Updated collection '{old_name}' to '{new_name}'")
                return True
            print(f"Collection '{old_name}' not found")
            
            return False
        except DuplicateKeyError:
            print(f"Duplicate collection name '{new_name}'")
            
            return False
        except Exception as e:
            print(f"Error updating collection: {e}")
            raise

    async def delete_collection(self, name: str) -> bool:
        try:
            result = self.collection.delete_one({"name": name})
            
            if result.deleted_count > 0:
                print(f"Deleted collection '{name}'")
                return True
            print(f"Collection '{name}' not found")
            
            return False
        except Exception as e:
            print(f"Error deleting collection '{name}': {e}")
            raise

    def close(self):
        self.client.close()