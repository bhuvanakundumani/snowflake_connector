<<<<<<< HEAD
Install python-dotenv

pip install -U python-dotenv


Install snowflake connector for python 

pip install --upgrade snowflake-connector-python


Environment Variables:

├── venv
├── .env

Create a file .env and store the credentials

SF_ACCOUNT    = <'account_name'>
SF_USER       = <'username'>
SF_WAREHOUSE  = <'warehouse_name'>
SF_DATABASE   = <'database_name'>
SF_SCHEMA     = <'schema_name'>
SF_PASSWORD   = <'password'>

Create a .gitignore file and add the following lines.

# Environments
.env
.venv
env/
venv/


