import pymysql

try:
    conn = pymysql.connect(host='localhost', user='root', password='')
    cursor = conn.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS resume_db;')
    print("Database created successfully")
    conn.close()
except Exception as e:
    print(f"Failed to create database: {e}")
