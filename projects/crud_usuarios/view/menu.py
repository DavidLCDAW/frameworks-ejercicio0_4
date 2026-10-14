from model.User import User

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


def get_user() -> User:
    print("Introduce los datos del usuario\n")
    # Variable basura
    id: str = "0"

    nombre: str = input("Nombre: \n")
    apellido1: str = input("Apellido 1: \n")
    apellido2: str = input("Apellido 2: \n")
    fecha_nacimiento: str = input("Fecha de nacimiento: \n")
    user = User(
        id=id, nombre=nombre, ape1=apellido1, ape2=apellido2, fechanac=fecha_nacimiento
    )
    user = User(
        id=id, nombre=nombre, ape1=apellido1, ape2=apellido2, fechanac=fecha_nacimiento
    )
    return user


def get_user_id() -> str:
    id: str = input("Introduce el identificador del usuario\n")
    return id


# def get_format() -> str:
