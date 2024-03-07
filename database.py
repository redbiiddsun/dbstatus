import mysql.connector
import psycopg2
import pymongo

def mysqlConnection(host, user, password, database, port = 3306):
    try:
        conn = mysql.connector.connect(
            host = host,
            user= user,
            password= password,
            database = database,
            port = port)
            
        print("-------------------------\n")
        print(f"Successfuly Connected to database ({user}@{host} with database {database})")
        print("\n-------------------------")
        exit(1)
    except Exception as e: 
        print(e)

def mongoDBConnection(connection = "mongodb://localhost:27017/"):
    try:
        client = pymongo.MongoClient(connection)
        client.server_info()

        print("-------------------------\n")
        print(f"Successfuly Connected to database ({connection})")
        print("\n-------------------------")

    except Exception as e: 
        print(e)

def postgreSQLConnection(host, user, password, database, port = 5432):
    try:
        conn = psycopg2.connect(host = host,
            user = user,
            password = password,
            database = database,
            port = port)
            
        print("-------------------------\n")
        print(f"Successfuly Connected to database ({user}@{host} with database {database})")
        print("\n-------------------------")
        exit(1)
    except Exception as e: 
        print(e)



        