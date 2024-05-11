import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

# PostgreSQL connection details
DB_NAME = 'React_flask_app'
DB_USER = 'postgres'
DB_PASSWORD = 'shantanu'
DB_HOST = 'localhost'
DB_PORT = '5432'

__all__ = ['get_db_connection']

def get_db_connection():

    return psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )

    # DB_URL = os.environ.get('DATABASE_URL')
    # return psycopg2.connect(DB_URL)