class Piramide:
    numeros = []

    def __init__(self, cantidad):
        self.cantidad = cantidad

    def ingresarNumeros(self):
        for i in range(self.cantidad):
            numero = int(input("Ingrese el número {}: ".format(i + 1)))
            self.numeros.append(numero)

    def ordenarNumeros(self):
        numerosOrdenados = sorted(self.numeros)
        return numerosOrdenados

    def imprimirNumeros(self):
        for num in self.numeros:
            print(num, end=" ")

    def imprimirParesImpares(self):
        pares = []
        impares = []

        for num in self.numeros:
            if num % 2 == 0:
                pares.append(num)

        for num in self.numeros:
            if num % 2 != 0:
                impares.append(num)

        print("\nNúmeros pares:", pares)
        print("Números impares:", impares)

    def contarRepeticiones(self):
        repeticiones = {}

        for num in self.numeros:
            if num in repeticiones:
                repeticiones[num] += 1
            else:
                repeticiones[num] = 1

        print("Repeticiones:")
        for num, cantidad in repeticiones.items():
            if cantidad >= 2:
                print("{} = {}".format(num, cantidad))

def main():
    cantidadNumeros = int(input("Ingrese la cantidad de números a ingresar: "))
    piramide_obj = Piramide(cantidadNumeros)
    piramide_obj.ingresarNumeros()
    piramide_obj.imprimirNumeros()
    numeros_ordenados = piramide_obj.ordenarNumeros()
    print("\nNúmeros ordenados:", numeros_ordenados)
    piramide_obj.imprimirParesImpares()
    piramide_obj.contarRepeticiones()

if __name__ == "__main__":
    main()
