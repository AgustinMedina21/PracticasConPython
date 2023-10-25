num = int(input("Ingrese un valor y voy a sumar los positivos, con 0 termina"))
suma = 0
while num != 0:
    if num > 0:
        print("Ingresaste un positivo, lo sumo")
        suma += num
    num = int(input("Ingrese un valor y voy a sumar los positivos, con 0 termina"))
print(f"La suma de los positivos es: {suma}")