'''
    Perform all activities related to the REST API Queries
    Connect with Database and do insert,fetch,update and delete operations
'''
class Tasks:
    '''
        Do Insert, Fetch, Update and Delete
    '''
    @staticmethod
    def get_users_information(mapper):
    	'''
    		Given a key-value pair, check the database for given combination
    		and retreive required values
    	'''
    	print(list(mapper))
    