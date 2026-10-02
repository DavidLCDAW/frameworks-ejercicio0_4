from model.db import connect, view_users


def view(config: dict[str, str]):
    print("Ver usuarios")
    try:
        cnx = connect(config)
        view_users(cnx)
    except Exception as e:
        print(f"Error: {e}")
