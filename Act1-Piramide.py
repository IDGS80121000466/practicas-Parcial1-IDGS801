class Piramide:
    numero = 0
    def __init__(self, n):
        self.numero = n

    def imprimirPiramide(self):
        for i in range(1, self.numero + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()


def main():
    numeroingresado = int(input("Ingrese un número: "))
    piramide_obj = Piramide(numeroingresado)
    piramide_obj.imprimirPiramide()

if __name__ == "__main__":
    main()
