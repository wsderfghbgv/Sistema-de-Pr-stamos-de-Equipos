"""
Replica de ejemplos del material de estudio (version fiel y ejecutable).
Se mantienen nombres y estructura de los ejemplos del texto.
"""

import datetime
import hashlib
import math
import re


# ==========================================================
# Concepto teorico de clase y objeto
# ==========================================================
class Coche:
    pass


mi_coche = Coche()
coche_de_amigo = Coche()


class Libro:
    pass


libro_python = Libro()
novela_fantasia = Libro()


# ==========================================================
# Clase y constructor
# ==========================================================
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


ana = Persona("Ana Garcia", 28)
juan = Persona("Juan Lopez", 35)


class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


laptop = Producto("Laptop XPS", 1200)
teclado = Producto("Teclado mecanico", 80, 15)


class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.area = ancho * alto
        self.perimetro = 2 * (ancho + alto)


rect = Rectangulo(5, 3)


class Cuenta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self.saldo = saldo_inicial


cuenta_ana = Cuenta("Ana Garcia", 1000)


class LibroBiblioteca:
    def __init__(self, titulo, autor, paginas, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.isbn = isbn
        self.disponible = disponible
        self.pagina_actual = 0


libro1 = LibroBiblioteca("Python Crash Course", "Eric Matthes", 544, "9781593279288")
libro2 = LibroBiblioteca("Clean Code", "Robert C. Martin", 464, "9780132350884", False)


class Fecha:
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    @classmethod
    def desde_texto(cls, texto):
        dia, mes, anio = map(int, texto.split("-"))
        return cls(dia, mes, anio)

    @classmethod
    def hoy(cls):
        fecha_actual = datetime.date.today()
        return cls(fecha_actual.day, fecha_actual.month, fecha_actual.year)


fecha1 = Fecha(15, 3, 2023)
fecha2 = Fecha.desde_texto("25-12-2023")
fecha3 = Fecha.hoy()


# ==========================================================
# Atributos
# ==========================================================
class Estudiante:
    universidad = "Universidad Autonoma"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.activo = True


estudiante1 = Estudiante("Maria", 20)
estudiante2 = Estudiante("Carlos", 22)


class ProductoAtributoClase:
    impuesto = 0.21

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class CocheAtributos:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometraje = 0


class PersonaDinamica:
    def __init__(self, nombre):
        self.nombre = nombre


juan_dinamico = PersonaDinamica("Juan")
juan_dinamico.edad = 30
juan_dinamico.profesion = "Ingeniero"


class CuentaBancaria:
    tasa_interes = 0.03

    def __init__(self, titular, saldo_inicial, pin):
        self.titular = titular
        self._saldo = saldo_inicial
        self.__pin = pin

    def verificar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado


class Temperatura:
    def __init__(self):
        self._celsius = 0

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        self.celsius = (valor - 32) * 5 / 9


class RectanguloProp:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self):
        return self.ancho * self.alto

    @property
    def perimetro(self):
        return 2 * (self.ancho + self.alto)


class Ejemplo:
    """Clase de ejemplo para mostrar atributos especiales"""

    def __init__(self, valor):
        self.valor = valor


# ==========================================================
# Metodos
# ==========================================================
class CocheMetodos:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.encendido = False
        self.velocidad_maxima = 200

    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"{self.marca} {self.modelo} encendido"
        return f"{self.marca} {self.modelo} ya estaba encendido"

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            return f"{self.marca} {self.modelo} apagado"
        return f"{self.marca} {self.modelo} ya estaba apagado"

    def acelerar(self, incremento):
        if not self.encendido:
            return f"No se puede acelerar: {self.marca} {self.modelo} esta apagado"
        nueva_velocidad = self.velocidad + incremento
        if nueva_velocidad > self.velocidad_maxima:
            self.velocidad = self.velocidad_maxima
            return f"Velocidad maxima alcanzada: {self.velocidad} km/h"
        self.velocidad = nueva_velocidad
        return f"Velocidad actual: {self.velocidad} km/h"

    def frenar(self, decremento):
        if self.velocidad == 0:
            return "El coche ya esta detenido"
        nueva_velocidad = self.velocidad - decremento
        if nueva_velocidad < 0:
            self.velocidad = 0
            return "Coche detenido"
        self.velocidad = nueva_velocidad
        return f"Velocidad actual: {self.velocidad} km/h"


