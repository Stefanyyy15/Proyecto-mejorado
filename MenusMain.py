import CamperTrainerCordinador as punto

def menuCamper():
    print("   ___                                   ")
    print("  / __|  __ _   _ __    _ __   ___   _ _ ")
    print(" | (__  / _` | | '  \  | '_ \ / -_) | '_|")
    print("  \___| \__,_| |_|_|_| | .__/ \___| |_|  ")
    print("                       |_|  ")
    while True:
        try:
            print("****************************************************************************************")
            print("Bienvenido Camper, ¿que desea hacer?")
            opc = int(input("1.Registrarme\n2.Modificar mi perfil\n3.Ver Notas \n4.Ver Horario\n0. Salir\n⭢ "))
            if opc == 1:
                punto.registrarCamper()
            elif opc == 2:
                punto.modificarCamper()
            elif opc == 3:
                punto.verNotas()
            elif opc == 4:
                punto.verHorario()
            elif opc == 0:
                print("Saliendo")
                break
            else:
                print("Ups opción incorrecta")
                print("****************************************************************************************")
        except Exception as err:
            print("****************************************************************************************")
            print("Ups algo salio mal", err)

def menuTrainer():
    print("  _____                _                    ")
    print(" |_   _|  _ _   __ _  (_)  _ _    ___   _ _ ")
    print("   | |   | '_| / _` | | | | ' \  / -_) | '_|")
    print("   |_|   |_|   \__,_| |_| |_||_| \___| |_|  ")
    while True:
        try:
            print("****************************************************************************************")
            print("Bienvenido Trainer, ¿que desea hacer?")
            opc = int(input("1.Registrarme\n2.Modificar mi perfil\n3.Eliminar mi perfil \n4.Modificar notas\n5.Ver Horario\n0. Salir\n⭢ "))
            if opc == 1:
                punto.registrarTrainer()
            elif opc == 2:
                punto.modificarTrainer()
            elif opc == 3:
                punto.elminarTrainer()
            elif opc == 4:
                punto.asignarNotas()
            elif opc == 5:
                punto.verHorarioTrainer()
            elif opc == 0:
                print("Saliendo")
                break
            else:
                print("Ups opción incorrecta")
                print("****************************************************************************************")
        except Exception as err:
            print("****************************************************************************************")
            print("Ups algo salio mal", err)

def menuCordinador():
    print("   ___                  _   _                    _             ")
    print("  / __|  ___   _ _   __| | (_)  _ _    __ _   __| |  ___   _ _ ")
    print(" | (__  / _ \ | '_| / _` | | | | ' \  / _` | / _` | / _ \ | '_|")
    print("  \___| \___/ |_|   \__,_| |_| |_||_| \__,_| \__,_| \___/ |_|  ")
    while True:
        try:
            print("****************************************************************************************")
            print("Bienvenido Cordinador, ¿que desea hacer?")
            opc = int(input("1.Modificar Camper\n2.Modificar Trainer\n3.Eliminar Camper \n4.Eliminar Trainer\n5.Asignar notas\n6.Agregar Ruta\n0. Salir\n⭢ "))
            if opc == 1:
                punto.cordinadorCamper()
            elif opc == 2:
                punto.modificarTrainer()
            elif opc == 3:
                punto.eliminarCamper()
            elif opc == 4:
                punto.elminarTrainer()
            elif opc == 5:
                punto.asignarNotas()
            elif opc == 6:
                punto.agregarRuta()
            elif opc == 0:
                print("Saliendo")
                break
            else:
                print("Ups opción incorrecta")
                print("****************************************************************************************")
        except Exception as err:
            print("****************************************************************************************")
            print("Ups algo salio mal", err)
        
    
def menuPrincipal():
    print("   _____                                             _                            _ ")
    print("  / ____|                                           | |                          | |")
    print(" | |        __ _   _ __ ___    _ __    _   _   ___  | |        __ _   _ __     __| |")
    print(" | |       / _` | | '_ ` _ \  | '_ \  | | | | / __| | |       / _` | | '_ \   / _` |")
    print(" | |____  | (_| | | | | | | | | |_) | | |_| | \__ \ | |____  | (_| | | | | | | (_| |")
    print("  \_____|  \__,_| |_| |_| |_| | .__/   \__,_| |___/ |______|  \__,_| |_| |_|  \__,_|")
    print("                              | |                                                   ")
    print("                              |_|                                                   ")
    while True:
        try:
            print("****************************************************************************************")
            print("Bienvenido ¿quien eres?")
            opc = int(input("1.Camper\n2.Trainer\n3.Cordinador\n0. Cerrar\n⭢ "))
            if opc == 1:
                menuCamper()
            elif opc == 2:
                menuTrainer()
            elif opc == 3:
                contra = input("Ingrese su contraseña\n⭢ ")
                if contra == "cordinador123":
                    menuCordinador()
                else:
                    print("Contraseña incorrecta")
                    print("****************************************************************************************")
            elif opc == 0:
                print("Cerrando programa, que vuelvas pronto!")
                break
            else:
                print("Ups opción incorrecta")
                print("****************************************************************************************")
        except Exception as err:
            print("****************************************************************************************")
            print("Ups algo salio mal", err)
            


menuPrincipal()