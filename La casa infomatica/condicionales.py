#if
#elif
#else

# montojuan = int(input("ingrese un monto: "))
# pollo = 15
# if montojuan >= pollo:
    # print("Juan puede comprar pollo")
# else:
    # print("Juan no puede comprar pollo")

nota = int(input("ingrese una nota: "))
if nota >= 7:
    print("Aprobado")
elif nota == 6:
    print("Segunda oportunidad")
    nota2= int(input("ingrese una segunda nota: "))
    if nota2 >= 7:
        print("Aprobado")
    else:
        print("Reprobado")
else:
    print("Reprobado")

