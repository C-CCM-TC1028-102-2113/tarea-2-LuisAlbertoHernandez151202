def main():
    #escribe tu código abajo de esta línea
   print("Por favor escribe 3 números")
num1=int(input("Ingresa el primer número:"))
num2=int(input("Ingresa el segundo número:"))
num3=int(input("Ingresa el tercer número:"))
if num2 < num1 > num3:
    print("El número mayor es el primer número.Número:",num1)
elif num1 < num2 > num3:
    print("El número mayor es el segundo número.Número",num2)
elif num1 < num3 > num2:
        print("El número mayor es el tercer número.Número",num3)
    pass


if __name__=='__main__':
    main()
