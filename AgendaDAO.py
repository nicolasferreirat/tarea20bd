from ZODB import DB
from ZODB.FileStorage import FileStorage
from Agenda import Agenda
import transaction

class AgendaDAO:
    def __init__(self, db_path='agenda.fs'):
        self.storage = FileStorage(db_path)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

        if 'agenda' not in self.root:
            self.root['agenda'] = Agenda()

        self.agenda = self.root['agenda']

    def agregar_contacto(self, persona):
        self.agenda.agregarContacto(persona)
        transaction.commit()

    def obtener_contactos(self):
        return self.agenda.listaPersonas

    def actualizar_contacto(self, nombre, persona_actualizada):
        for i, persona in enumerate(self.agenda.listaPersonas):
            if persona.nombre == nombre:
                self.agenda.listaPersonas[i] = persona_actualizada
                transaction.commit()
                print(f"Contacto {nombre} actualizado.")
                return
        print(f"Contacto {nombre} no encontrado.")

    def eliminar_contacto(self, nombre):
        for i, persona in enumerate(self.agenda.listaPersonas):
            if persona.nombre == nombre:
                del self.agenda.listaPersonas[i]
                transaction.commit()
                print(f"Contacto {nombre} eliminado.")
                return
        print(f"Contacto {nombre} no encontrado.")

    def listar_contactos(self):
        return self.agenda.listaPersonas

    def cerrar(self):
        self.connection.close()
        self.db.close()
