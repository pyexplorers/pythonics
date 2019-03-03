'''
    Perform all activities related to the REST API Queries
    Connect with Database and do insert,fetch,update and delete operations
'''
import web_configs
from core.utilities.pyutils import Py_Utils
from core.metas.metas import authorize

class Tasks:
    '''
        Do Insert, Fetch, Update and Delete
    '''
    @staticmethod
    def set_process_read_frequent():
        '''
            Set an infinite process to read the json files periodically and update the records
            ##TODO## -> This Function object will be triggered periodically and contents be updated
                from MongoDB
        '''
        #Class Variables to fetch & store the records -> File will be read once during module import
        Tasks.DATASTORE_JSON_RECORDS = Py_Utils.read_json(web_configs.DATASTORE_JSON_FILE_CACHES)['records']
        return Tasks.DATASTORE_JSON_RECORDS
    
    @staticmethod
    @authorize(credentials=web_configs.AUTHORIZATION_INFORMATION,invalid_credentials_error=web_configs.INVALID_CREDENTIALS_ERROR)
    def get_users_information(mapper,authorize_info):
        '''
            Given a key-value pair, check the database for given combination and retreive required values.
            ***
                For all GET Operations instead of querying the Databasse, we shall take the
                records from the cache and return the filtered output
            ***
            :param mapper: User requested keys & values
            :param authorize_info: Auth Info required for processing REST Calls
            @return:
                Success -> All matching records that fit user's requests
                Exception -> Empty Array
        '''
        try:
            # Filter keys that are actually part of the system
            keys_api_users_attributes = [each_user_key for each_user_key in mapper if str(each_user_key[0]).lstrip().rstrip() in web_configs.API_USERS_ATTRIBUTES]
            # Do a Search on the existing datastore to filter records that fit the user's requests
            return [each_record for each_record in Tasks.DATASTORE_JSON_RECORDS for each_user_key in keys_api_users_attributes \
                if str(each_record[each_user_key[0]]).lower().__contains__(str(each_user_key[1]).lower())]
        except Exception as error:
            return ['ERROR']