Aim:

	To implement an user management system with basic authentication using REST APIs.

Principle:

	 CRUD -> The REST API must support all the CRUD operations such as Create, Update and Delete
	 The following operations are performed;

	 	1.) GET
	 	2.) POST
	 	3.) PUT
	 	4.) DELETE

Attributes:

	The User Management System shall have the following attributes for all Users that undergo CRUD operations.

	['emp_id','name_prefix','first_name','middle_initial','last_name','gender','email',
	'father_name','mother_name','mother_maiden_name','dob','tob','age','weight','doj','quarter_joining','half_joining',
	'year_joining','month_joining','month_name_joining','short_month','day_of_joining','dow_joining','short_dow',
	'age_in_company','salary','last_hike','ssn','phone','place','county','city','state','zip','region','user_name','password']

Source Code:
	
	Entire Project Source Code is located at;
		https://github.com/pyexplorers/pythonics

Modules and Significance:
	
	1.) 
		File name: https://github.com/pyexplorers/pythonics/blob/master/core/app/web/apis.py
		Requirement: 
			1.) Handle all incoming REST Calls such as GET,PUT,POST and DELETE. 
			2.) Starting point where the server is booted and processes are invoked.

	2.) 
		File name: https://github.com/pyexplorers/pythonics/blob/master/core/app/web/web_utils.py
		Requirement: 
			1.) Handle all execution opertions for REST Calls such as GET,PUT,POST and DELETE as and when invoked by apis.py.
			2.) The execution, verification and validation happens through this module.

	3.) 
		File name: https://github.com/pyexplorers/pythonics/blob/master/core/app/web/web_configs.py
		Requirement: 
			1.) Handle all configurations related information.
			2.) Store all User's attributes.
			3.) Store database credentials for connecting to database and retreiving the collections.
			4.) Actual connection to MongoDB , fetching database and collection happens in this module.

	4.) 
		File name: https://github.com/pyexplorers/pythonics/blob/master/core/databases/mongoapp/db_configs.py
		Requirement: 
			1.) Handle all configurations related information related to database.
			2.) Store all exceptions and error messages to be raised when database operation fails.
			3.) Store all User's attributes.


	5.) 
		File name: https://github.com/pyexplorers/pythonics/blob/master/core/databases/mongoapp/query.py
		Requirement: 
			1.) Handle all database tasks
			2.) Following actions are performed in this module
				-> MongoDB Database Connection.
				-> Retreiving User recommended database.
				-> Retreiving User recommended collection inside the database.
				-> Insert documents into a collection.
				-> Update documents in a collection.
				-> Delete documents in a collection.
				-> Find and Yield all documents inside a collection.


	6.) 
		File name: https://github.com/pyexplorers/pythonics/blob/master/core/metas/metas.py
		Requirement: 
			1.) Handle all metaprogramming tasks
			2.) Following actions are performed in this module
				-> Validate REST API Credentials.
        		-> Execute the authorize function and return results if credentials hold good else raise error.


	7.) 
		File name: https://github.com/pyexplorers/pythonics/blob/master/core/utilities/pyutils.py
		Requirement: 
			1.) Handle all common and repetitive tasks as an utility
			2.) Following actions are performed in this module
				-> Read normal files.
				-> Read *.json files.
				-> Write *.json files.
				-> Issue a GET REST API Call.
				-> Issue a POST REST API Call.
				-> Validate all the information queried by the User.
				-> Given a *.csv file, read it and populate the *.json file.

