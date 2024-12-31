"""
DatabaseService: A CRUD service for PostgreSQL using psycopg2.
"""

import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

class DatabaseService:
    """
    A service class to handle CRUD operations with PostgreSQL.
    """

    def __init__(self):
        load_dotenv()
        self.db_user = os.getenv("POSTGRES_USER")
        self.db_password = os.getenv("POSTGRES_PASSWORD")
        self.db_name = os.getenv("POSTGRES_DB")
        self.db_host = os.getenv("POSTGRES_HOST")
        self.db_port = os.getenv("POSTGRES_PORT")

    def _get_connection(self):
        """
        Open a new database connection.
        """
        connection = psycopg2.connect(
            dbname=self.db_name,
            user=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            cursor_factory=RealDictCursor,
        )
        connection.autocommit = True
        return connection

    def create(self, c_text, c_double):
        """
        Insert a new record into the Table1 table.
        """
        query = """
        INSERT INTO public."Table1" (c_text, c_double)
        VALUES (%s, %s) RETURNING id;
        """
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (c_text, c_double))
                return cursor.fetchone()["id"]

    def read(self):
        """
        Retrieve all records from the Table1 table.
        """
        query = 'SELECT * FROM public."Table1";'
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()

    def read_by_id(self, record_id):
        """
        Retrieve a record from the Table1 table by ID.
        """
        query = 'SELECT * FROM public."Table1" WHERE id = %s;'
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (record_id,))
                return cursor.fetchone()

    def update(self, record_id, c_text=None, c_double=None):
        """
        Update a record in the Table1 table.
        """
        query = """
        UPDATE public."Table1"
        SET c_text = %s, c_double = %s
        WHERE id = %s;
        """
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (c_text, c_double, record_id))
                return cursor.rowcount > 0

    def delete(self, record_id):
        """
        Delete a record from the Table1 table.
        """
        query = 'DELETE FROM public."Table1" WHERE id = %s;'
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (record_id,))
                return cursor.rowcount > 0

