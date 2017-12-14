import sqlite3
import user_choice
import add_client

base = sqlite3.connect('c:\sqlite\empernar.db')
cur = base.cursor()

def bienvenida():

    print("Bienvenido/a Sr/a. cliente: ")
    print("1 - Ingrese '1' para iniciar sesión.")
    print("1 - Ingrese '2' para registrarse.")

    choice = int(input())

    if choice == 1:
        dni = input("Ingrese su dni: ")
        cur.execute('select ID_CLIENTE, NOMBRE from CLIENTES where DNI = "{}"'.format(dni))
        resp = cur.fetchall()
        confirm = input("Es usted: " + str(resp) + "? (Y/N): ").upper()

        if confirm == "Y":
            print("Visualise, elija y decida opciones para su viaje: ")
            user_choice.verTablas()
        elif confirm == "N":
            bienvenida()
        else:
            print("Ingrese un valor valido, por favor.")

    elif choice == 2:
        add_client.agregarCliente()
        bienvenida()

    elif choice != type(int):
        print("Ingrese un valor valido, por favor.")