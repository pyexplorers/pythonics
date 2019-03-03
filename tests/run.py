'''
	Run , Assert & Verify the Testcases for all REST APIs and Utils related data
'''
import sys
import tests_configs
from core.utilities.pyutils import Py_Utils
import pytest

'''
	A Class to run and execute the tests
'''
class Tests:
	'''
		Run multiple testcases and assert the records
	'''
	def tests_data_store(self):
		'''
			Check and Assert if the Datastore records are getting populated as per the requirement
			If the result of execution return an empty {} then assertion shall fail, else pass
		'''
		assert Py_Utils.populate_json_records(tests_configs.test_csv_file,tests_configs.test_write_file,tests_configs.array_json_columns) != {}

	def tests_get_requests_api(self):
		'''
			Do a GET call and check if the API is returning valid result
		'''
		# Execute all the URLs and get the requests object.
		result_api_calls = [Py_Utils.get_api_result(each_api_url_call,tests_configs.SET_USER_NAME,tests_configs.SET_USER_PWD) \
			for each_api_url_call in tests_configs.REST_API_GET_URL]
		'''
			To Check
				1.) Assert if the requests return code is 200
				2.) Assert if the data is not empty
			I do a check if all params that i pass return non-empty results
		'''
		for each_api_url_call_result in result_api_calls:
			print("\n\n Do Assertion for URL {} ".format(each_api_url_call_result.url))
			# Assert if the request was made with valid username and password
			assert each_api_url_call_result.json()['data'] != tests_configs.ERROR_INVALID_CREDS
			# Assert if the requests return code is 200
			assert each_api_url_call_result.status_code == 200 and bool(each_api_url_call_result.ok)
			# Assert if the request url was not errored out
			assert each_api_url_call_result.json()['data'] != ['ERROR']
			# Assert if the data is not empty
			assert each_api_url_call_result.json()['data'] != []

	@pytest.mark.skip()
	def tests_post_requests_api(self):
		'''
			Do a GET call and check if the API is returning valid result
		'''
		# Execute all the URLs and get the requests object.
		result_api_calls = [Py_Utils.post_api_result(each_api_url_call,tests_configs.SET_USER_NAME,tests_configs.SET_USER_PWD) \
			for each_api_url_call in tests_configs.REST_API_POST_URL]
		'''
			To Check
				1.) Assert if the requests return code is 200
				2.) Assert if the data is not empty
			I do a check if all params that i pass return non-empty results
		'''
		for each_api_url_call_result in result_api_calls:
			print("\n\n Do Assertion for URL {} ".format(each_api_url_call_result.url))
			print("\n\n Do Assertion for URL {} ".format(each_api_url_call_result.url))
			# Assert if the request was made with valid username and password
			assert each_api_url_call_result.json()['data'] != tests_configs.ERROR_INVALID_CREDS
			# Assert if the requests return code is 200
			assert each_api_url_call_result.status_code == 200 and bool(each_api_url_call_result.ok)
			# Assert if the request url was not errored out
			assert each_api_url_call_result.json()['data'] != ['ERROR']
			# Assert if the data is not empty
			assert each_api_url_call_result.json()['data'] != []			