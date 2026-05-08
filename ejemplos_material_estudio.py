"""
Ejemplos del material de estudio:
Fundamentos de Python - Clases, Objetos y Encapsulación.

Este archivo reúne ejemplos prácticos en un solo lugar para facilitar
la validación en consola.
"""

from __future__ import annotations

from datetime import date
import math
import hashlib
import re


# =========================================================
# 1) CONCEPTO DE CLASE Y OBJETO
# =========================================================
class CochePlano:
    pass


class LibroPlano:
    pass


# =========================================================
# 2) CLASE Y CONSTRUCTOR
# =========================================================
class PersonaConstructor:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad


class ProductoConstructor:
    def __init__(self, nombre: str, precio: float, stock: int = 0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


class RectanguloConstructor:
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto
        self.area = ancho * alto
        self.perimetro = 2 * (ancho + alto)


class CuentaValidada:
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self.saldo = saldo_inicial


class LibroBibliotecaCtor:
    def __init__(
        self,
        titulo: str,
        autor: str,
        paginas: int,
        isbn: str,
        disponible: bool = True,
    ):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.isbn = isbn
        self.disponible = disponible
        self.pagina_actual = 0


class Fecha:
    def __init__(self, dia: int, mes: int, anio: int):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    @classmethod
    def desde_texto(cls, texto: str) -> "Fecha":
        dia, mes, anio = map(int, texto.split("-"))
        return cls(dia, mes, anio)

    @classmethod
    def hoy(cls) -> "Fecha":
        actual = date.today()
        return cls(actual.day, actual.month, actual.year)


# =========================================================
# 3) ATRIBUTOS
# =========================================================
class Estudiante:
    universidad = "Universidad Autonoma"

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
        self.activo = True


class ProductoImpuesto:
    impuesto = 0.21

    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio


class CocheAtributos:
    def __init__(self, marca: str, modelo: str, color: str):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometraje = 0


class PersonaDinamica:
    def __init__(self, nombre: str):
        self.nombre = nombre


class CuentaBancariaVisibilidad:
    tasa_interes = 0.03

    def __init__(self, titular: str, saldo_inicial: float, pin: str):
        self.titular = titular
        self._saldo = saldo_inicial
        self.__pin = pin

    def verificar_pin(self, pin_ingresado: str) -> bool:
        return self.__pin == pin_ingresado


class Temperatura:
    def __init__(self):
        self._celsius = 0.0

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, valor: float):
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor: float):
        self.celsius = (valor - 32) * 5 / 9


class RectanguloCalculado:
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self) -> float:
        return self.ancho * self.alto

    @property
    def perimetro(self) -> float:
        return 2 * (self.ancho + self.alto)


class EjemploEspecial:
    """Clase de ejemplo para atributos especiales."""

    def __init__(self, valor):
        self.valor = valor


# =========================================================
# 4) METODOS
# =========================================================
class CocheMetodos:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.encendido = False
        self.velocidad_maxima = 200

    def encender(self) -> str:
        if not self.encendido:
            self.encendido = True
            return f"{self.marca} {self.modelo} encendido"
        return f"{self.marca} {self.modelo} ya estaba encendido"

    def apagar(self) -> str:
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            return f"{self.marca} {self.modelo} apagado"
        return f"{self.marca} {self.modelo} ya estaba apagado"

    def acelerar(self, incremento: int) -> str:
        if not self.encendido:
            return f"No se puede acelerar: {self.marca} {self.modelo} esta apagado"
        nueva_velocidad = self.velocidad + incremento
        if nueva_velocidad > self.velocidad_maxima:
            self.velocidad = self.velocidad_maxima
            return f"Velocidad maxima alcanzada: {self.velocidad} km/h"
        self.velocidad = nueva_velocidad
        return f"Velocidad actual: {self.velocidad} km/h"

    def frenar(self, decremento: int) -> str:
        if self.velocidad == 0:
            return "El coche ya esta detenido"
        self.velocidad = max(0, self.velocidad - decremento)
        return "Coche detenido" if self.velocidad == 0 else f"Velocidad actual: {self.velocidad} km/h"


