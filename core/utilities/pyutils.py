'''
    An Utils module for all common and frequent tasks such as file handling etc..
'''
import json
import requests

class Py_Utils:

    @staticmethod
    def get_api_result(api_url,*args):
        '''
            Given an API URL do a GET request call and return the result
            :param api_url: URL on which GET will be applied
            :param args: Contains username and password
        '''
        try:
            print("Do a GET call for URL .. {} ".format(api_url))
            return requests.get(api_url,auth=(args[0],args[1]))
        except Exception as error:
            return {'data':'ERROR'}

    @staticmethod
    def validate_users_keys(user_inputs,required_inputs,user_names_array):
        '''
            Check if the User supplies all the required inputs.
            If any of the user keys are not passed, return False.
            If the username is already available in the database ,then do not process
            :param user_inputs: Inputs given by the User
            :param required_inputs: Expected inputs, mentioned as part of configs
            :param user_names_array: Array of usernames available in the database
        '''
        try:
            user_inputs_keys = sorted(list(user_inputs.keys()))
            required_inputs_keys = sorted(required_inputs)
            return user_inputs_keys == required_inputs_keys and str(user_inputs['user_name']).lower() not in user_names_array
        except Exception as error:
            return False

    @staticmethod
    def post_api_result(api_url,*args):
        '''
            Given an API URL do a GET request call and return the result
            :param api_url: URL on which GET will be applied
            :param args: Contains username and password
        '''
        try:
            print("Do a POST call for URL .. {} ".format(api_url))
            return requests.post(api_url,auth=(args[0],args[1]))
        except Exception as error:
            return {'data':'ERROR'}


    @staticmethod
    def read_json(json_file):
        ''' 
            Read a json file and return the contents
            :param json_file: Full Path of the json file to be read
            @return: 
                Success -> Json file contents as a dictionary. 
                Exception -> Empty dictionary
        '''
        try:
            print("Read Json ... {} ".format(json_file))
            with open(json_file,'r') as reader:
                return json.load(reader)
        except Exception as error:
            return {}

    @staticmethod
    def write_json(json_file,contents):
        ''' 
            Write the contents to the *json* file
            :param json_file: Full Path of the json file to be written to
            :param contents: Contents to be written to json file
            @return: 
                Success -> Json file contents as a dictionary. 
                Exception -> Empty dictionary
        '''
        try:
            with open(json_file,'w') as writer:
                return json.dump(contents,writer)
        except Exception as error:
            return {}

    @staticmethod
    def read_file(file_path):
        ''' 
            Read any file and return the contents
            :param file_path: Full Path of the file to be read
            @return: 
                Success -> File contents as an Array. 
                Exception -> Empty dictionary
        '''
        try:
            with open(file_path,'r') as reader:
                for each_line in reader.readlines():
                    yield each_line.split(',')
        except Exception as error:
            return {}

    @classmethod
    def populate_json_records(cls,csv_file_path,json_file_path,json_columns):
        '''
            Read the given csv file and populate the json file
            :param csv_file_path: Full path of the csv file
            :param json_file_path: Full path of the json file
            :param json_columns: Array of json columns
            @return:
                Success -> Write the contents to the final json file
                Exception ->Write empty array to the final json file
        '''
        try:
            csv_contents = list(cls.read_file(csv_file_path))
            json_contents = {"records":[{str(json_column):str(record) for record,json_column in zip(records,json_columns)} for records in csv_contents]}
            return cls.write_json(json_file=json_file_path,contents=json_contents)
        except Exception as error:
            return cls.write_json(json_file=json_file_path,contents={"error":[]})