cadena = input("Ingrese una cadena:\n ")
opcion = input("ingrese que quiere que se haga con la cadena:\n1- Te lo devuelvo en mayusculas\n2- Te lo devuelvo en minusculas\n3- Te devuelvo la longitud de la cadena\n")
if opcion == "1":
    print(f"La cadena en mayusculas es: {cadena.upper()}")
elif opcion == "2":
    print(f"La cadena en minusculas es: {cadena.lower()}")
elif opcion == "3":
    print(f"La longitud de la cadena es de {len(cadena)} caracteres")
else:
    print("Opcion invalida")