class CuentaBancariaMetodos:
    def __init__(self, titular: str, saldo_inicial: float = 0):
        self.titular = titular
        self._saldo = saldo_inicial

    def consultar_saldo(self) -> str:
        return f"Saldo actual de {self.titular}: ${self._saldo}"

    def depositar(self, cantidad: float) -> str:
        if cantidad <= 0:
            return "La cantidad a depositar debe ser positiva"
        self._saldo += cantidad
        return f"Deposito de ${cantidad} realizado. Nuevo saldo: ${self._saldo}"

    def retirar(self, cantidad: float) -> str:
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
        return "Error: Division por cero" if b == 0 else a / b

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
    def __init__(self, nombre: str, apellido: str, edad: int):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido}"

    def es_mayor_de_edad(self) -> bool:
        return self.edad >= 18

    def presentarse(self) -> str:
        estado = "mayor" if self.es_mayor_de_edad() else "menor"
        return f"Hola, soy {self.nombre_completo()} y soy {estado} de edad."


class Punto:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, otro: "Punto"):
        return Punto(self.x + otro.x, self.y + otro.y)

    def __eq__(self, otro):
        return isinstance(otro, Punto) and self.x == otro.x and self.y == otro.y

    def __len__(self):
        return abs(self.x) + abs(self.y)


class MathUtils:
    @staticmethod
    def es_primo(n: int) -> bool:
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
    def factorial(n: int) -> int:
        if n < 0:
            raise ValueError("El factorial no esta definido para negativos")
        if n in (0, 1):
            return 1
        return n * MathUtils.factorial(n - 1)


class Empleado:
    num_empleados = 0

    def __init__(self, nombre: str, salario: float):
        self.nombre = nombre
        self.salario = salario
        Empleado.num_empleados += 1

    @classmethod
    def desde_salario_anual(cls, nombre: str, salario_anual: float):
        return cls(nombre, salario_anual / 12)

    @classmethod
    def obtener_num_empleados(cls):
        return cls.num_empleados


class LibroLectura:
    def __init__(self, titulo: str, autor: str, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.pagina_actual = 0
        self.abierto = False

    def abrir(self):
        if self.abierto:
            return f"{self.titulo} ya esta abierto"
        self.abierto = True
        return f"{self.titulo} ha sido abierto"

    def cerrar(self):
        if not self.abierto:
            return f"{self.titulo} ya esta cerrado"
        self.abierto = False
        return f"{self.titulo} ha sido cerrado"

    def leer(self, num_paginas: int):
        if not self.abierto:
            return f"No puedes leer: {self.titulo} esta cerrado"
        if self.pagina_actual >= self.paginas:
            return f"Ya has terminado de leer {self.titulo}"
        paginas_a_leer = min(num_paginas, self.paginas - self.pagina_actual)
        self.pagina_actual += paginas_a_leer
        if self.pagina_actual >= self.paginas:
            return f"Has leido {paginas_a_leer} paginas y has terminado {self.titulo}"
        return f"Has leido {paginas_a_leer} paginas. Estas en la pagina {self.pagina_actual} de {self.paginas}"

    def reiniciar_lectura(self):
        self.pagina_actual = 0
        return f"Has reiniciado la lectura de {self.titulo}"

    def __str__(self):
        estado = "abierto" if self.abierto else "cerrado"
        progreso = f"{self.pagina_actual}/{self.paginas} paginas"
        return f"{self.titulo} por {self.autor} - {progreso} - {estado}"


# =========================================================
# 5) ENCAPSULACION - ATRIBUTOS PRIVADOS
# =========================================================
class CuentaBancariaPrivada:
    def __init__(self, titular: str, saldo_inicial: float, pin: str):
        self._titular = titular
        self._saldo = saldo_inicial
        self.__pin = pin

    def validar_pin(self, pin_ingresado: str) -> bool:
        return self.__pin == pin_ingresado


class Vehiculo:
    def __init__(self, marca: str, modelo: str):
        self._marca = marca
        self.__modelo = modelo


class CocheHerencia(Vehiculo):
    def __init__(self, marca: str, modelo: str, puertas: int):
        super().__init__(marca, modelo)
        self._puertas = puertas

    def info(self):
        return f"Marca: {self._marca}"


# =========================================================
# 6) GETTERS Y SETTERS
# =========================================================
class PersonaGetSet:
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre: str):
        if not isinstance(nuevo_nombre, str) or not nuevo_nombre:
            raise ValueError("El nombre debe ser una cadena no vacia")
        self._nombre = nuevo_nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, nueva_edad: int):
        if not isinstance(nueva_edad, int) or not 0 <= nueva_edad <= 120:
            raise ValueError("La edad debe ser un entero entre 0 y 120")
        self._edad = nueva_edad


