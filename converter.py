ml = 0.621371
km = 1.60934
respuesta = "si"
while respuesta == "si":
    option= input("Elige que deseas convertir: (1) km a ml o (2) ml a km")
    if option == "1":
        km1 = int(input("Ingresa los km que deseas convertir a millas:"))
        print(km1, "km" + " " + "son", km1 * ml, "millas")
    elif option == "2":
        ml1 = int(input("Ingresa las millas que deseas convertir a kilometros:"))
        print(ml1, "millas" + " " + "son", ml1 * km, "kilometros")
    respuesta = input("Te gustaria volver a repetir: si/no ")
print("SALIENDO ...")
print("---------------")
print("EXIT")




