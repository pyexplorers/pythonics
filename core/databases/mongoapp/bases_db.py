'''
	Define all methods that are required for all database operations.

	All Classes derive a metaclass and defines abstractmethods that must be implemented in the sub-class.

	class Mongo_Database_base -> Does the abstractmethods for MongoDB	
'''

import abc

class Mongo_Database_base(metaclass=abc.ABCMeta):
	
	'''
		A Class to handle all database related tasks for Mongo DB.
	'''

	@abc.abstractmethod
	def get_connection(server_name, server_port):
        '''
            Connect to MongoDB and return the connection object
            :param server_name: Server on which MongoDB is hosted
            :param server_port: Port on the Server where MongoDB is running
            @return:
                Success -> MongoDB Connection Object
                Exception -> Inform User that DB cant be reached
        '''

	@abc.abstractmethod
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

    @abc.abstractmethod
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

	@abc.abstractmethod
	def update_records(collection_object, records):
        '''
            Given an existing database and collection in the System, update all documents in the collection.
            :param collection_object: Collection inside a database on which documents will be updated
            :param records: The Records that are meant to be inserted inside a collection within a database
            @return:
                Success -> Update all documents in the mongodb collection that match the criteria.
                Exception -> Inform the User that the records couldn't be updated.
        '''        

    @abc.abstractmethod
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

    @abc.abstractmethod
	def return_records(collection_object):
        '''
            Given an existing database and a collection in the System, return records
            from the User specified collections.
            :param collection_object: Collection name from which the records are to be retreived
            @return:
                Success -> Array of records from the given collection
                Exception -> Inform the User that the records couldn't be retreived and return an empty mapper
        '''           