class ProductoGetSet:
    def __init__(self, nombre: str, precio: float, stock: int = 0):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock
        self._descuento = 0.0

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio * (1 - self._descuento)

    def get_precio_base(self):
        return self._precio

    def get_stock(self):
        return self._stock

    def get_descuento(self):
        return self._descuento

    def set_nombre(self, nuevo_nombre: str):
        if not isinstance(nuevo_nombre, str) or not nuevo_nombre:
            raise ValueError("El nombre debe ser una cadena no vacia")
        self._nombre = nuevo_nombre

    def set_precio(self, nuevo_precio: float):
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            raise ValueError("El precio debe ser un numero positivo")
        self._precio = float(nuevo_precio)

    def set_stock(self, nuevo_stock: int):
        if not isinstance(nuevo_stock, int) or nuevo_stock < 0:
            raise ValueError("El stock debe ser un entero positivo")
        self._stock = nuevo_stock

    def set_descuento(self, nuevo_descuento: float):
        if not isinstance(nuevo_descuento, float) or not 0 <= nuevo_descuento <= 1:
            raise ValueError("El descuento debe ser un numero entre 0 y 1")
        self._descuento = nuevo_descuento


class Electronico(ProductoGetSet):
    def __init__(self, nombre: str, precio: float, stock: int, garantia_meses: int):
        super().__init__(nombre, precio, stock)
        self._garantia_meses = garantia_meses
        self._activado = False

    def get_garantia_meses(self):
        return self._garantia_meses

    def esta_activado(self):
        return self._activado

    def set_garantia_meses(self, meses: int):
        if not isinstance(meses, int) or meses < 0:
            raise ValueError("Los meses de garantia deben ser un entero positivo")
        self._garantia_meses = meses

    def activar(self):
        self._activado = True

    def desactivar(self):
        self._activado = False

    def set_precio(self, nuevo_precio: float):
        super().set_precio(nuevo_precio)
        if nuevo_precio > 1000:
            self._garantia_meses = max(self._garantia_meses, 24)


# =========================================================
# 7) PROPIEDADES
# =========================================================
class TemperaturaProp:
    def __init__(self, celsius: float = 0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor: float):
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor: float):
        celsius = (valor - 32) * 5 / 9
        if celsius < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = celsius


class PersonaProp:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._amigos = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not isinstance(valor, str) or not valor:
            raise ValueError("El nombre debe ser una cadena no vacia")
        self._nombre = valor

    @property
    def amigos(self):
        return self._amigos.copy()

    @amigos.deleter
    def amigos(self):
        self._amigos = []


class Circulo:
    def __init__(self, radio: float):
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor: float):
        if valor <= 0:
            raise ValueError("El radio debe ser positivo")
        self._radio = valor

    @property
    def area(self):
        return math.pi * self._radio**2

    @property
    def perimetro(self):
        return 2 * math.pi * self._radio


