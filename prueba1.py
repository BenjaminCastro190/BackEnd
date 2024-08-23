
print("***REGISTRO***")
user=input("Ingrese su nombre: ")
password=input("Ingrese su contraseña: ")

print("***LOGIN***")

userl=input("Ingrese su nombre: ")
passwordl=input("Ingrese su contraseña: ")

if user == userl and password==passwordl:
    print("***INGRESADO***")
    print("***CAlCULADORA***")
    num1=int(input("Ingrese su primer numero"))
    num2=int(input("Ingrese su segundo numero"))
    print("1) SUMA")
    print("2) RESTA")
    print("3) MULTIPLICACION")
    print("4) DIVISION")
    Opcion=int(input("Que opcion elige:"))
    if Opcion==1:
        sum=num1+num2
        print(sum)
    elif Opcion==2:
        rest=num1-num2
        print(rest)
    elif Opcion==3:
        mult=num1*num2
        print(mult)
    elif Opcion==4:
        div=num1/num2
        print(div)


else:
    print("***NO INGRESADO***")
