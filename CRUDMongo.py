#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pymongo import MongoClient, errors
from bson.objectid import ObjectId
import json

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""
    
    def __init__(self, user, password, host, port, db, collection,    auth_source='admin'):
        """" Crud Operations for Animal collections in MongoDB """
         # Initialize the MongoClient
        self.client = MongoClient(
                host=host,
                port=port,
                username=user,
                password=password,
                authSource=auth_source,
                authMechanism="SCRAM-SHA-256"
            )
        # Initialize Connection
        #
        try:
            self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}')
            self.database = self.client[db]
            self.collection = self.database[collection]
            print("Connected")
        except errors.ConnectionError as e:
            print(f"Could not connect to {e}")
        
    # Complete this method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                insert_result = self.collection.insert_one(data) 
                return True #returns true if successful
            except errors.PyMongoError as e:
                print(f'Unable to create {e}')
                return False
        else:
            raise ValueError("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            try:
                cursor = self.collection.find(query)
                data = list(cursor)
                return data
            except errors.PyMongoError as e:
                print(f"Error with {e}")
                return []
            
        else:
            raise ValueError("Empty query")
            
     # create the U in CRUD (update)           
    def update(self, query, newData):
        if query is not None:
            try:
                result = self.collection.update_many(query, {"$set": newData})
                return result.raw_result # returns how many were updated
            except errors.PyMongoError as e:
                print(f'Error with {e}')
                return []
        else:
            return []
        
    # create a delete method (D in CRUD)
    def delete(self, query):
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.raw_result #returns how many were deleted
            except errors.PyMongoError as e:
                print(f'Error with {e}')
                return []
        else:
            return []
        
        
                      
        

