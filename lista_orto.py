from nodo1 import Nodo1
import os
import time
class ListaOrtogonal():
    def __init__ (self):
        self.inicio = None
        
    def CrearMatriz(self,n,m,Datos):
        q = None
        s = None
        k = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                nuevoNodo = Nodo1(Datos[k])
                k = k + 1
                nuevoNodo.siguiente = None
                nuevoNodo.abajo = None
                if j == 1:
                    nuevoNodo.anterior = None
                    if self.inicio == None:
                        self.inicio = nuevoNodo
                    q = nuevoNodo
                else:
                    nuevoNodo.anterior = q
                    q.siguiente = nuevoNodo
                    q = nuevoNodo
                if i == 1:
                    nuevoNodo.arriba = None
                    q = nuevoNodo
                else:
                    nuevoNodo.arriba = s
                    s.abajo = nuevoNodo
                    s = s.siguiente
            s = self.inicio
            while s.abajo != None:
                s = s.abajo

    def MostrarMat(self):
        if self.inicio != None:
            aux = self.inicio
            while aux != None:
                auxi = aux
                while auxi != None:
                    auxi.Mostrar()
                    auxi = auxi.siguiente
                aux = aux.abajo
                print("")

    def MostrarRedu(self):
        if self.inicio != None:
            aux = self.inicio
            while aux != None:
                auxi = aux
                while auxi != None:
                    auxi.MostrarR()
                    auxi = auxi.siguiente
                aux = aux.abajo
                print("")
                
    def CrearNodo(self,Id,Name,Shape,Color):
        return Id + "[label=\"" + Name + "\" shape="+ Shape +", style=filled, fillcolor = " + Color +"]\n"

    def UnirNodo(self,A,B):
        return A + "->" + B +"\n"

    def NoFilas(self):
        pp = self.inicio
        fila = 0
        while pp.abajo != None:
            fila = fila + 1
            pp = pp.abajo
        fila = fila + 1
        return fila

    def NoColumnas(self):
        pp = self.inicio
        colum = 0
        while pp.siguiente != None:
            colum = colum + 1
            pp = pp.siguiente
        colum = colum + 1
        return colum

    def Grafo(self,t,mm,nn):
        inicio = self.inicio
        p = inicio
        q = self.inicio
        cont = 0
        t = t
        mm = mm
        nn = nn
        file = open("Reporte.dot","w")
        file.write("digraph Tarea1{\n")
        file.write(self.CrearNodo("M","Matrices","circle","\"#B3BE30\""))
        file.write(self.CrearNodo("titulo",str(t),"circle","\"#B3BE30\""))
        file.write(self.CrearNodo("n","n="+str(nn),"circle","\"#B3BE30\""))
        file.write(self.CrearNodo("m","m="+str(mm),"circle","\"#B3BE30\""))
        file.write(self.UnirNodo("M","titulo"))
        file.write(self.UnirNodo("titulo","n"))
        file.write(self.UnirNodo("titulo","m"))
        for j in range(1,mm+1):
            for i in range(1,nn+1):
                while p.abajo != None:
                    if p == inicio:
                        file.write(self.CrearNodo(str(cont),str(p.getDato()),"circle","\"#B3BE30\""))
                        cont = cont + 1
                        file.write(self.CrearNodo(str(cont),str(p.abajo.getDato()),"circle","\"#B3BE30\""))
                        file.write(self.UnirNodo(str(cont-1),str(cont))) 
                        file.write(self.UnirNodo("titulo",str(cont-1))) 
                    else:
                        cont = cont + 1
                        file.write(self.CrearNodo(str(cont),str(p.abajo.getDato()),"circle","\"#B3BE30\""))
                        file.write(self.UnirNodo(str(cont-1),str(cont)))
                    p = p.abajo
            inicio = q.siguiente
            p = inicio
            q = q.siguiente
            cont = cont + 3
        file.write("}")
        file.close()
        os.system("dot -Tpng Reporte.dot -o Grafo.png")
        print("La grafica se Genero exitosamente")

    def Suma(self,patron):
        p = self.inicio
        q = None
        m = int(self.NoColumnas())
        datos = []
        num = 0
        for i in range(1,m+1):
            for i in patron:
                for j in i:
                    q = p
                    k = 1
                    while q.abajo != None:
                        if k == j:
                            num = num + int(q.getDato())
                        k = k + 1
                        q = q.abajo
                    if q.abajo == None:
                        if k == j:
                            num = num + int(q.getDato())
                datos.append(num)
                num = 0
            p = p.siguiente
        x = 0
        y = 1
        bien = []
        print("Sumando truplas...")
        time.sleep(1)
        for i in range(0,len(datos)):
            x = x + 1
            dic = {"x": x, "y":y, "num":datos[i]}
            if x == len(patron):
                x = 0
                y = y + 1
            bien.append(dic)
            dat = [bien,patron,m]
        return dat
            

            
    def Patron(self):
        inicio = self.inicio
        p = inicio
        q = None
        r = None
        s = None
        match = True
        cont = None
        i = 1
        coincidencias = []
        rep = []
        pos = []
        l = True
        print("Calculando matriz binaria...")
        time.sleep(1)
        while p.abajo != None:
            for o in rep:
                if o == i:
                    l = False
            cont = i+1
            q = p
            r = p.abajo
            if l:
                while r.abajo != None:
                    s = r
                    while s.siguiente != None:   
                        if q.getBinaria() != s.getBinaria():
                            match = False
                        s = s.siguiente
                        q = q.siguiente
                    if s.siguiente == None and match == True:
                        if q.getBinaria() == s.getBinaria():
                            rep.append(cont)
                            pos.append(cont)
                    r = r.abajo
                    q = p
                    cont = cont + 1
                    match = True
                if r.abajo == None:
                    s = r
                    while s.siguiente != None:
                        if q.getBinaria() != s.getBinaria():
                            match = False
                        s = s.siguiente
                        q = q.siguiente
                    if s.siguiente == None and match == True:
                        if q.getBinaria() == s.getBinaria():
                            rep.append(cont)
                            pos.append(cont)
                pos.insert(0,i)
                coincidencias.append(pos)
            i = i + 1
            l = True
            p = p.abajo
            pos = []
        suma = self.Suma(coincidencias)
        return suma


