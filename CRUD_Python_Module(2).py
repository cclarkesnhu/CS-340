# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId
from pymongo.errors import PyMongoError


class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser2' 
        PASS = 'Kappa' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Create Method in CRUD
    def create(self, data):
        if data is not None:
            try:
                result = self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"Error inserting document: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data is empty")

    # Read Method in CRUD
    def read(self, query): 
        if query is not None: 
            try:
                cursor = self.collection.find(query)
                result = list(cursor)
                return result
            except Exception as e:
                print(f"Error reading documents: {e}")
                return []
        else:
            raise Exception("Nothing to read because query is empty")
            
    # Update Method in CRUD   
    def update(self, query, newValue):
        if query is not None and newValue is not None:  
            try:
                result = self.collection.update_many(query, {"$set": newValue})  
                return result.modified_count
            except Exception as e:
                print(f"Error updating documents: {e}")
                return 0
        else:
            raise Exception("Unable to update because query and/or update data is empty")
    
    # Delete Method in CRUD
    def delete(self, query):
        if query is not None: 
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:  
                print(f"Error deleting documents: {e}")
                return 0
        else:
            raise Exception("Cannot delete because query is empty")  
            
            
class CRUD:
    def __init__(self, username, password, db_name="aac", collection_name="animals"):
        # This line must be indented inside __init__
        self.client = MongoClient(
            f"mongodb://{username}:{password}@127.0.0.1:27017/{db_name}?authSource={db_name}"
        )
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    
    def create(self, data):
        if data is not None:
            try:
                result = self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"Error inserting document: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data is empty")

    # Read Method in CRUD
    def read(self, query): 
        if query is not None: 
            try:
                cursor = self.collection.find(query)
                result = list(cursor)
                return result
            except Exception as e:
                print(f"Error reading documents: {e}")
                return []
        else:
            raise Exception("Nothing to read because query is empty")
            
    # Update Method in CRUD   
    def update(self, query, newValue):
        if query is not None and newValue is not None:  
            try:
                result = self.collection.update_many(query, {"$set": newValue})  
                return result.modified_count
            except Exception as e:
                print(f"Error updating documents: {e}")
                return 0
        else:
            raise Exception("Unable to update because query and/or update data is empty")
    
    # Delete Method in CRUD
    def delete(self, query):
        if query is not None: 
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:  
                print(f"Error deleting documents: {e}")
                return 0
        else:
            raise Exception("Cannot delete because query is empty")
