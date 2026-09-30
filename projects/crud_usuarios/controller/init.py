from pathlib import Path

from model.db import add_user, connect

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
        cnx = connect(config)
        print(add_user(cnx))

    if ERROR_KEY in config.keys():
        print(config["error"])
        return None
    return None
