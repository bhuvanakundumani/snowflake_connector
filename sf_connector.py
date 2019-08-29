import snowflake.connector
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv
 
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
 
# Get the credentials from .env
SF_ACCOUNT    = os.getenv('SF_ACCOUNT')
SF_USER       = os.getenv('SF_USER')
SF_WAREHOUSE  = os.getenv('SF_WAREHOUSE')
SF_DATABASE   = os.getenv('SF_DATABASE')
SF_SCHEMA     = os.getenv('SF_SCHEMA')
SF_PASSWORD   = os.getenv('SF_PASSWORD')

# fire up an instance of a snowflake connection
connection = snowflake.connector.connect (
account  = SF_ACCOUNT,
user     = SF_USER,
password = SF_PASSWORD,
warehouse = SF_WAREHOUSE,
database = SF_DATABASE,
schema   = SF_SCHEMA
)

cs = connection.cursor()

try:

 #SAMPLE CODE 1
  for cur in cs.execute("SHOW tables"):
    for ret in cur:
      print(ret)

  #SAMPLE CODE 2 
  cs.execute(
    "CREATE OR REPLACE TABLE "
    "test_table_1(col1 integer, col2 string)")

  " YOUR CODE HERE "
  
except Exception as e:
  raise e
finally:
  cs.close()

connection.close()



