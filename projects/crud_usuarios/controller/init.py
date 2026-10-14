from pathlib import Path

from view.menu import (
    ask_option,
    get_format,
    get_user,
    get_user_id,
    print_menu,
    validate_option,
)

from controller.menu_mgmt import delete, download_db, register, update, view

FILE_PATH = Path(__file__).resolve().parent.parent / "conf.txt"
DEBUG: bool = False
ERROR_KEY: str = "error"


def load_config() -> dict[str, str]:
    try:
        with open(FILE_PATH, "r") as f:
            return {
                "user": f.readline().strip().split("=")[1],
                "pw": f.readline().strip().split("=")[1],
                "host": f.readline().strip().split("=")[1],
                "db": f.readline().strip().split("=")[1],
                "admin_pw": f.readline().strip().split("=")[1],
            }
    except FileExistsError as e:
        return {"error": "error de fichero"}
    except Exception as e:
        return {"error": "error inesperado: " + str(e)}


def run_app(config: dict[str, str]) -> None:
    end: bool = False

    if DEBUG:
        print(config.items())

    if ERROR_KEY in config.keys():
        print(config["error"])
        return None

    while not end:
        print_menu()
        option = ask_option()
        if option == validate_option("Salir"):
            end = True
        if option == validate_option("Ver"):
            view(config)
        if option == validate_option("Añadir usuario"):
            user = get_user()
            register(config, user)
        if option == validate_option("Eliminar usuario"):
            userId = get_user_id()
            delete(config, userId)
        if option == validate_option("Modificar usuario"):
            userId = get_user_id()
            user = get_user()
            update(config, user, userId)
        if option == validate_option("Descargar"):
            formato: str = get_format()

            while (
                not formato.__contains__("json")
                and not formato.__contains__("csv")
                and not formato.__contains__("toml")
                and not formato.__contains__("yaml")
            ):
                print("Formato no válido.")
                formato = get_format()

            download_db(config, formato)
