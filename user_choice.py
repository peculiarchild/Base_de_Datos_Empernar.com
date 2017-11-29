import sqlite3

base = sqlite3.connect('d:\sqlite\empernar1.db')
cur = base.cursor()

def verTablas():

    tablaUsuario = input("Ingrese una opción (Ciudades/Hoteles/Itinerarios): ").upper()
    cur.execute('SELECT * FROM {};'.format(tablaUsuario))
    resp = cur.fetchall()
    for i in resp:
        print(i)

