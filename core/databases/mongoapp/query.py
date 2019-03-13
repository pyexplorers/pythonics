'''
    Import modules to be used in the mongo related operations
'''
import pymongo
import core.databases.mongoapp.db_configs as db_configs
from core.databases.mongoapp.bases_db import Mongo_Database_base
from core.exceptions.def_exceptions import MongoDB_Exceptions_Connection,MongoDB_Exceptions_Records

'''
 A module to perform all mongodb related operations.
    1.) Insert 
    2.) Update
    3.) Delete
    4.) DB Connections and Related Objects
'''

class Mongo_Utils(Mongo_Database_base):
    '''
        Interact with mongo objects and return user required information
    '''
    @staticmethod
    def get_connection(server_name, server_port):
        '''
            Connect to MongoDB and return the connection object
            :param server_name: Server on which MongoDB is hosted
            :param server_port: Port on the Server where MongoDB is running
            @return:
                Success -> MongoDB Connection Object
                Exception -> Inform User that DB cant be reached
        '''
        try:
          return pymongo.Mongo_Client(server_name, server_port)
        except Exception as error:
          raise MongoDB_Exceptions_Connection(db_configs.MONGO_DB_CONNECTION_ERROR)
    
    @staticmethod
    def set_mongo_database(connection_object, database_name):
        '''
            Given an existing database in the System ,using the
            connection object and database name return the database instance
            :param connection_object: Mongo Connection instance
            :param database_name: Name of the database in Mongo
            @return:
                Success -> Database instance
                Exception -> Inform User that the database cannot be fetched
        '''
        try:          
           return connect_object[database_name]
        except Exception as error:
          raise MongoDB_Exceptions_DataBase(db_configs.MONGO_DB_DATABASE_ERROR.format(database_name,error))
    
    @staticmethod
    def insert_records(collection_object, records):
        '''
            Given an existing database in the System, insert records
            to the User specified collections.
            :param collection_object: Collection inside a database on which documents will be inserted
            :param records: The Records that are meant to be inserted inside a collection within a database
            @return:
                Success -> Insert Record into Mongo DB Collections
                Exception -> Inform the User that the records couldn't be inserted
        '''
        try:          
           return collection_object.insert_one(records) if not records.__class__ == list else collection_object.insert_many(records)
        except Exception as error:
          raise MongoDB_Exceptions_Records(db_configs.MONGO_DB_DATABASE_COLLECTIONS_DOCUMENTS_INSERT_ERROR.format(error)) 
        
    @staticmethod
    def update_records(collection_object, records):
        '''
            Given an existing database and collection in the System, update all documents in the collection.
            :param collection_object: Collection inside a database on which documents will be updated
            :param records: The Records that are meant to be inserted inside a collection within a database
            @return:
                Success -> Update all documents in the mongodb collection that match the criteria.
                Exception -> Inform the User that the records couldn't be updated.
        '''
        try:          
           # Get the field -> user_name
           records_user_name = records['user_name']
           # Update all documents in the collection where the user_name == records_user_name
           return collection_object.update(
                {"user_name":records_user_name},
                    {
                        "$set":records
                    }
                )
        except Exception as error:
          raise MongoDB_Exceptions_Records(db_configs.MONGO_DB_DATABASE_COLLECTIONS_DOCUMENTS_UPDATE_ERROR.format(error)) 

    @staticmethod
    def delete_records(collection_object, records):
        '''
            Given an existing database and collection in the System, delete all documents in the collection.
            :param collection_object: Collection inside a database on which documents will be deleted.
            :param records: Find records['user_name'] and delete all documents inside a collection.
                where such user_name exists.
            @return:
                Success -> Update all documents in the mongodb collection.
                Exception -> Inform the User that the records couldn't be updated.
        '''
        try:          
           # Get the field -> user_name
           records_user_name = records['user_name']
           # Delete all documents in the collection where the user_name == records_user_name
           return collection_object.delete_many({"user_name":records_user_name})
        except Exception as error:
          raise MongoDB_Exceptions_Records(db_configs.MONGO_DB_DATABASE_COLLECTIONS_DOCUMENTS_UPDATE_ERROR.format(error)) 

    @staticmethod
    def return_records(collection_object):
        '''
            Given an existing database and a collection in the System, return records
            from the User specified collections.
            :param collection_object: Collection name from which the records are to be retreived
            @return:
                Success -> Array of records from the given collection
                Exception -> Inform the User that the records couldn't be retreived and return an empty mapper
        '''
        try:       
           for each_record in collection_object.find():
                yield each_record
        except Exception as error:
          return {}
