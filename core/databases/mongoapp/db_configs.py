'''
    Handle all MongoDB related configuration information
'''
# Raise an exception if mongodb cannot be connected
MONGO_DB_CONNECTION_ERROR = '''Unable to invoke a connection with Mongo -
Please check Server name and Port and ensure that Mongo server is active. '''

# Raise an exception if database name is not available
MONGO_DB_DATABASE_ERROR = '''Unable to invoke a connection with Mongo database - {}
Please check configurations.  Error -> {} '''
# Raise an exception if data cannot be inserted into a given collection
MONGO_DB_DATABASE_COLLECTIONS_DOCUMENTS_INSERT_ERROR = '''Unable to insert the documents into a given database and collection. Error -> {} '''
# Raise an exception if the documents inside a collection cannot be updated
MONGO_DB_DATABASE_COLLECTIONS_DOCUMENTS_UPDATE_ERROR = '''Unable to update the documents inside the given collection and database. Error -> {} '''
# Raise an exception if the documents inside a collection cannot be deleted
MONGO_DB_DATABASE_COLLECTIONS_DOCUMENTS_DELETE_ERROR = '''Unable to delete the documents inside the given collection and database. Error -> {} '''
