#ejrcicio 2 
"""Desarrollar un sistema de gestión de contactos, en el cual se debe crear dos clases,
Contacto y Agenda, para gestionar los contactos de una agenda. El objetivo es permitir al
usuario realizar operaciones básicas como añadir, buscar, editar y listar contactos. Además,
el programa debe finalizar correctamente cuando el usuario lo solicite.

Clase Contacto
La clase debe tener los atributos privados de nombre, teléfono y email.
Métodos de la clase
● Constructor
● Método mágico que retorne una cadena con el nombre, teléfono y email del
contacto.
● Otro método que permite modificar el nombre, teléfono o email de un contacto. Solo
los datos que se proporcionen deben ser modificados.

Clase Agenda
La clase debe tener un atributo que almacene una lista pública de contactos.
Métodos de la clase
● Crear método que permita añadir un nuevo contacto a la agenda.
● Agregar método que muestre todos los contactos en la agenda.
● Un método para buscar un contacto en la agenda por nombre y lo muestra.
● Agregar un método para buscar un contacto por nombre y editar sus datos.
● Por último, crear un método que finalice el programa.
El programa debe mostrar un menú con las siguientes opciones: ● Añadir contactos ● Listar contactos ● Buscar contactos ● Editar contactos ● Cerrar agenda"""
class Contacto:
    def __init__(self, __nombre, __telefono, __email):
        self.__nombre = __nombre
        self.__telefono = __telefono
        self.__email = __email

    def __str__(self):
        return (f"El contacto cuyo nombre es: {self.__nombre}, teléfono: {self.__telefono}, Email: {self.__email}")

    def modificar_datos(self, nuevo_nom='', nuevo_tel='', nuevo_email=''):
        if nuevo_nom:
            self.__nombre = nuevo_nom
        if nuevo_tel:
            self.__telefono = nuevo_tel
        if nuevo_email:
            self.__email = nuevo_email
        return f"Datos actualizados: {self.__nombre}, teléfono: {self.__telefono}, Email: {self.__email}"


class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, contacto):
        self.contactos.append(contacto)
        print(f"Contacto {contacto} añadido a la agenda.")

    def mostrar_contactos(self):
        if len(self.contactos) == 0:
            print("No hay contactos en la agenda.")
        else:
            print("Contactos en la agenda:")
            for contacto in self.contactos:
                print(contacto)

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto._Contacto__nombre.lower() == nombre.lower():
                return contacto
        print("Contacto no encontrado.")
        return None

    def editar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            nuevo_nombre = input("Ingrese nuevo nombre (deje en blanco para no modificar): ")
            nuevo_telefono = input("Ingrese nuevo teléfono (deje en blanco para no modificar): ")
            nuevo_email = input("Ingrese nuevo email (deje en blanco para no modificar): ")
            contacto.modificar_datos(
                nuevo_nom=nuevo_nombre,
                nuevo_tel=nuevo_telefono,
                nuevo_email=nuevo_email
            )
            print("Contacto actualizado.")

    def cerrar_agenda(self):
        print("Cerrando agenda. Hasta luego.")
        exit()


def menu():
    agenda = Agenda()
    while True:
        print("\n--- Menú ---")
        print("1. Añadir contactos")
        print("2. Listar contactos")
        print("3. Buscar contactos")
        print("4. Editar contactos")
        print("5. Cerrar agenda")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del contacto: ")
            telefono = input("Teléfono del contacto: ")
            email = input("Email del contacto: ")
            contacto = Contacto(nombre, telefono, email)
            agenda.añadir_contacto(contacto)
        elif opcion == '2':
            agenda.mostrar_contactos()
        elif opcion == '3':
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            agenda.buscar_contacto(nombre)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del contacto a editar: ")
            agenda.editar_contacto(nombre)
        elif opcion == '5':
            agenda.cerrar_agenda()
        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    menu()
