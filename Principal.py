import os
from xml.dom import minidom
import xml.etree.ElementTree as ET
from lista_circular import ListaCircular
from lista_orto import ListaOrtogonal

Matrices = []
Lista = ListaCircular()



def ordenarDatos(dato,n,m):
    Datos = []
    for i in range(1,n+1):
        for j in range(1,m+1):
            for k in range(0,(n*m)):
                if dato[k].get("x") == i and dato[k].get("y")==j:
                    Datos.append(dato[k].get("num"))
    return Datos


def CargarArchivo():
    global Matrices, Matriz
    print("OPCIÓN CARGAR ARCHIVOS")
    ruta = str(input("Ingrese la ruta del archivo: "))
    tree = ET.parse(ruta)
    root = tree.getroot()
    i = 0
    nombres = []
    for elem in root:
        Matriz = []
        error = False
        nueva = True
        if elem.tag == "matriz":
            n = int(elem.attrib.get('n'))
            m = int(elem.attrib.get('m'))
            nombre = str(elem.attrib.get('nombre'))
            for nom in range(0,len(nombres)):
                if nombres[nom] == nombre:
                    print("error, la matriz "+nombre+" ya existe")
                    nueva = False
                    i = i + 1
            if nueva == True:
                nombres.append(nombre)
                i = i + 1
                Temp = []
                for node in root.findall('matriz['+str(i)+']/dato'):
                    x = int(node.attrib.get('x'))
                    y = int(node.attrib.get('y'))
                    num = int(node.text)
                    if x <= n and y <= m: 
                        dato = {"x":x, "y":y, "num":num}
                        Temp.append(dato)
                    else:
                        error = True
                if error:
                    print("***Error, la matriz "+nombre+" excede el limite de filas o columnas ")
                Mati = ordenarDatos(Temp,n,m)
                ListaO = ListaOrtogonal()
                ListaO.CrearMatriz(n,m,Mati)
                Lista.Agregar(ListaO,nombre)
    print("El archivo ha sido leido correctamente")
                        

def ProcesarArchivos():
    print("OPCIÓN PROCESAR ARCHIVOS")
    Lista.Procesar()

def EscribirArchivo():
    print("OPCIÓN ESCRIBIR ARCHIVOS DE SALIDA")
    Lista.Salida()

def MostrarDatos():
    print("OPCIÓN MOSTRAR DATOS DEL ESTUDIANTE")
    print("Katheryn Darleny Yuman Oscal")
    print("201902209")
    print("Introducción a la Programacion y Computación 2 sección \"B\"")
    print("Ingenieria en Ciencias y Sistemas")
    print("5to Semestre")

def GenerarGrafica():
    print("OPCIÓN GENERAR GRÁFICA")
    Lista.ElegirNombre()
def menu():
    print("MENÚ PRINCIPAL:")
    print("1 - Cargar archivo")
    print("2 - Procesar archivos")
    print("3 - Escribir archivo de salida")
    print("4 - Mostar datos del estudiante")
    print("5 - Generar grafica")
    print("6 - Salir")
    op = input("Elija una opcion:")
    return op

while True:
    op = menu()
    os.system("cls")
    if op == "1":
        CargarArchivo()
    elif op == "2":
        ProcesarArchivos()
    elif op == "3":
        EscribirArchivo()  
    elif op == "4":
        MostrarDatos()
    elif op == "5":
        GenerarGrafica()
    elif op == "6":
        break
    else:
        print("Opcion no valida")
    input("")

    



