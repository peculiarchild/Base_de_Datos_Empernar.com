import sqlite3

from random import randint

base = sqlite3.connect('c:\sqlite\empernar.db')
cur = base.cursor()

def verTablas():

    tablaUsuario = input("Ingrese una opción (Ciudades/Hoteles): ").upper()
    cur.execute('SELECT * FROM {};'.format(tablaUsuario))
    resp = cur.fetchall()
    for i in resp:
        print(i)


def generarNumeroDeVuelo():

    origen = input("Ingrese su ciudad de origen: ").upper()
    cur.execute('SELECT CIUDADES FROM CIUDADES WHERE ID_CIUDAD = {};'.format(origen))
    resp = cur.fetchall()
    destino = input("Ingrese su ciudad de destino: ").upper()
    cur.execute('SELECT CIUDADES FROM CIUDADES WHERE ID_CIUDAD = {};'.format(destino))
    resp2 = cur.fetchall()
    confirm = input("¿Usted quisiera viajar desde {} hasta {}? (Y/N): ".format(resp, resp2))
    confirm = confirm.upper()
    if confirm == "Y":
        randomnum = randint(0,10000)
        print('El número de tu vuelo es: "{}"'.format(randomnum))

    elif confirm == "N":
        generarNumeroDeVuelo()

#print(generarNumeroDeVuelo())