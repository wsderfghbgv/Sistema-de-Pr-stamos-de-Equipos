# GA1-220501093-04-AA1-EV04

Fundamentos de Python: Clases, Objetos y Encapsulación.

## Estructura del repositorio

- `taller_clases_objetos.py`: solución del Taller de Clases y Objetos.
- `taller_encapsulacion.py`: solución del Taller de Encapsulación con propiedades.
- `prestamos_equipos.py`: reto integrador "Sistema de Préstamos de Equipos" con POO.

## 1) Taller de Clases y Objetos

Se implementa la clase `Libro` con:

- Atributos: `titulo`, `autor`, `paginas`, `disponible`.
- Métodos: `prestar()`, `devolver()`, `informacion()`.
- Pruebas en `main()` con dos objetos diferentes.

### Ejecución

```bash
python taller_clases_objetos.py
```

## 2) Taller de Encapsulación

Se implementa la clase `CuentaBancaria` con encapsulación de datos:

- Atributos privados: `_titular` y `_saldo`.
- Propiedad de solo lectura: `titular`.
- Propiedad de lectura/escritura: `saldo` con validación de no-negatividad.
- Métodos de negocio:
  - `depositar(cantidad)` retorna `True/False`.
  - `retirar(cantidad)` retorna `True/False`.

### Ejecución

```bash
python taller_encapsulacion.py
```

## 3) Proyecto integrador: Sistema de Préstamos de Equipos

El proyecto se desarrolló aplicando Programación Orientada a Objetos:

- Clase `Equipo`: maneja disponibilidad e historial de préstamos.
- Clase `Usuario`: representa la persona que solicita el préstamo.
- Clase `Prestamo`: modela cada préstamo con usuario y fecha.

También se aplican colecciones:

- **Diccionario** para inventario de equipos.
- **Lista** para historial por equipo.
- **Tupla** en `Prestamo.como_tupla()` con formato `(usuario, fecha)`.

### Funciones implementadas

- `mostrar_equipos(inventario)`
- `registrar_prestamo(inventario)`
- `devolver_equipo(inventario)`
- `ver_historial(inventario)`
- `agregar_equipo(inventario)`
- `menu()`

### Ejecución

```bash
python prestamos_equipos.py
```

## Ejemplo de uso en consola (resumen)

1. Ver inventario inicial.
2. Registrar préstamo de `Portatil-01` para un usuario.
3. Consultar historial.
4. Devolver equipo.
5. Agregar un nuevo equipo.

## Lógica aplicada

Se separó la lógica de negocio en clases para mejorar organización, reutilización y legibilidad.  
El control de estado del préstamo se encapsuló en métodos de la clase `Equipo`, evitando modificaciones directas desde fuera.  
El flujo interactivo se dejó en funciones de menú para facilitar mantenimiento y pruebas manuales.

## Reflexión personal

Durante esta actividad se fortaleció el modelado de problemas reales con POO en Python. Se comprendió mejor cómo el encapsulamiento protege datos sensibles y cómo las propiedades permiten validar cambios de forma controlada. Además, integrar listas, tuplas y diccionarios en un solo proyecto ayudó a consolidar una solución práctica y escalable.
