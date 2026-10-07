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
    cnx: MySQLConnectionAbstract | PooledMySQLConnection | None,
) -> list[User]:
    if cnx is None or not cnx.is_connected():
        raise ConnectionError("No se pudo conectar a la base de datos")
    with cnx.cursor() as cursor:
        cursor.execute("select id, nombre, ape1, ape2, fechanac from usuarios")
        rows = cursor.fetchall()
        users = []
        for id, nombre, ape1, ape2, fechanac in rows:
            users.append(
                User(
                    id=str(id),
                    nombre=str(nombre),
                    ape1=str(ape1),
                    ape2=str(ape2),
                    fechanac=str(fechanac),
                )
            )
        return users

# Add user
def add_user(
    cnx: MySQLConnectionAbstract | PooledMySQLConnection | None,
    user: User,
) -> None:
    if cnx is None or not cnx.is_connected():
        raise ConnectionError("No se pudo conectar a la base de datos")
    with cnx.cursor() as cursor:
        cursor.execute(
            "insert into usuarios (nombre, ape1, ape2, fechanac) values (%s, %s, %s, %s)",
            (user.nombre, user.ape1, user.ape2, user.fechanac),
        )
        cnx.commit()
