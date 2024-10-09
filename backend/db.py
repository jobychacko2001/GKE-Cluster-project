import pyodbc
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get database credentials from environment variables
server = os.getenv('SQL_SERVER')
database = os.getenv('SQL_DATABASE')
username = os.getenv('SQL_USERNAME')
password = os.getenv('SQL_PASSWORD')

def get_db_connection():
    """Function to establish a connection to the SQL Server."""
    try:
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password};'

        )
        print("Connection to the database was successful.")
        return conn
    except pyodbc.Error as ex:
        # Capture and print error details
        sqlstate = ex.args[0]
        message = ex.args[1]
        print(f"Connection failed with SQL state: {sqlstate} and message: {message}")
        return None

# Example usage
if __name__ == "__main__":
    connection = get_db_connection()
    if connection:
        # Close the connection if it's successful
        connection.close()
