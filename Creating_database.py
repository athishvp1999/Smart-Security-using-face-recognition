from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

client = Cloudant("fcf055c3-9b00-418e-a955-a88fd70d32d0-bluemix", "a10a022499db0fcd47dce369b941bb895d640c859923fae1fd2806ea5cbe4721", url="https://fcf055c3-9b00-418e-a955-a88fd70d32d0-bluemix:a10a022499db0fcd47dce369b941bb895d640c859923fae1fd2806ea5cbe4721@fcf055c3-9b00-418e-a955-a88fd70d32d0-bluemix.cloudantnosqldb.appdomain.cloud")

client.connect()
database_name = "athishface"
my_database = client.create_database(database_name)
if my_database.exists():
   print(f"'{database_name}' successfully created.")

record_data={"name":"athish","education":"be","roll no":123}

# Create a document by using the database API.
new_document = my_database.create_document(record_data)
if new_document.exists():
     print(f"Document  successfully created.")
result_collection = Result(my_database.all_docs,include_docs=True)
print(f"Retrieved minimal document:\n{result_collection[0]}\n")