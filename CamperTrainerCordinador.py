import Datos as fill

def registrarCamper():
    all= fill.cargar_datos()
    dixi={}
    try:
        print("Para registrarse debe seguir estos pasos ⭣")
        doc = input("Por favor digite su número de documento:\n⭢ ")
        if doc in all["Usuarios"]["Campers"]:
            print("Ups, este usuario ya está registrado")
        else:
            dixi["Nombres"]=input("Ingrese sus nombres:\n⭢ ")
            dixi["Apellidos"]=input("Ingrese sus apellidos:\n⭢ ")
            while True:
                dixi["Direccion"]=input("Ingrese su dirección:\n⭢ ")
                if "#" and "-" in dixi["Direccion"]:
                    dixi["Acudiente"]=input("Ingrese el nombre y apellido de su acudiente:\n⭢ ")
                    while True:
                        dixi["Celular"]=input("Ingrese su numero de celular:\n⭢ +57 ")
                        dixi["Telefono Fijo"]=input("Ingrese su numero de telefono fijo:\n⭢ 601 ")
                        dixi["Informacion"]={}
                        valorCelular = len(dixi["Celular"])
                        valorTelefono = len(dixi["Telefono Fijo"])
                        if (valorCelular == 10) and (valorTelefono == 7):
                            all["Usuarios"]["Campers"][doc] = dixi
                            fill.guardar_datos(all)
                            print("Felicitaciones has sido registrado con exito")
                            break
                        else:
                            print("El numero de celular debe tener 10 digitos y el telefono fijo debe tener 6")
                    break
                else:
                    print("La direccion debe estar completa")    
    except Exception as err:
        print("****************************************************************************************")
        print("Ups algo salio mal", err)

def modificarCamper():
    all = fill.cargar_datos()
    dixi={}
    try:
        print("Para modificar su usuario debe seguir estos pasos ⭣")
        doc = input("Por favor digite su número de documento:\n⭢ ")
        if doc in all["Usuarios"]["Campers"]:
            dixi["Nombres"]=input("Ingrese sus nombres:\n⭢ ")
            dixi["Apellidos"]=input("Ingrese sus apellidos:\n⭢ ")
            while True:
                dixi["Direccion"]=input("Ingrese su dirección:\n⭢ ")
                if "#" and "-" in dixi["Direccion"]:
                    dixi["Acudiente"]=input("Ingrese el nombre y apellido de su acudiente:\n⭢ ")
                    while True:
                        dixi["Celular"]=input("Ingrese su numero de celular:\n⭢ +57 ")
                        dixi["Telefono Fijo"]=input("Ingrese su numero de telefono fijo:\n⭢ 601 ")
                        valorCelular = len(dixi["Celular"])
                        valorTelefono = len(dixi["Telefono Fijo"])
                        if (valorCelular == 10) and (valorTelefono == 7):
                            all["Usuarios"]["Campers"][doc] = dixi
                            fill.guardar_datos(all)
                            print("Felicitaciones has sido registrado con exito")
                            break
                        else:
                            print("El numero de celular debe tener 10 digitos y el telefono fijo debe tener 6")
                    break
                else:
                    print("La direccion debe estar completa")  
        else:
              print("Ups, este usuario no está registrado")
    except Exception as err:
        print("****************************************************************************************")
        print("Ups algo salio mal", err)

def eliminarCamper():
    all = fill.cargar_datos()
    dixi={}
    try:
        print("Para eliminar el usuario debe seguir estos pasos ⭣")
        doc = input("Por favor digite su número de documento:\n⭢ ")
        if doc in all["Usuarios"]["Campers"]:
            opc=int(input("¿Esta seguro de eliminar el usuario?\n1.Si \n2.No\n⭢ "))
            if opc == 1:
                all["Usuarios"]["Campers"].pop(doc)
                fill.guardar_datos(all)
                print("Este usuario ha sido eliminado con exito")
            elif opc == 2:
                print("Accion no ejecutada")
            else:
                print("Ups algo está mal")
        else:
            print("Ups, este usuario no está registrado")
    except Exception as err:
        print("****************************************************************************************")
        print("Ups algo salio mal", err)

