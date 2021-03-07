class Nodo1():
    def __init__ (self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
        self.abajo = None
        self.arriba = None
        if dato == 0:
            self.binaria = 0
        else:
            self.binaria = 1

    def Mostrar(self):
        print(str(self.dato)+"-"+str(self.binaria), end = " ")

    def MostrarR(self):
        print(str(self.dato), end = " ")
        
    def getDato(self):
        return self.dato

    def getBinaria(self):
        return self.binaria