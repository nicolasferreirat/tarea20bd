from Persona import Persona
from Agenda import Agenda
from AgendaDAO import AgendaDAO


class Main:
    def __init__(self):
        self.dao = AgendaDAO()

    def ejecutar(self):
        while True:
            contactos = self.dao.obtener_contactos() 

            print("\n___Opciones___")
            print("1. Agregar contacto: ")
            print("2. Listar contactos")
            print("3. Actualizar contacto: ")
            print("4. Eliminar contacto: ")
            
            # la opcion 5 se muestra solo si el usuario agregó un contacto a la agenda
            if contactos:
                print("5. Salir")
            else:
                print("5. (Deshabilitada: No hay contactos en la agenda)")

            opcion = input("---> Elige una opción: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                genero = input("Género: ")
                telefono = input("Teléfono: ")
                direccion = input("Dirección: ")

                persona = Persona(nombre, edad, genero, telefono, direccion)
                self.dao.agregar_contacto(persona)
                print("Contacto agregado.")

            elif opcion == "2":
                if not contactos:
                    print("No hay contactos en la agenda.")
                else:
                    for contacto in contactos:
                        print(contacto.consultar_informacion())
                        print("-------------------------------------------------------")

            elif opcion == "3":
                if not contactos:
                    print("No hay contactos para actualizar.")
                else:
                    nombre = input("Ingrese el nombre del contacto a actualizar: ")
                    edad = int(input("Ingrese la edad: "))
                    genero = input("Ingrese el género: ")
                    telefono = input("Ingrese el teléfono: ")
                    direccion = input("Ingrese la dirección: ")

                    persona_actualizada = Persona(nombre, edad, genero, telefono, direccion)
                    self.dao.actualizar_contacto(nombre, persona_actualizada)

            elif opcion == "4":
                if not contactos:
                    print("No hay contactos para eliminar.")
                else:
                    nombre = input("Ingrese el nombre del contacto a eliminar: ")
                    self.dao.eliminar_contacto(nombre)

            elif opcion == "5":
                if not contactos:
                    print("No puedes salir, agrega al menos un contacto.")
                else:
                    print("Saliendo...")
                    self.dao.cerrar()
                    break

            else:
                print("Opción no válida. Intenta nuevamente.")



if __name__ == "__main__":
    app = Main()
    app.ejecutar()
