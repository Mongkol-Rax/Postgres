"""
DatabaseService: A CRUD service for PostgreSQL using psycopg2.
"""

import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv


class DatabaseService:
    """
    A service class to handle CRUD operations with PostgreSQL.
    """

    def __init__(self):
        """
        Initialize the DatabaseService with a connection to PostgreSQL.
        """
        load_dotenv()

        db_user = os.getenv("POSTGRES_USER")
        db_password = os.getenv("POSTGRES_PASSWORD")
        db_name = os.getenv("POSTGRES_DB")
        db_host = os.getenv("POSTGRES_HOST")
        db_port = os.getenv("POSTGRES_PORT")

        try:
            self.connection = psycopg2.connect(
                dbname=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
                cursor_factory=RealDictCursor,
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("Connected to the database successfully!")
        except psycopg2.Error as error:
            print(f"Error connecting to the database: {error}")
            self.connection = None
            self.cursor = None

    def create(self, c_text, c_double):
        """
        Insert a new record into the Table1 table.

        Args:
            c_text (str): The text value for the record.
            c_double (float): The double value for the record.

        Returns:
            int: The ID of the newly inserted record.
        """
        if not self.cursor:
            raise ConnectionError("Database connection is not initialized.")
        
        query = """
        INSERT INTO public."Table1" (c_text, c_double)
        VALUES (%s, %s) RETURNING id;
        """
        self.cursor.execute(query, (c_text, c_double))
        return self.cursor.fetchone()["id"]

    def read(self):
        """
        Retrieve all records from the Table1 table.

        Returns:
            list[dict]: A list of dictionary representations of the records.
        """
        if not self.cursor:
            raise ConnectionError("Database connection is not initialized.")
        
        query = 'SELECT * FROM public."Table1";'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def read_by_id(self, record_id):
        """
        Retrieve a record from the Table1 table by ID.

        Args:
            record_id (int): The ID of the record to retrieve.

        Returns:
            dict: A dictionary representation of the record.
        """
        if not self.cursor:
            raise ConnectionError("Database connection is not initialized.")
        
        query = 'SELECT * FROM public."Table1" WHERE id = %s;'
        self.cursor.execute(query, (record_id,))
        return self.cursor.fetchone()

    def update(self, record_id, c_text=None, c_double=None):
        """
        Update a record in the Table1 table.

        Args:
            record_id (int): The ID of the record to update.
            c_text (str, optional): The new text value.
            c_double (float, optional): The new double value.

        Returns:
            bool: True if the record was updated, False otherwise.
        """
        if not self.cursor:
            raise ConnectionError("Database connection is not initialized.")
        
        query = """
        UPDATE public."Table1"
        SET c_text = %s, c_double = %s
        WHERE id = %s;
        """
        self.cursor.execute(query, (c_text, c_double, record_id))
        return self.cursor.rowcount > 0

    def delete(self, record_id):
        """
        Delete a record from the Table1 table.

        Args:
            record_id (int): The ID of the record to delete.

        Returns:
            bool: True if the record was deleted, False otherwise.
        """
        if not self.cursor:
            raise ConnectionError("Database connection is not initialized.")
        
        query = 'DELETE FROM public."Table1" WHERE id = %s;'
        self.cursor.execute(query, (record_id,))
        return self.cursor.rowcount > 0

    def close(self):
        """
        Close the database connection.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
