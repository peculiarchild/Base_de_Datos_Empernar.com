import sqlite3

base = sqlite3.connect('d:\sqlite\empernar1.db')
cur = base.cursor()


def agregarCliente():

   sel = input('Ingrese nombre de cliente nuevo: ').upper()
   dni = input('Ingrese su dni: ')
   cur.execute('INSERT INTO CLIENTES (NOMBRE, DNI) VALUES("{}", "{}")'.format(sel, dni))
   base.commit()

