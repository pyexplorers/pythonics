'''
    An Utils module for all common and frequent tasks such as file handling etc..
'''
import json
import requests

class Py_Utils:
    
    @staticmethod
    def check_api_result(api_url,*args):
        '''
            Given an API URL do a GET request call and return the result
            :param api_url: URL on which GET will be applied
            :param args: Contains username and password
        '''
        try:
            print("Do a Get call for URL .. {} ".format(api_url))
            return requests.get(api_url,auth=(args[0],args[1]))
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