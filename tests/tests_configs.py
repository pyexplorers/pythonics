'''
	Config file to store all the tests related information
'''

'''
	Define the project base-path
'''
PROJECT_BASE_PATH = "D:\\ArunChandramouli\\code\\pythonics\\users_records"

'''
	Test Content for data-store
'''
# Sample csv file with multiple employees records
test_csv_file = 'D:\\ArunChandramouli\\code\\pythonics\\users_records\\datastore\\sets\\csv\\records.csv'
# Json file to store employees records
test_write_file = 'D:\\ArunChandramouli\\code\\pythonics\\users_records\\datastore\\sets\\json\\records.json'
# Json dict keys - for storing employee data
array_json_columns = ['emp_id','name_prefix','first_name','middle_initial','last_name','gender','email',
'father_name','mother_name','mother_maiden_name','dob','tob','age','weight','doj','quarter_joining','half_joining',
'year_joining','month_joining','month_name_joining','short_month','day_of_joining','dow_joining','short_dow',
'age_in_company','salary','last_hike','ssn','phone','place','county','city','state','zip','region','user_name','password']


'''
	Test Content for REST-API Calls
'''
# REST GET URL
REST_API_GET_URL = ['http://127.0.0.1:4000/user_info?first_name=Lois&last_name=Walker&email=maria']

# REST POST URL
REST_API_POST_URL = ['http://127.0.0.1:4000/post_user_info?first_name=Lois&last_name=Walker&email=maria']

# Set username and password for authentication process
SET_USER_NAME,SET_USER_PWD = 'admin','admin'
# Error raised when invalid URL Credentials are sent
ERROR_INVALID_CREDS = {'ERROR_INVALID_CREDENTIALS': 'Authorization was not successful'}