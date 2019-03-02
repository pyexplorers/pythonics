'''
    Handle all MongoDB related configuration information
'''
# Raise an exception if mongodb cannot be connected
MONGO_DB_CONNECTION_ERROR = '''Unable to invoke a connection with Mongo -
Please check Server name and Port and ensure that Mongo server is active. '''

# Raise an exception if database name is not available
MONGO_DB_DATABASE_ERROR = '''Unable to invoke a connection with Mongo database - {}
Please check configurations.'''

# Raise an exception if data cannot be inserted into a given collection
MONGO_DB_DATABASE_COLLECTIONS_INSERT_ERROR = '''Unable to insert records into a given database and collection.'''
