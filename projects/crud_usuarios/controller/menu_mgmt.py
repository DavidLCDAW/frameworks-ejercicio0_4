from model.User import User
from model.db import add_user, connect, view_users


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
        print(f"Error: {e}")
