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
        Records are inserted and fetched from Json/DB
    '''
    
    @users_api.route('/user_info')
    def users_information():
        '''
            Given a key get all information w.r.t to an User
        '''
        # Get all users whose attributes matches the argument specified by the User
        get_users_information = web_utils.Tasks.get_users_information(request.args.items(),request.authorization)
        return json.dumps({"data":get_users_information})

'''
    Start the Flask Server and do all REST Operations
'''        
if __name__ == "__main__":
    # Pre-Requisite
    web_utils.Tasks.set_process_read_frequent()
    # Run the app in port 4000
    users_api.run(debug=True,port=4000)

    
    
    
    
    
    
    
    
    
    
    