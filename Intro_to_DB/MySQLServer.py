#!/usr/bin/env python3
"""
Script to create the alx_book_store database in MySQL
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    """Create the alx_book_store database if it doesn't exist"""
    connection = None
    cursor = None
    
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',      # Replace with your MySQL username
            password='',      # Replace with your MySQL password
            port=3306
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        print("Please make sure MySQL server is running on localhost:3306")
        
    finally:
        # Close the connection if it was established
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()