class EmpleadoProp:
    def __init__(self, nombre: str, salario_base: float, horas_extra: int = 0, tarifa_extra: float = 0):
        self._nombre = nombre
        self._salario_base = salario_base
        self._horas_extra = horas_extra
        self._tarifa_extra = tarifa_extra

    @property
    def nombre(self):
        return self._nombre

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, valor):
        if valor < 0:
            raise ValueError("El salario base no puede ser negativo")
        self._salario_base = valor

    @property
    def horas_extra(self):
        return self._horas_extra

    @horas_extra.setter
    def horas_extra(self, valor):
        if valor < 0:
            raise ValueError("Las horas extra no pueden ser negativas")
        self._horas_extra = valor

    @property
    def tarifa_extra(self):
        return self._tarifa_extra

    @tarifa_extra.setter
    def tarifa_extra(self, valor):
        if valor < 0:
            raise ValueError("La tarifa extra no puede ser negativa")
        self._tarifa_extra = valor

    @property
    def salario_total(self):
        return self._salario_base + (self._horas_extra * self._tarifa_extra)


class ProductoProp:
    def __init__(self, nombre: str, precio: float):
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

    @property
    def info(self):
        return f"{self._nombre}: {self._precio}€"


class ProductoDigital(ProductoProp):
    def __init__(self, nombre: str, precio: float, tamano_mb: float):
        super().__init__(nombre, precio)
        self._tamano_mb = tamano_mb

    @property
    def tamano_mb(self):
        return self._tamano_mb

    @tamano_mb.setter
    def tamano_mb(self, valor: float):
        if valor <= 0:
            raise ValueError("El tamano debe ser positivo")
        self._tamano_mb = valor

    @property
    def info(self):
        return f"{self._nombre}: {self._precio}€ ({self._tamano_mb} MB)"


# =========================================================
# 8) METODOS PRIVADOS
# =========================================================
class Autenticador:
    def __init__(self, usuario: str, contrasena: str):
        self._usuario = usuario
        self._contrasena_hash = self.__generar_hash(contrasena)

    def __generar_hash(self, contrasena: str):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    def verificar_contrasena(self, contrasena_ingresada: str):
        return self.__generar_hash(contrasena_ingresada) == self._contrasena_hash


class ProcesadorTexto:
    def __init__(self):
        self._texto = ""
        self._estadisticas = {}

    def procesar_texto(self, texto: str):
        self._texto = self.__normalizar_texto(texto)
        self._estadisticas = self.__calcular_estadisticas(self._texto)
        return True

    def __normalizar_texto(self, texto: str):
        texto = texto.lower()
        texto = re.sub(r"[^\w\s]", "", texto)
        texto = re.sub(r"\s+", " ", texto).strip()
        return texto

    def __calcular_estadisticas(self, texto: str):
        palabras = texto.split()
        return {
            "total_palabras": len(palabras),
            "palabras_unicas": len(set(palabras)),
            "longitud_promedio": (sum(len(p) for p in palabras) / len(palabras)) if palabras else 0,
        }

    def obtener_estadisticas(self):
        return self._estadisticas.copy()

    def obtener_texto_procesado(self):
        return self._texto


