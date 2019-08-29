Install python-dotenv

    pip install -U python-dotenv

Install snowflake connector for python 

    pip install --upgrade snowflake-connector-python

Environment Variables:

    ├── venv
    ├── .env

Create a file .env and store the credentials

    SF_ACCOUNT    = <'snowflake_account_name'>
    SF_USER       = <'snowflake_username'>
    SF_WAREHOUSE  = <'warehouse_name'>
    SF_DATABASE   = <'database_name'>
    SF_SCHEMA     = <'schema_name'>
    SF_PASSWORD   = <'snoflake_password'>

Create a .gitignore file and add the following lines.
    # Environments
    .env
    .venv
    env/
    venv/
    ENV/
    VENV/
    .Python
    [Bb]in
    [Ii]nclude
    [Ll]ib
    [Ll]ib64
    [Ll]ocal
    [Ss]cripts
    pyvenv.cfg
    pip-selfcheck.json

    # Ignore Mac DS_Store files
    .DS_Store

    # Ignore vscode files
    .vscode