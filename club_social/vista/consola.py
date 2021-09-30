from club_social.mundo.errores import SocioExistenteError, SocioNoExistenteError
from club_social.mundo.mundo import Club


def menu():
    opt = 0
    while opt not in range(1, 6):
        print("\nMENU DE OPCIONES - CLUB SOCIAL")
        print("1. Afiliar un socio al club")
        print("2. Registrar persona autorizada")
        print("3. Registrar consumo")
        print("4. Pagar factura")
        print("5. Salir")

        opt = int(input("\nIngrese una opción: "))

        if opt not in range(1, 6):
            print("\nERROR: Opción no válida")

    return opt


if __name__ == "__main__":
    club = Club()
    opcion = 0
    while opcion != 5:
        opcion = menu()
        if opcion == 1:
            print("\n>>>> AFILIAR SOCIO AL CLUB")
            cedula = input("Cédula del nuevo socio: ")
            nombre = input("Nombre del nuevo socio: ")
            try:
                club.afiliar_socio_al_club(cedula, nombre)
            except SocioExistenteError as err:
                print(f"\nERROR: {err.msg}")
            else:
                print("\nINFO: El socio fue afiliado exitosamente.")

        elif opcion == 2:
            print("\n>>>> REGISTRAR PERSONA AUTORIZADA")
            cedula = input("Cédula del socio: ")
            autorizado = input("Nombre de la persona autorizada: ")
            try:
                club.registrar_autorizado_por_socio(cedula, autorizado)
            except SocioNoExistenteError as err:
                print(f"\nERROR: {err.msg}")
            else:
                print("\nINFO: Se registró la persona autorizada exitosamente.")

        elif opcion == 3:
            print("\n>>>> REGISTRAR CONSUMO")
            cedula = input("Cédula del socio: ")
            concepto = input("Concepto del consumo: ")
            valor_valido = False
            while not valor_valido:
                try:
                    valor = float(input("Valor del consumo: "))
                except ValueError:
                    print("ERROR: El valor debe ser numérico.")
                else:
                    valor_valido = True
            autorizado = input("Nombre de la persona autorizada (opcional): ")
            try:
                club.registrar_consumo_a_socio(cedula, concepto, valor, autorizado)
            except SocioNoExistenteError as err:
                print(f"\nERROR: {err.msg}")
            else:
                print("\nINFO: Se registró el consumo exitosamente.")

        elif opcion == 4:
            print("\n>>>> PAGAR FACTURA")
            cedula = input("Cédula del socio: ")
            socio = club.buscar_socio(cedula)
            if socio is not None:
                if len(socio.facturas) > 0:
                    print("\nFACTURAS PENDIENTES")
                    for index, factura in enumerate(socio.facturas, start=1):
                        print(f"{index} - {factura}")

                    indx_factura = int(input("Factura a pagar: "))
                    factura = socio.facturas[indx_factura - 1]

                    try:
                        club.pagar_factura(cedula, factura)
                    except SocioNoExistenteError as err:
                        print(f"\nERROR: {err.msg}")
                    else:
                        print("\nINFO: Se pagó la factura exitosamente.")
                else:
                    print("\nINFO: No hay facturas pendientes.")
            else:
                print("\nERROR: No existe socio con la cédula dada.")

        elif opcion == 5:
            print("\n=================")
            print("FIN DEL PROGRAMA")
            print("=================")
