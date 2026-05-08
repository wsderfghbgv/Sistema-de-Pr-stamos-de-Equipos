from datetime import date


class Usuario:
    def __init__(self, nombre):
        self._nombre = nombre.strip()

    @property
    def nombre(self):
        return self._nombre

    def __str__(self):
        return self._nombre


class Equipo:
    def __init__(self, nombre):
        self._nombre = nombre.strip()
        self._disponible = True
        self._historial = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def disponible(self):
        return self._disponible

    @property
    def historial(self):
        return self._historial.copy()

    def registrar_prestamo(self, prestamo):
        if not self._disponible:
            return False
        self._historial.append(prestamo)
        self._disponible = False
        return True

    def devolver(self):
        if self._disponible:
            return False
        self._disponible = True
        return True


class Prestamo:
    def __init__(self, usuario, fecha):
        self._usuario = usuario
        self._fecha = fecha

    @property
    def usuario(self):
        return self._usuario

    @property
    def fecha(self):
        return self._fecha

    def como_tupla(self):
        return (self._usuario.nombre, self._fecha)

    def __str__(self):
        return f"Usuario: {self._usuario.nombre} | Fecha: {self._fecha}"


def mostrar_equipos(inventario):
    print("\n=== INVENTARIO DE EQUIPOS ===")
    if not inventario:
        print("No hay equipos registrados.")
        return

    for nombre, equipo in inventario.items():
        estado = "Disponible" if equipo.disponible else "Prestado"
        print(f"- {nombre}: {estado}")


def registrar_prestamo(inventario):
    mostrar_equipos(inventario)
    nombre_equipo = input("\nIngrese el nombre exacto del equipo a prestar: ").strip()

    if nombre_equipo not in inventario:
        print("El equipo no existe en el sistema.")
        return

    equipo = inventario[nombre_equipo]
    if not equipo.disponible:
        print("El equipo no está disponible en este momento.")
        return

    nombre_usuario = input("Ingrese el nombre del usuario: ").strip()
    if not nombre_usuario:
        print("El nombre del usuario no puede estar vacío.")
        return

    usuario = Usuario(nombre_usuario)
    prestamo = Prestamo(usuario, str(date.today()))

    if equipo.registrar_prestamo(prestamo):
        usuario_fecha = prestamo.como_tupla()
        print(
            f"Préstamo registrado correctamente para '{equipo.nombre}' "
            f"a nombre de {usuario_fecha[0]} en fecha {usuario_fecha[1]}."
        )
    else:
        print("No fue posible registrar el préstamo.")


def devolver_equipo(inventario):
    nombre_equipo = input("\nIngrese el nombre exacto del equipo a devolver: ").strip()

    if nombre_equipo not in inventario:
        print("El equipo no existe en el sistema.")
        return

    equipo = inventario[nombre_equipo]
    if equipo.devolver():
        print(f"El equipo '{equipo.nombre}' fue marcado como disponible.")
    else:
        print(f"El equipo '{equipo.nombre}' ya estaba disponible.")


def ver_historial(inventario):
    print("\n=== HISTORIAL DE PRÉSTAMOS ===")
    if not inventario:
        print("No hay equipos registrados.")
        return

    for nombre, equipo in inventario.items():
        print(f"\nEquipo: {nombre}")
        if not equipo.historial:
            print("  Sin préstamos registrados.")
            continue
        for indice, prestamo in enumerate(equipo.historial, start=1):
            print(f"  {indice}. {prestamo}")


def agregar_equipo(inventario):
    nombre_equipo = input("\nIngrese el nombre del nuevo equipo: ").strip()

    if not nombre_equipo:
        print("El nombre del equipo no puede estar vacío.")
        return

    if nombre_equipo in inventario:
        print("Ese equipo ya existe en el inventario.")
        return

    inventario[nombre_equipo] = Equipo(nombre_equipo)
    print(f"Equipo '{nombre_equipo}' agregado exitosamente.")


def menu():
    inventario = {
        "Portatil-01": Equipo("Portatil-01"),
        "Portatil-02": Equipo("Portatil-02"),
        "VideoBeam-01": Equipo("VideoBeam-01"),
    }

    while True:
        print("\n===== SISTEMA DE PRÉSTAMOS DE EQUIPOS =====")
        print("1. Ver equipos disponibles")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial de préstamos")
        print("5. Agregar nuevo equipo")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            mostrar_equipos(inventario)
        elif opcion == "2":
            registrar_prestamo(inventario)
        elif opcion == "3":
            devolver_equipo(inventario)
        elif opcion == "4":
            ver_historial(inventario)
        elif opcion == "5":
            agregar_equipo(inventario)
        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
