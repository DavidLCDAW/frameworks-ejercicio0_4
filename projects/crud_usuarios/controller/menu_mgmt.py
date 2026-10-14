from model.db import add_user, connect, delete_user, update_user, view_user, view_users
from model.User import User


def view(config: dict[str, str]):
    print("Ver usuarios\n")
    try:
        cnx = connect(config)
        users = view_users(cnx)
        for user in users:
            print(
                f"Id: {user.id}\nNombre: {user.nombre}\nApellido 1: {user.ape1}\nApellido 2: {user.ape2}\nFecha de nacimiento: {user.fechanac}\n"
            )
    except Exception as e:
        print(f"Error: {e}")


def register(config: dict[str, str], user: User):
    print("Añadir usuario\n")
    try:
        cnx = connect(config)
        add_user(cnx, user)
    except Exception as e:
        print(f"error: {e}")


def delete(config: dict[str, str], userId: str):
    print("Eliminar usuario\n")
    try:
        cnx = connect(config)
        user = view_user(cnx, userId=userId)

        deleted = delete_user(cnx, user)

        if deleted:
            print("Usuario eliminado")

    except Exception as e:
        print(f"error: {e}")


def update(config: dict[str, str], user: User, userId: str):
    print("Modificar usuario\n")
    try:
        cnx = connect(config)

        updated = update_user(cnx, user, userId)

        if updated:
            print("Usuario modificado")

    except Exception as e:
        print(f"error: {e}")