class CuentaBancariaMetodos:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial

    def consultar_saldo(self):
        return f"Saldo actual de {self.titular}: ${self._saldo}"

    def depositar(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a depositar debe ser positiva"
        self._saldo += cantidad
        return f"Deposito de ${cantidad} realizado. Nuevo saldo: ${self._saldo}"

    def retirar(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a retirar debe ser positiva"
        if cantidad > self._saldo:
            return "Fondos insuficientes"
        self._saldo -= cantidad
        return f"Retiro de ${cantidad} realizado. Nuevo saldo: ${self._saldo}"


class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: Division por cero"
        return a / b

    def calcular_estadisticas(self, numeros):
        if not numeros:
            return {"suma": 0, "promedio": 0, "minimo": None, "maximo": None}
        return {
            "suma": sum(numeros),
            "promedio": sum(numeros) / len(numeros),
            "minimo": min(numeros),
            "maximo": max(numeros),
        }


class PersonaMetodos:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def presentarse(self):
        estado = "mayor" if self.es_mayor_de_edad() else "menor"
        return f"Hola, soy {self.nombre_completo()} y soy {estado} de edad."


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

    def __eq__(self, otro):
        return isinstance(otro, Punto) and self.x == otro.x and self.y == otro.y

    def __len__(self):
        return abs(self.x) + abs(self.y)


class MathUtils:
    @staticmethod
    def es_primo(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("El factorial no esta definido para numeros negativos")
        if n == 0 or n == 1:
            return 1
        return n * MathUtils.factorial(n - 1)


class Empleado:
    num_empleados = 0

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.num_empleados += 1

    @classmethod
    def desde_salario_anual(cls, nombre, salario_anual):
        salario_mensual = salario_anual / 12
        return cls(nombre, salario_mensual)

    @classmethod
    def obtener_num_empleados(cls):
        return cls.num_empleados


# ==========================================================
# Encapsulacion - Atributos privados, getters/setters,
# propiedades y metodos privados
# ==========================================================
class PersonaGetSet:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacia")

    def get_edad(self):
        return self._edad

    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and 0 <= nueva_edad <= 120:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un entero entre 0 y 120")


class Círculo:
    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError("El radio debe ser positivo")
        self._radio = valor

    @property
    def área(self):
        return math.pi * self._radio ** 2

    @property
    def perímetro(self):
        return 2 * math.pi * self._radio


class Autenticador:
    def __init__(self, usuario, contraseña):
        self._usuario = usuario
        self._contraseña_hash = self.__generar_hash(contraseña)

    def __generar_hash(self, contraseña):
        return hashlib.sha256(contraseña.encode()).hexdigest()

    def verificar_contraseña(self, contraseña_ingresada):
        hash_ingresado = self.__generar_hash(contraseña_ingresada)
        return hash_ingresado == self._contraseña_hash


class Formulario:
    def __init__(self):
        self._datos = {}
        self._errores = {}

    def validar(self, datos):
        self._datos = datos.copy()
        self._errores = {}
        self.__validar_campos_requeridos()
        self.__validar_email()
        self.__validar_contraseña()
        self.__validar_edad()
        return len(self._errores) == 0

    def obtener_errores(self):
        return self._errores.copy()

    def __validar_campos_requeridos(self):
        campos_requeridos = ["nombre", "email", "contraseña"]
        for campo in campos_requeridos:
            if campo not in self._datos or not self._datos[campo]:
                self._errores[campo] = f"El campo {campo} es obligatorio"

    def __validar_email(self):
        if "email" in self._datos and self._datos["email"]:
            patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            if not re.match(patron, self._datos["email"]):
                self._errores["email"] = "El formato del email no es valido"

    def __validar_contraseña(self):
        if "contraseña" in self._datos and self._datos["contraseña"]:
            contraseña = self._datos["contraseña"]
            if len(contraseña) < 8:
                self._errores["contraseña"] = "La contraseña debe tener al menos 8 caracteres"
            elif not any(c.isupper() for c in contraseña):
                self._errores["contraseña"] = "La contraseña debe contener al menos una mayuscula"
            elif not any(c.isdigit() for c in contraseña):
                self._errores["contraseña"] = "La contraseña debe contener al menos un numero"

    def __validar_edad(self):
        if "edad" in self._datos:
            try:
                edad = int(self._datos["edad"])
                if edad < 18:
                    self._errores["edad"] = "Debes ser mayor de edad"
                elif edad > 120:
                    self._errores["edad"] = "La edad ingresada no es valida"
            except ValueError:
                self._errores["edad"] = "La edad debe ser un numero"


def main():
    print("Replica de ejemplos del texto cargada correctamente.")
    print("Instancias de ejemplo creadas:", isinstance(mi_coche, Coche), isinstance(ana, Persona))
    t = Temperatura()
    t.celsius = 25
    print("Temperatura prueba:", t.celsius, t.fahrenheit)


if __name__ == "__main__":
    main()
