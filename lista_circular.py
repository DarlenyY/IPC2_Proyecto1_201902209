from nodo import Nodo
from lista_orto import ListaOrtogonal
import xml.etree.cElementTree as ET

class ListaCircular():
    def __init__ (self):
        self.primero = None
        self.ultimo = None
    
    def vacia(self):
        return self.primero == None

    def Agregar(self,dato,nombre):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato,nombre)
            self.ultimo.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato,nombre)
            self.ultimo.siguiente = self.primero
        
    def Recorrer(self):
        aux = self.primero
        if aux != None :
            while aux.siguiente != self.primero:
                print(aux.nombre)
                aux.dato.MostrarMat()
                aux = aux.siguiente
            print(aux.nombre) 
            aux.dato.MostrarMat()
        else:
            print("No hay datos")  

    def Ordenar(self,dato,patron,m):
        n = len(patron)
        dato = dato
        Datos = []
        Res = []
        for i in range(1,n+1):
            for j in range(1,m+1):
                for k in range(0,(n*m)):
                    if dato[k].get("x") == i and dato[k].get("y")==j:
                        dic = {"x":i, "y":j,"num":dato[k].get("num")}
                        Datos.append(dic)
        Res = [Datos]
        Res.extend([patron,m])
        return Res

    def Sett (self,dato,aux):
        aux = aux
        aux.setReducida(dato)

    def gett (self):
        aux = self.primero
        if aux != None :
            while aux.siguiente != self.primero:
                print(aux.nombre) 
                dat = aux.getReducida()
                aux = aux.siguiente
                print(dat) 
            print(aux.nombre) 
            dat = aux.getReducida()
            print(dat)
    
    def Procesar(self):
        aux = self.primero
        if aux != None:
            while aux.siguiente != self.primero:
                procesar = aux.dato.Patron()
                m = procesar[2]
                Datos = self.Ordenar(procesar[0],procesar[1],m)
                self.Sett(Datos,aux)
                aux = aux.siguiente
            procesar = aux.dato.Patron()
            m = procesar[2]
            Datos = self.Ordenar(procesar[0],procesar[1],m)
            self.Sett(Datos,aux)  
        else:
            print("***No se ha cargado ningun archivo de entrada")
        self.gett()

    def ElegirNombre(self):
        nombres = []
        aux = self.primero
        auxi = self.primero
        busq = None
        if(aux != None):
            while aux.siguiente != self.primero:
                nombres.append(aux.nombre)
                aux = aux.siguiente
            nombres.append(aux.nombre) 
            for i in range(1,len(nombres)+1):
                print(str(i)+"-"+nombres[i-1])
            elegido = int(input("Elija una opción: "))
            for i in range(1,len(nombres)+1):
                if elegido == i:
                    busq = nombres[i-1]
            if(auxi != None):           
                while auxi.siguiente != self.primero:
                    if busq == auxi.nombre:
                        nn = auxi.dato.NoFilas()
                        mm = auxi.dato.NoColumnas()
                        auxi.dato.Grafo(busq,mm,nn)
                        auxi.dato.MostrarMat()
                    auxi = auxi.siguiente
                    if busq == auxi.nombre and auxi.siguiente ==self.primero:
                        auxi.dato.MostrarMat()
                        nn = auxi.dato.NoFilas()
                        mm = auxi.dato.NoColumnas()
                        auxi.dato.Grafo(busq,mm,nn)
                        
                        
        else:
            print("***No se a cargado ningun archivo de entrada")
 
    def Salida(self,ruta):
        aux = self.primero
        if aux != None:
            if aux.getReducida() != None :
                root = ET.Element("matrices")
                while aux.siguiente != self.primero:
                    print(aux.nombre)
                    dat = aux.getReducida()
                    print(dat)
                    num = dat[0]
                    patron = dat[1]
                    m = dat[2]
                    g = len(patron)
                    matriz = ET.SubElement(root, "matriz", nombre=aux.nombre, n=str(g), m=str(m), g=str(g))
                    for i in num:
                        dato = ET.SubElement(matriz, "dato", x=str(i.get("x")), y=str(i.get("y")))
                        dato.text = str(i.get("num"))
                    j = 0
                    for i in patron:
                        j = j + 1
                        f = len(i)
                        frecu = ET.SubElement(matriz, "frecuencia", g=str(j))
                        frecu.text = str(f)
                    aux = aux.siguiente
                print(aux.nombre) 
                dat = aux.getReducida()
                print(dat)

                num = dat[0]
                patron = dat[1]
                m = dat[2]
                g = len(patron)
                matriz = ET.SubElement(root, "matriz", nombre=aux.nombre, n=str(g), m=str(m), g=str(g))
                for i in num:
                    dato = ET.SubElement(matriz, "dato", x=str(i.get("x")), y=str(i.get("y")))
                    dato.text = str(i.get("num"))
                j = 0
                for i in patron:
                    j = j + 1
                    f = len(i)
                    frecu = ET.SubElement(matriz, "frecuencia", g=str(j))
                    frecu.text = str(f)

                arbol = ET.ElementTree(root)
                arbol.write(ruta+"/ArchivoDeSalida.xml")
            else:
                print("***El archivo no ha sido procesado")  
        else:
             print("***No se ha cargado ningun archivo de entrada")  


                 

