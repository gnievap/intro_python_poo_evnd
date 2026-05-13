def main():
    print("Hello, World!")
    print("Hola de nuevo, Mundo!")
    resultado = suma()
    print(f"La suma de los dos números es: {resultado}")

def suma():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    return num1 + num2

if __name__ == "__main__":
    main()