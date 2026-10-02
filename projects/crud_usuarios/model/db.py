import mysql.connector
from model.User import User
from mysql.connector import errorcode
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection


def connect(
    config: dict[str, str],
) -> PooledMySQLConnection | MySQLConnectionAbstract | None:
    try:
        connection = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["pw"],
            database=config["db"],
        )
        return connection

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


# View users in the database
def view_users(
    cnx: MySQLConnectionAbstract | PooledMySQLConnection,
) -> None:
    if cnx and cnx.is_connected():
        with cnx.cursor() as cursor:
            result = cursor.execute("SELECT * FROM usuarios")

            rows = cursor.fetchall()

            for row in rows:
                print(row)

        cnx.close()
