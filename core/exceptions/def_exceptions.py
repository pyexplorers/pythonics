'''
	Define exceptions for all modules. 
	Define Custom exceptions classes by inheriting from the base exception class.

	class MongoDB_Exceptions_Connection -> Raise an exception on connection error with MongoDB.
'''

class MongoDB_Exceptions_Connection(Exception):
	'''
		Raise an exception on connection error with MongoDB.
	'''
	def __init__(self,message):
		'''
			Define the Exception Message
			:param message: Exception message to be raised
		'''
		self.message = message

	def __str__(self):
		'''
			Return the error message
		'''
		return "MongoDB ERROR Connection:: " + str(self.message)


class MongoDB_Exceptions_Records(Exception):
	'''
		Raise an exception on Add/Delete/Update error with MongoDB.
	'''
	def __init__(self,message):
		'''
			Define the Exception Message
			:param message: Exception message to be raised
		'''
		self.message = message

	def __str__(self):
		'''
			Return the error message
		'''
		return "MongoDB ERROR Add/Delete/Update :: " + str(self.message)

class MongoDB_Exceptions_DataBase(Exception):
	'''
		Raise an exception on database selection error with MongoDB
	'''
	def __init__(self,message):
		'''
			Define the Exception Message
			:param message: Exception message to be raised
		'''
		self.message = message

	def __str__(self):
		'''
			Return the error message
		'''
		return "MongoDB ERROR Database Selection :: " + str(self.message)

