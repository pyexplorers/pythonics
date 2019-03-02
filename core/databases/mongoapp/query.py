'''
    Import modules to be used in the mongo related operations
'''
import pymongo
import db_configs

'''
 A module to perform all mongodb related operations
    1.) Insert 
    2.) Update
    3.) Delete
    4.) DB Connections and Related Objects
'''

class Mongo_Utils:
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
          raise Exception(db_configs.MONGO_DB_CONNECTION_ERROR)
    
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
          raise Exception(db_configs.MONGO_DB_DATABASE_ERROR.format(database_name))
    
    @staticmethod
    def insert_records(collection_object, records):
        '''
            Given an existing database in the System, insert records
            to the User specified collections.
            :param collection_object: Collection name into which the records are to be inserted
            :param records: The Records that are meant to be inserted inside a collection within a database
            @return:
                Success -> Insert Record into Mongo DB Collections
                Exception -> Inform the User that the records couldn't be inserted
        '''
        try:          
           return collection_object.insert_one(records) if not records.__class__ == list else collection_object.insert_many(records)
        except Exception as error:
          raise Exception(db_configs.MONGO_DB_DATABASE_COLLECTIONS_INSERT_ERROR) 
        
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
