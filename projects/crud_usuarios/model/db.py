import mysql.connector
from model.User import User
from mysql.connector import errorcode
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

CONNECTION = MySQLConnectionAbstract | PooledMySQLConnection | None


def connect(
    config: dict[str, str],
) -> CONNECTION:
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


# View user by id in the database
def view_users(
    cnx: CONNECTION,
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
    cnx: CONNECTION,
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


# Get user
def view_user(
    cnx: CONNECTION,
    userId: str,
) -> User:
    if cnx is None or not cnx.is_connected():
        raise ConnectionError("No se pudo conectar a la base de datos")
    with cnx.cursor() as cursor:
        cursor.execute(
            "select id, nombre, ape1, ape2, fechanac from usuarios where id=%s",
            (userId,),
        )
        row = cursor.fetchone()
        if row is None:
            raise ValueError(f"No se encontró el usuario con id {userId}")

        id, nombre, ape1, ape2, fechanac = row
        return User(
            id=str(id),
            nombre=str(nombre),
            ape1=str(ape1),
            ape2=str(ape2),
            fechanac=str(fechanac),
        )


# Delete user
def delete_user(
    cnx: CONNECTION,
    user: User,
) -> bool:
    if cnx is None or not cnx.is_connected():
        raise ConnectionError("No se pudo conectar a la base de datos")
    with cnx.cursor() as cursor:
        cursor.execute(
            "delete from usuarios where id=%s",
            (user.id,),
        )
        cnx.commit()
        return cursor.rowcount > 0


# Modify user
def update_user(cnx: CONNECTION, user: User, userId: str) -> bool:
    if cnx is None or not cnx.is_connected():
        raise ConnectionError("No se pudo conectar a la base de datos")

    with cnx.cursor() as cursor:
        cursor.execute(
            "update usuarios set nombre=%s, ape1=%s, ape2=%s, fechanac=%s where id=%s",
            (user.nombre, user.ape1, user.ape2, user.fechanac, userId),
        )
        cnx.commit()
        return cursor.rowcount > 0
