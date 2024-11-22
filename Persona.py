from persistent import Persistent

class Persona(Persistent):
    def __init__(self, nombre:str, edad:int, genero:str, telefono:str, direccion:str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.telefono = telefono
        self.direccion = direccion

    def consultar_informacion(self):
        return (f"Nombre: {self.nombre}\n Edad: {self.edad}\n Género: {self.genero}\n Teléfono: {self.telefono}\n Dirección: {self.direccion}")
