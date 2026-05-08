class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        if saldo_inicial < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = float(saldo_inicial)

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = float(nuevo_saldo)

    def depositar(self, cantidad):
        if cantidad <= 0:
            return False
        self._saldo += float(cantidad)
        return True

    def retirar(self, cantidad):
        if cantidad <= 0 or cantidad > self._saldo:
            return False
        self._saldo -= float(cantidad)
        return True


def main():
    cuenta = CuentaBancaria("Andres Ramirez", 500000)

    print("=== Taller de Encapsulación ===")
    print(f"Titular: {cuenta.titular}")
    print(f"Saldo inicial: ${cuenta.saldo:,.2f}")

    print("\nDepósito de $150.000:")
    print("Operación exitosa" if cuenta.depositar(150000) else "Operación fallida")
    print(f"Saldo actual: ${cuenta.saldo:,.2f}")

    print("\nRetiro de $100.000:")
    print("Operación exitosa" if cuenta.retirar(100000) else "Operación fallida")
    print(f"Saldo actual: ${cuenta.saldo:,.2f}")

    print("\nIntento de retiro de $700.000:")
    print("Operación exitosa" if cuenta.retirar(700000) else "Operación fallida")
    print(f"Saldo actual: ${cuenta.saldo:,.2f}")

    print("\nIntento de asignar saldo negativo:")
    try:
        cuenta.saldo = -1000
    except ValueError as error:
        print(f"Error capturado: {error}")


if __name__ == "__main__":
    main()
