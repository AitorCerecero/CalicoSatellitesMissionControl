import time

User = "Via003"
PWD = "Viasat3"

print("Bienvenido al Sistema Satelital Viasat")
while True:
    print("Por favor ingresa tu usuario y contraseña")
    user = input()
    pwd = input()

    if user == User and pwd == PWD:
        print("Bienvenido al Control de Mision de Viasat")
        while True:
            xex="""
            1. Monitoreo de estado Satelital
            2. Verificacion de Punteo de Antena
            3. Actualizacion de OS Satelital
            4. Salir del control de Mision
            """
            print(xex)
            op = int(input())
            if op == 1:
                print("Obteniendo Datos de los Satelites... Espera un momento")
                time.sleep(5)
                print("Datos Listos")
                print("""
                Nombre: AnikF F2
                Coordenadas: 111.1
                Longitud: Oeste
                Estado: Saludable, Sin Detalles
                """)
                print("""
                Nombre: Wildblue 1
                Coordenadas: 111.1
                Longitud: Oeste
                Estado: Saludable, Sin Detalles
                """)
                print("""
                Nombre: Viasat 1
                Coordenadas: 115.1
                Longitud: Oeste
                Estado: Saludable, Sin Detalles
                """)
                print("""
                Nombre: Viasat 2
                Coordenadas: 69.9
                Longitud: Oeste
                Estado: Saludable, Sin Detalles
                """)
                print("""
                Nombre: Viasat 3
                Coordenadas: 89.9
                Longitud: Oeste
                Estado: Requiere Actualizacion
                """)
                while True:
                    opcion_volver = input("Presione 'm' para volver al menú principal: ")
                    if opcion_volver == "m":
                        break
                    else:
                        print("Opción no válida. Inténtalo de nuevo.")
                        
            elif op == 2:
                print("Verificando punteo de Antena... Espera un momento")
                time.sleep(3)
                print("Punteo Correcto, Antenas de Central Terrestre apuntadas a los Satelites, Sistemas en Linea")
                while True:
                    opcion_volver = input("Presione 'm' para volver al menú principal: ")
                    if opcion_volver == "m":
                        break
                    else:
                        print("Opción no válida. Inténtalo de nuevo.")
            elif op == 3:
                print("Iniciando Actualización del OS... Espera un momento")
                time.sleep(10)
                print("Actualización Completada, Sistema Orbital en Linea de nuevo")
                while True:
                    opcion_volver = input("Presione 'm' para volver al menú principal: ")
                    if opcion_volver == "m":
                        break
                    else:
                        print("Opción no válida. Inténtalo de nuevo.")
            elif op == 4:
                print("Sesion Cerrada")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
        break
    else:
        print("Intenta de nuevo")
