import sqlite3
base = sqlite3.connect('c:\sqlite\empernar.db')
cur = base.cursor()

print("Por favor elija una opción: ")
print("1 - Ingrese Sesión o registre un nuevo usuario")
print("2 - Visualise opciones de viaje (Ciudades/Hoteles/Itinerarios)")
print("3 - Si ya decidió su vieja ingrese el n° de Itinerario")
#print("4 - OPCIÓN EN MANTENIMIENTO")

option = int(input())


def main():
    if option == 1:
        bienvenida()
    elif option == 2:
        verTablas()
    elif option == 3:
        print("hola")
    elif option == 4:
        print("hola")
    else:
        print("Ingrese una opción valida, por favor.")


def bienvenida():

    print("Bienvenido/a Sr/a. cliente: ")
    print("1 - Ingrese '1' para iniciar sesión")
    print("1 - Ingrese '2' para registrarse")

    choice = int(input())

    if choice == 1:
        dni = input("Ingrese su dni: ")
        cur.execute('select ID_CLIENTE, NOMBRE from CLIENTES where DNI = "{}"'.format(dni))
        resp = cur.fetchall()
        confirm = input("Es usted: " + str(resp) + "? (Y/N): ").upper()

        if confirm == "Y":
            print("Visualise, elija y decida opciones para su viaje: ")
            verTablas()
        elif confirm == "N":
            bienvenida()
        else:
            print("Ingrese un valor valido, por favor.")

    elif choice == 2:
        agregarCliente()
        bienvenida()

    elif choice != type(int):
        print("Ingrese un valor valido, por favor.")


def verTablas():

    tablaUsuario = input("Ingrese una opción (Ciudades/Hoteles/Itinerarios): ").upper()
    cur.execute('SELECT * FROM {};'.format(tablaUsuario))
    resp = cur.fetchall()
    for i in resp:
        print(i)


def agregarCliente():

   sel = input('Ingrese nombre de cliente nuevo: ').upper()
   dni = input('Ingrese su dni: ')
   cur.execute('INSERT INTO CLIENTES (NOMBRE, DNI) VALUES("{}", "{}")'.format(sel, dni))
   base.commit()

print(main())