def registrarTrainer():
    all = fill.cargar_datos()
    dixi={}
    try:
        print("Para registrarse debe seguir estos pasos ⭣")
        doc = input("Por favor digite su número de documento:\n⭢ ")
        if doc in all["Usuarios"]["Trainers"]:
            print("Ups, este usuario ya está registrado")
        else:
            dixi["Nombres"]=input("Ingrese sus nombres:\n⭢ ")
            dixi["Apellidos"]=input("Ingrese sus apellidos:\n⭢ ")
            dixi["Edad"]=int(input("Ingrese su edad:\n⭢ "))
            dixi["Horario"]=input("Elija un horario M1 M2 T1 T2\n⭢ ")
            all["Usuarios"]["Trainers"][doc]=dixi
            fill.guardar_datos(all)
            print("Felicitaciones has sido registrado con exito")
    except Exception as err:
        print("****************************************************************************************")
        print("Ups algo salio mal", err)

def modificarTrainer():
    all = fill.cargar_datos()
    dixi={}
    try:
        print("Para registrarse debe seguir estos pasos ⭣")
        doc = input("Por favor digite su número de documento:\n⭢ ")
        if doc in all["Usuarios"]["Trainers"]:
            dixi["Nombres"]=input("Ingrese sus nombres:\n⭢ ")
            dixi["Apellidos"]=input("Ingrese sus apellidos:\n⭢ ")
            dixi["Edad"]=int(input("Ingrese su edad:\n⭢ "))
            all["Usuarios"]["Trainers"][doc]=dixi
            fill.guardar_datos(all)
            print("Felicitaciones has sido registrado con exito")
        else:
            print("Ups, este usuario no está registrado")
    except Exception as err:
        print("****************************************************************************************")
        print("Ups algo salio mal", err)

def elminarTrainer():
    all = fill.cargar_datos()
    dixi={}
    try:
        print("Para eliminar el usuario debe seguir estos pasos ⭣")
        doc = input("Por favor digite su número de documento:\n⭢ ")
        if doc in all["Usuarios"]["Trainers"]:
            opc=int(input("¿Esta seguro de eliminar el usuario?\n1.Si \n2.No\n⭢ "))
            if opc == 1:
                all["Usuarios"]["Trainers"].pop(doc)
                fill.guardar_datos(all)
                print("Este usuario ha sido eliminado con exito")
            elif opc == 2:
                print("Accion no ejecutada")
            else:
                print("Ups algo está mal")
        else:
            print("Ups, este usuario no está registrado")
    except Exception as err:
        print("****************************************************************************************")
        print("Ups algo salio mal", err)

def cordinadorCamper():
    all= fill.cargar_datos()
    dixi={}
    try:
        print("Ingrese los datos del camper que desea modificar ⭣")
        doc = input("Por favor digite su número de documento:\n⭢ ")
        if doc in all["Usuarios"]["Campers"]:
            while True:
                print("Vas a modificar al camper con nombre ⭢", all["Usuarios"]["Campers"][doc].get("Nombres") )
                dixi["Resultado Pruebas"]=int(input("Ingrese el resultado de las pruebas del camper:\n⭢ "))
                dixi["Estado"]=input("Ingrese el estado de camper:\n⭢ ")
                mayuscula = dixi["Estado"].capitalize()
                if dixi["Resultado Pruebas"] < 65 and mayuscula == "Aprobado":
                    print("Nota: El camper no puede estar aprobado si no pasó las pruebas con más de 65!")
                    print("********************************************************************************")
                else:
                    print("Las rutas para elegir son:", all.get("Rutas"))
                    dixi["Ruta"]=input("Ingrese la ruta del camper:\n⭢ ")
                    nombreTrainer= [i["Nombres"] for i in all["Usuarios"]["Trainers"].values()]
                    print("Por el momento contamos con la disponibilidad de estos trainers: ", nombreTrainer)
                    dixi["Trainer"]=input("Ingrese el trainer que desea asignarle\n⭢ " )
                    dixi["Horario"]=input("El camper tiene horario M1, M2, T1 o T2:\n⭢ ")
                    dixi["Notas"]={}
                    all["Usuarios"]["Campers"][doc]["Informacion"]=dixi
                    fill.guardar_datos(all)
                    print("Usuario modificado con exito!")
                    break
        else:
            print("Ups, este usuario no está registrado")
    except Exception as err:
        print("****************************************************************************************")
        print("Ups algo salio mal", err)
  
