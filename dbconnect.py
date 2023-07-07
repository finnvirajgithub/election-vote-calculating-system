import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
mycursor = conn.cursor()
mycursor.execute('CREATE DATABASE IF NOT EXISTS ELECTION_VOTING_SYSTEM')

def create_tables():
    mycursor.execute("USE ELECTION_VOTING_SYSTEM")
    
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS candidate (
        NIC VARCHAR(20) PRIMARY KEY,
        name VARCHAR(50),
        election_number int,
        age INT,
        province VARCHAR(30),
        party VARCHAR(50),
        education VARCHAR(50)
    )
    """)
    
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS citizen (
        NIC VARCHAR(20) PRIMARY KEY,
        name VARCHAR(50),
        age INT,
        province VARCHAR(30)
    )
    """)
    
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS vote (
        citizen_NIC VARCHAR(20),
        candidate_NIC VARCHAR(20),
        electtion_No int,
        province VARCHAR(30),
        party VARCHAR(50)
    )
    """)
    
create_tables()