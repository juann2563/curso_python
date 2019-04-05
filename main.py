# tipos de datos y condiciones anidadas
""" x =float(input("Ingrese dato: "))
#print(x)
y= float(input("Ingrese dato: "))
print(10%2)
a = True
b = False
print(a) """
""" a = 5
if a<4:
    print("hola")
    print("mundo")
elif a<5:
    print("es menor que 5")
else:
    print("No es menor") """
# condiciones multiples
""" a = 3
b = 4
if a ==3 or b == 4:
    print("es correcto") """

# cilo while
""" a = 7
while a==7:
    print("estoy en el while")
    a = int(input("ingrese el nuevo valor de a: "))
    if a != 7:
        break """

# ciclo for
""" for i in range(0,5):
    print(i) """
#ejercicio algoritmo
num1 = int(input("Ingrese dato 1: "))
num2 = int(input("Ingrese dato 2: "))
while True:
    opcion = input('Ingrese S - suma, R - resta, M - multiplicacion, D - Division: ')
    if opcion == 'S':
        print("suma = " + str(num1 + num2))
        break
    elif opcion == 'R':
        print("resta = " + str(num1 - num2))
        break
    elif opcion == 'M':
        print("multiplicacion = " + str(num1 * num2))
        break
    elif opcion == 'D':
        if num2 == 0:
            print("No se puede realizar division por 0, intente de nuevo")
        else:
            print("division = " + str(num1 / num2))
            break
    else:
        print("opcion no valida, ingrese una opcion valida")
