'''
    Import module to be used as part of apis requests
'''
from flask import Flask, request
import json
import web_utils,web_configs
import pdb

''' 
    Create the Flask app.
    Perform all CRUD operations.
    Process GET,POST,PUT,DELETE events with authentication    
'''
users_api = Flask(__name__)

class Users_Stats:
    '''
        A Class to store and return information about multiple users
        Records are inserted and fetched from Json/DB.
        Define separate method calls for each REST Type
            GET -> 
                def users_information
                @users_api.route('/user_info')
            POST -> 
                def post_users_information
                @users_api.route('/post_user_info')
    '''
    
    @users_api.route('/user_info')
    def users_information():
        '''
            Given a key get all information w.r.t to an User
            Search the cached data from MongoDB and return all
            records that match the user query.
            ************************************************
                For all REST GET calls , results will be loaded 
                from cache since hitting DB for query
                can be avoided and data  from cache can be faster.

                Data will be loaded from DB -> Cache periodically
            ************************************************
            @return:
                Success -> Valid records that match user's query
                Exception -> {"data":"ERROR"}
        '''
        # Get all users whose attributes matches the argument specified by the User
        get_users_information = web_utils.Tasks.get_users_information(request.args.items(),request.authorization)
        return json.dumps({"data":get_users_information})

    @users_api.route('/post_user_info',methods=['POST'])
    def post_users_information():
        '''
            On a REST POST call -> Make a new entry into MongoDB
            Given that User specifies required attributes and that the authorization information
            is correct then make an entry into the database.
            @return:
                Success -> {"data":"True"}
                Exception -> {"data":"ERROR"}
        '''
        print("\n\n\n {} \n\n\n ".format(request.method))
        # Get all users whose attributes matches the argument specified by the User
        get_users_information = web_utils.Tasks.post_users_information(request.args.items(),request.authorization)
        return {}
        
'''
    Start the Flask Server and do all REST Operations
'''        
if __name__ == "__main__":
    # Pre-Requisite
    web_utils.Tasks.set_process_read_frequent()
    # Run the app in port 4000
    users_api.run(debug=True,port=4000)

    
    
    
    
    
    
    
    
    
    
    