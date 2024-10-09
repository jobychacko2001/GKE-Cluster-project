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
            f'PWD={password}'
        )
        print("Connection successful!")
        return conn
    except pyodbc.Error as e:
        print("Error in connection:", e)

# Create a connection
conn = get_db_connection()
if conn:
    cursor = conn.cursor()

    # Create the 'users' table
    cursor.execute("""
    CREATE TABLE users (
        id INT PRIMARY KEY IDENTITY,
        name NVARCHAR(100),
        email NVARCHAR(100)
    )
    """)

    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()
