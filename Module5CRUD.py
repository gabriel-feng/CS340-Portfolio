from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:47587/AAC' % (username, password))
        # where xxxxx is your unique port number
        self.database = self.client['AAC']
        print("Connected Properly")

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if type(data) is dict:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD.
    def read(self, data):
        if type(data) is dict and data is not None:
            result = self.database.animals.find(data, {'_id': False})
            return result
        else:
            raise Exception("No results found")

# Create method to implement the U in CRUD.
    def update(self, data, newData):
        if type(data) is dict and type(newData) is dict and data is not None and newData is not None:
            updateData = {"$set" : newData}
            self.database.animals.update_one(data, updateData)
            print("Successfully updated")
            result = self.database.animals.find(newData)
            return result
        else:
            raise Exception("No results found")

# Create method to implement the D in CRUD.
    def delete(self, data):
        if type(data) is dict and data is not None:
            self.database.animals.delete_one(data)
            print("Successfully deleted")
            return True
        else:
            raise Exception("No results found")