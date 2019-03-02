'''
	Run , Assert & Verify the Testcases for all REST APIs and Utils related data
'''
import sys
import tests_configs
sys.path.append(tests_configs.PROJECT_BASE_PATH)# shortcut for imports
from core.utilities.pyutils import Py_Utils

class Tests:
	'''
		Run multiple testcases and assert the records
	'''
	def tests_data_store(self):
		assert Py_Utils.populate_json_records(tests_configs.test_csv_file,tests_configs.test_write_file,tests_configs.array_json_columns) != {}

