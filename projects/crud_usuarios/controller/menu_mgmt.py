from model.db import connect, view_users


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
