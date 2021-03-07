class Nodo():
    def __init__ (self,dato,nombre):
        self.dato = dato
        self.nombre = nombre
        self.reducida = None
        self.siguiente = None
    
    def setReducida(self,reducida):
        self.reducida = reducida

    def getReducida(self):
        return self.reducida