class Forma:
    def __init__(self):
        self._tipo = "Forma generica"

    def calcular_area(self):
        return self._obtener_area()

    def _obtener_area(self):
        raise NotImplementedError("Las subclases deben implementar este metodo")

    def _validar_dimensiones(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("Las dimensiones deben ser numeros positivos")
        return True


class CirculoForma(Forma):
    def __init__(self, radio):
        super().__init__()
        self._tipo = "Circulo"
        self._validar_dimensiones(radio)
        self._radio = radio

    def _obtener_area(self):
        return math.pi * self._radio**2


class RectanguloForma(Forma):
    def __init__(self, ancho, alto):
        super().__init__()
        self._tipo = "Rectangulo"
        self._validar_dimensiones(ancho)
        self._validar_dimensiones(alto)
        self._ancho = ancho
        self._alto = alto

    def _obtener_area(self):
        return self._ancho * self._alto


class Formulario:
    def __init__(self):
        self._datos = {}
        self._errores = {}

    def validar(self, datos: dict):
        self._datos = datos.copy()
        self._errores = {}
        self.__validar_campos_requeridos()
        self.__validar_email()
        self.__validar_contrasena()
        self.__validar_edad()
        return len(self._errores) == 0

    def obtener_errores(self):
        return self._errores.copy()

    def __validar_campos_requeridos(self):
        campos = ["nombre", "email", "contrasena"]
        for campo in campos:
            if campo not in self._datos or not self._datos[campo]:
                self._errores[campo] = f"El campo {campo} es obligatorio"

    def __validar_email(self):
        email = self._datos.get("email", "")
        if email and not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            self._errores["email"] = "El formato del email no es valido"

    def __validar_contrasena(self):
        contrasena = self._datos.get("contrasena", "")
        if not contrasena:
            return
        if len(contrasena) < 8:
            self._errores["contrasena"] = "La contraseña debe tener al menos 8 caracteres"
        elif not any(c.isupper() for c in contrasena):
            self._errores["contrasena"] = "La contraseña debe contener al menos una mayuscula"
        elif not any(c.isdigit() for c in contrasena):
            self._errores["contrasena"] = "La contraseña debe contener al menos un numero"

    def __validar_edad(self):
        if "edad" not in self._datos:
            return
        try:
            edad = int(self._datos["edad"])
            if edad < 18:
                self._errores["edad"] = "Debes ser mayor de edad"
            elif edad > 120:
                self._errores["edad"] = "La edad ingresada no es valida"
        except ValueError:
            self._errores["edad"] = "La edad debe ser un numero"


def main():
    print("=== EJEMPLOS DEL MATERIAL DE ESTUDIO ===")

    # Concepto clase/objeto
    mi_coche = CochePlano()
    coche_amigo = CochePlano()
    print(f"Instancias CochePlano creadas: {id(mi_coche) != id(coche_amigo)}")

    # Constructor
    ana = PersonaConstructor("Ana Garcia", 28)
    print(f"PersonaConstructor: {ana.nombre}, {ana.edad}")
    fecha = Fecha.desde_texto("25-12-2023")
    print(f"Fecha desde texto: {fecha.dia}/{fecha.mes}/{fecha.anio}")

    # Atributos
    est = Estudiante("Maria", 20)
    print(f"Estudiante: {est.nombre}, universidad: {est.universidad}")
    temp = Temperatura()
    temp.celsius = 25
    print(f"Temperatura: {temp.celsius}C = {temp.fahrenheit}F")

    # Metodos
    coche = CocheMetodos("Toyota", "Corolla")
    print(coche.encender())
    print(coche.acelerar(50))
    print(coche.frenar(50))

    # Encapsulacion
    cuenta = CuentaBancariaPrivada("Ana", 1000, "1234")
    print(f"PIN correcto: {cuenta.validar_pin('1234')}")

    # Getters / setters
    p = PersonaGetSet("Laura", 29)
    p.set_edad(30)
    print(f"PersonaGetSet edad: {p.get_edad()}")

    # Propiedades
    c = Circulo(5)
    print(f"Circulo area: {c.area:.2f}")

    # Metodos privados
    auth = Autenticador("admin", "Secreta123")
    print(f"Autenticacion: {auth.verificar_contrasena('Secreta123')}")
    procesador = ProcesadorTexto()
    procesador.procesar_texto("Hola, HOLA mundo mundo!")
    print(f"Estadisticas texto: {procesador.obtener_estadisticas()}")

    print("=== FIN DE DEMOSTRACION ===")


if __name__ == "__main__":
    main()
