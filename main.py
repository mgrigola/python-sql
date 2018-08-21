import mysql.connector
from mysql.connector import errorcode
import numpy as np

cnxConfig = {
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'movie_ratings',
    'user': 'root',
    'password': 'admin',
    'use_pure': 'False'
}


try:
    cnx = mysql.connector.connect(**cnxConfig)
except mysql.connector.Error as err:
    okay = False
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('(server login) access denied :*( ')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('specified database does not exist :*( ')
    else:
        print('error:', err)
else:
    okay = True
    cursor = cnx.cursor()

    query = "SELECT user_id, movie_id, rating_val FROM ratings"
    cursor.execute(query)

    qryDtype = [('user_id', 'u4'), ('movie_id', 'u4'), ('rating', '<f8')]
    something = np.fromiter(cursor.fetchall(), qryDtype)

    cursor.close()
    cnx.close()

