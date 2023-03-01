import psycopg2
from config import config

# Establishing the connection
conn = psycopg2.connect(
    database="postgres", user='postgres', password='postgres', host='127.0.0.1', port='5432'
)
# Setting auto commit false
conn.autocommit = True
import configparser

config = configparser.ConfigParser()
config.read('db.ini')

host = config['postgresql']['host']
user = config['postgresql']['user']
passwd = config['postgresql']['passwd']
db = config['postgresql']['db']

print('postgresql configuration:')

print(f'Host: {host}')
print(f'User: {user}')
print(f'Password: {passwd}')
print(f'Database: {db}')


def insertEmployee(empid, empname):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO employee(empid,empname)
                VALUES(%s,%s) """
    conn = psycopg2.connect(
        database="postgres", user='postgres', password='postgres', host='127.0.0.1', port='5432'
    )
    # create a new cursor
    cur = conn.cursor()
    # execute the INSERT statement
    cur.execute(sql, (empid, empname))
    # commit the changes to the database
    conn.commit()
    # close communication with the database
    cur.close()


if __name__ == '__main__':
    # insert one Employee
    insertEmployee(300, 'ram')
