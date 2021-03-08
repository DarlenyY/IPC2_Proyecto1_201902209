import os
from xml.dom import minidom
import xml.etree.ElementTree as ET
from lista_circular import ListaCircular
from lista_orto import ListaOrtogonal
import time

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
    print("----------------------")
    while True:
        ruta = str(input("Ingrese la ruta del archivo: "))
        try:
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
                            time.sleep(1)
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
                            print("error, la matriz "+nombre+" excede el limite de filas o columnas ")
                            time.sleep(1)
                        Mati = ordenarDatos(Temp,n,m)
                        ListaO = ListaOrtogonal()
                        ListaO.CrearMatriz(n,m,Mati)
                        Lista.Agregar(ListaO,nombre)
            print("***SE TERMINO DE LEER EL ARCHIVO***")
            break
        except:
            print("***La ruta no es valida***")
            print(" ")
                        

def ProcesarArchivos():
    print("OPCIÓN PROCESAR ARCHIVOS")
    print("------------------------")
    try:
        Lista.Procesar()
    except:
        print("Ocurrio un error")

def EscribirArchivo():
    print("OPCIÓN ESCRIBIR ARCHIVOS DE SALIDA")
    print("----------------------------------")
    Lista.Salida()

def MostrarDatos():
    print("OPCIÓN MOSTRAR DATOS DEL ESTUDIANTE")
    print("-----------------------------------")
    print("Katheryn Darleny Yuman Oscal")
    print("201902209")
    print("Introducción a la Programacion y Computación 2 sección \"B\"")
    print("Ingenieria en Ciencias y Sistemas")
    print("5to Semestre")

def GenerarGrafica():
    print("OPCIÓN GENERAR GRÁFICA")
    print("----------------------")
    try:
        Lista.ElegirNombre()
    except:
        print("Ocurrio un error")

def menu():
    print("MENÚ PRINCIPAL:")
    print("--------------------------------")
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
    print(" ")
    input("Presione enter")
    os.system("cls")


    



