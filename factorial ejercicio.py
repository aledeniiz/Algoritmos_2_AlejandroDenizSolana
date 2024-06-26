#Recursividad para calcular el factorial de un número.
# Definir la función factorial
def factorial(n):
    """Calcula el factorial de un número dado.
    """
    #Código a realizar.
    # Caso base: Si n es 0, retorna 1
    if n == 0:
        return 1
    # Paso recursivo: Si n > 0, retorna n * factorial(n-1)
    else:
        return n * factorial(n - 1)

def main():
    print("=================================================================.")
    print("Test Case 1: Check the Factorial of 5.")
    print("=================================================================.")
    print("The factorial of 5 is: ", factorial(5))

if __name__ == "__main__":
    main()
