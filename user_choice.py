import sqlite3

base = sqlite3.connect('d:\sqlite\empernar1.db')
cur = base.cursor()

def verTablas():

    tablaUsuario = input("Ingrese una opción (Ciudades/Hoteles/Itinerarios): ").upper()
    cur.execute('SELECT * FROM {};'.format(tablaUsuario))
    resp = cur.fetchall()
    for i in resp:
        print(i)

def definirItinerario():

    origen = input("Ingrese el numero de su ciudad de origen: ")
    cur.execute('SELECT CIUDADES FROM CIUDADES WHERE ID_CIUDAD = {};'.format(origen))
    resp = cur.fetchall()
    return resp
print(definirItinerario())