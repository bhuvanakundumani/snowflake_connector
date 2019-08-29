import snowflake.connector
import json
import os

#defined variables
CONFIG_LOCATION='config/'

# load config
CONFIG = json.loads(open(str(CONFIG_LOCATION+'config.json')).read())

# Get the credentials from config
SF_ACCOUNT    = CONFIG['credentials']['account']
SF_USER       = CONFIG['credentials']['user']
SF_WAREHOUSE  = CONFIG['credentials']['warehouse']
SF_DATABASE   = CONFIG['credentials']['database']
SF_SCHEMA     = CONFIG['credentials']['schema']
SF_PASSWORD   = CONFIG['credentials']['password']

# fire up an instance of a snowflake connection
connection = snowflake.connector.connect (
account  = SF_ACCOUNT,
user     = SF_USER,
password = SF_PASSWORD,
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