def asignarNotas():
    all= fill.cargar_datos()
    dixi={}
    try:
        print("Ingrese los datos del camper que desea modificar sus notas ⭣")
        doc = input("Por favor digite su número de documento:\n⭢ ")
        if doc in all["Usuarios"]["Campers"]:
                print("Vas a modificar las notas del camper con nombre ⭢", all["Usuarios"]["Campers"][doc].get("Nombres") )
                all["Usuarios"]["Campers"][doc]["Informacion"]["Estado"]="Cursando"
                dixi["Taller"]=int(input("Ingrese la nota del taller:\n⭢ "))
                dixi["Filtro"] =int(input("Ingrese la nota del filtro:\n⭢ "))
                promedio = (dixi["Taller"] + dixi["Filtro"]) / 2
                dixi["Nota final"]= promedio
                if promedio < 65:
                    dixi["Riesgo"]= True
                else: 
                    dixi["Riesgo"]= False
                all["Usuarios"]["Campers"][doc]["Informacion"]["Notas"]=dixi
                fill.guardar_datos(all)
                print("Notas modificadas con exito!")
        else:
            print("Ups, este usuario no está registrado")
    except Exception as err:
        print("****************************************************************************************")
        print("Ups algo salio mal", err)

def verHorario():
    all= fill.cargar_datos()
    dixi={}
    try:
        doc = input("Por favor digite su número de documento:\n⭢ ")
        if doc in all["Usuarios"]["Campers"]:
            horario = all["Usuarios"]["Campers"][doc]["Informacion"].get("Horario")
            print("Su horario es:",horario)
            opc = int(input("¿Desea verlo?\n1.Si 2.No\n⭢ "))
            if opc == 1:
                if horario == "M1" or horario == "m1":
                    for clave, valor in all["Horarios"].get("M1").items():
                        print(clave, "⭢", valor)
                elif horario == "M2" or horario == "m2":
                    for clave, valor in all["Horarios"].get("M2").items():
                        print(clave, "⭢", valor)
                elif horario == "T1" or horario == "t1":
                    for clave, valor in all["Horarios"].get("T1").items():
                        print(clave, "⭢", valor)
                elif horario == "T2" or horario == "t2":
                    for clave, valor in all["Horarios"].get("T2").items():
                        print(clave, "⭢", valor)
            elif opc ==2:
                print("No te mostraremos el horario, puedes retroceder")
            else:
                print("Ups opción incorrecta")
        else:
            print("Ups, este usuario no está registrado")
    except Exception as err:
        print("****************************************************************************************")
        print("Ups algo salio mal", err)

def agregarRuta():
    all= fill.cargar_datos()
    try:
        nombre = input("Ingrese el nombre de la ruta que desea crear\n⭢ ")
        mayuscula = nombre.capitalize()
        if mayuscula in all["Rutas"]:
            print("Ups esa ruta ya existe")
        else:
            all["Rutas"].append(mayuscula)
            fill.guardar_datos(all)
            print("Ruta creada con exito")
    except Exception as err:
        print("****************************************************************************************")
        print("Ups algo salio mal", err)

def verNotas():
    all= fill.cargar_datos()
    dixi={}
    try:
        doc = input("Por favor digite su número de documento:\n⭢ ")
        if doc in all["Usuarios"]["Campers"]:
            notas = all["Usuarios"]["Campers"][doc]["Informacion"].get("Notas")
            print("Sus notas son:")
            for clave, valor in notas.items():
                print( clave, "⭢", valor)
        else:
            print("Ups, este usuario no está registrado")
    except Exception as err:
        print("****************************************************************************************")
        print("Ups algo salio mal", err)

def verHorarioTrainer():
    all= fill.cargar_datos()
    dixi={}
    try:
        doc = input("Por favor digite su número de documento:\n⭢ ")
        if doc in all["Usuarios"]["Trainers"]:
            horario = all["Usuarios"]["Trainers"][doc].get("Horario")
            print("Su horario es:",horario)
            opc = int(input("¿Desea verlo?\n1.Si 2.No\n⭢ "))
            if opc == 1:
                if horario == "M1" or horario == "m1":
                    for clave, valor in all["Horarios"].get("M1").items():
                        print(clave, "⭢", valor)
                elif horario == "M2" or horario == "m2":
                    for clave, valor in all["Horarios"].get("M2").items():
                        print(clave, "⭢", valor)
                elif horario == "T1" or horario == "t1":
                    for clave, valor in all["Horarios"].get("T1").items():
                        print(clave, "⭢", valor)
                elif horario == "T2" or horario == "t2":
                    for clave, valor in all["Horarios"].get("T2").items():
                        print(clave, "⭢", valor)
            elif opc ==2:
                print("No te mostraremos el horario, puedes retroceder")
            else:
                print("Ups opción incorrecta")
        else:
            print("Ups, este usuario no está registrado")
    except Exception as err:
        print("****************************************************************************************")
        print("Ups algo salio mal", err)
