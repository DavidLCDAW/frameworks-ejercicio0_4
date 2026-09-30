class User:
    def __init__(self, id: str, nombre: str, ape1: str, ape2: str, fechanac: str):
        self._id = User._sanitize(id)
        # self._nombre = User._sanitize(nombre)
        # self._ape1 = User._sanitize(ape1)
        # self._ape2 = User._sanitize(ape2)
        # self._fechanac = User._sanitize(fechanac)
