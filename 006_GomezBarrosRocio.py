"""
Ejercicio 6
En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere también al
final del día calcular la cantidad de dinero que se ha depositado.
Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos nombre y
cantidad y los métodos __init__, depositar, extraer, mostrar_total.
La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y
deposito_total.
"""

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0

    def depositar(self):
        monto = int(input(f"{self.nombre}, ¿cuánto deseas depositar?: "))
        self.cantidad += monto
        print("Depósito realizado")

    def extraer(self):
        monto = int(input(f"{self.nombre}, ¿cuánto deseas extraer?: "))
        if monto <= self.cantidad:
            self.cantidad -= monto
            print("Extracción realizada")
        else:
            print("No tienes suficiente dinero")

    def mostrar_total(self):
        print(f"{self.nombre} tiene {self.cantidad}")


class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Cliente 1")
        self.cliente2 = Cliente("Cliente 2")
        self.cliente3 = Cliente("Cliente 3")

    def operar(self):
        for c in [self.cliente1, self.cliente2, self.cliente3]:
            print(f"\n--- Turno de {c.nombre} ---")
            print("1- Depositar")
            print("2- Extraer")

            op = int(input("Ingrese: "))
            if op == 1:
                c.depositar()
            elif op == 2:
                c.extraer()
            else:
                print("Opción inválida")

    def deposito_total(self):
        total = self.cliente1.cantidad + self.cliente2.cantidad + self.cliente3.cantidad
        print(f"\nEl total depositado en el banco es: {total}")

banco = Banco()
banco.operar()

print("\n--- ESTADO FINAL ---")
banco.cliente1.mostrar_total()
banco.cliente2.mostrar_total()
banco.cliente3.mostrar_total()

banco.deposito_total()