#PROJECT - SGS

**Objective**: A simple backend service for management of health SBMs.

**Stack used**: Python (Flask with SQL Alchemy), code pattern MVC.

**How to run this code**:

1. Clone this repository
2. Run `pip install -r requirements.txt`
3. Create the necessary environment variables `FLASK_APP = "app.py"`
4. Create a database instance of Sqlite based on the model on paciente.py
5. Create the environment variable DB_PATH and set it to your database connection string (https://docs.sqlalchemy.org/en/14/core/engines.html)
6. Populate the instance if you wish.
7. Navigate on a terminal to the project source folder
8. Run `flask run`