import argparse
from utill import parse_mysql_connection_string, parse_postgresql_connection_string
from database import mongoDBConnection, postgreSQLConnection, mysqlConnection

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='A database connection test',
        prog="PROG",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('--mysql', help='MySQL Connection')
    parser.add_argument('--mongo', help='Mongo Connection')
    parser.add_argument('--postgre', help='PostgreSQL Connection')
    
    args = parser.parse_args()

    parseArgs = vars(args)

    if(parseArgs['mysql'] != None):

        conectionProp = parse_mysql_connection_string(parseArgs['mysql'])
        mysqlConnection(host = conectionProp['host'],
            user = conectionProp['username'],
            password = conectionProp['password'],
            database = conectionProp['database'],
            port = conectionProp['port'])
        
    if(parseArgs['mongo'] != None):

        mongoDBConnection(parseArgs['mongo'])

    if(parseArgs['postgre'] != None):
        
        conectionProp = parse_postgresql_connection_string(parseArgs['postgre'])
        postgreSQLConnection(
            host = conectionProp['host'],
            user = conectionProp['username'],
            password = conectionProp['password'],
            database = conectionProp['database'],
            port = conectionProp['port']
        )

