class ClubError(Exception):
    pass


class SocioExistenteError(ClubError):
    """
    Representa una excepción que indica que el socio ya existe en el club

    Attributes:
        cedula: un str que indica la cédula del socio que ya existe
        msg: un str que contiene el mensaje de error
    """
    def __init__(self, cedula: str, msg: str):
        self.cedula = cedula
        self.msg = msg


class SocioNoExistenteError(ClubError):
    """
    Representa una excepción que indica que el socio no existe en el club

    Attributes:
        cedula: un str que indica la cédula del socio que no existe
        msg: un str que contiene el mensaje de error
    """
    def __init__(self, cedula: str, msg: str):
        self.cedula = cedula
        self.msg = msg
