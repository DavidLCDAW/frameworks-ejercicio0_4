OPTIONS_MENU: dict[str, int] = {
    "Ver": 1,
    "Añadir usuario": 2,
    "Eliminar usuario": 3,
    "Salir": 4,
}


def print_menu() -> None:
    print("Menu: ")
    for key, value in OPTIONS_MENU.items():
        print(f"{value}. {key}")


def ask_option() -> int:
    option: int = int(input("Selecciona una opción: "))
    return option


def validate_option(option: str) -> int:
    return OPTIONS_MENU.get(option, -1)


# def get_user() -> User:
# def get_format() -> str:
