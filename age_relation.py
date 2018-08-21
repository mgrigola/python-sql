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

    query = "SELECT ratings.user_id, ratings.movie_id, ratings.rating_val, users.age, users.gender, users.occupation, users.zip_code \
            FROM ratings INNER JOIN users ON users.user_id = ratings.user_id"
    cursor.execute(query)

    qryDtype = [('user_id', 'u4'), ('movie_id', 'u4'), ('rating', '<f8'), ('age', 'u1'), ('gender', 'S1'), ('occupation', 'S16'), ('zip', 'S16')]
    userRatings = np.fromiter(cursor.fetchall(), qryDtype)

    cursor.close()
    cnx.close()

