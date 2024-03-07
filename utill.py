def parse_mysql_connection_string(connection_string):
    try: 
        components = connection_string.split('://')[1].split('@')
        username, password = components[0].split(':')
        host_port, database = components[1].split('/')
        host, port = host_port.split(':')

        return {
            'username': username,
            'password': password,
            'host': host,
            'port': int(port),
            'database': database
        }
    except Exception as e:
        print("-------------------------\n")
        print("Can not parse this mysql connection string\n")
        print("(Example: mysql://root:root@localhost:3304/redbiiddsun )")
        print("\n-------------------------")
        exit(1)



def parse_postgresql_connection_string(connection_string):
    try: 

        components = connection_string.split('://')[1].split('@')
        username, password = components[0].split(":")
        host_port, database = components[1]. split("/")
        host, port = host_port.split(":")

        return {
            'username': username,
            'password': password,
            'host': host,
            'port': int(port),
            'database': database
        }
    except Exception as e:
        print("-------------------------\n")
        print("Can not parse this postgreSQL connection string\n")
        print("(Example: postgres://admin:password@localhost:5432/database")
        print("\n-------------------------")
        exit(1)
        

