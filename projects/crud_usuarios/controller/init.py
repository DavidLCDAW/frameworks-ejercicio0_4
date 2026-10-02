from pathlib import Path

from view.menu import ask_option, print_menu, validate_option

from controller.menu_mgmt import view

FILE_PATH = Path(__file__).resolve().parent.parent / "conf.txt"
DEBUG: bool = True
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
