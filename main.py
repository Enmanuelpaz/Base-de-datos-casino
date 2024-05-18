```python
# Crear una lista vacÃ­a para almacenar informaciÃ³n de los usuarios
usuarios_casino = []

# FunciÃ³n para agregar un nuevo usuario con su respectivo puntaje
def agregar_usuario(nombre, puntaje):
    usuario = {
        "nombre": nombre,
        "puntaje": puntaje
    }
    usuarios_casino.append(usuario)

# FunciÃ³n para mostrar todos los usuarios y sus puntajes
def mostrar_usuarios():
    for usuario in usuarios_casino:
        print(f"Nombre: {usuario['nombre']} - Puntaje: {usuario['puntaje']}")

# Ejemplo de uso:
agregar_usuario("Juan", 100)
agregar_usuario("Maria", 150)
agregar_usuario("Pedro", 80)

mostrar_usuarios()
```

Este cÃ³digo en Python crea una lista donde se pueden almacenar la informaciÃ³n de usuarios del casino, incluyendo su nombre y puntaje. Luego, se definen funciones para agregar un nuevo usuario y mostrar la lista de usuarios con sus puntajes. Finalmente, se realiza un ejemplo de uso agregando usuarios y mostrando la informaciÃ³n almacenada.