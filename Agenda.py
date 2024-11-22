from persistent import Persistent
import transaction

class Agenda(Persistent):
    def __init__(self):
        self.listaPersonas = []  
        self.numContactos = 0

    def agregarContacto(self, persona):
        self.listaPersonas.append(persona)
        self.numContactos += 1
        transaction.commit()  

    def mostrarDatos(self):
        for persona in self.listaPersonas:
            print(persona.consultar_informacion())
