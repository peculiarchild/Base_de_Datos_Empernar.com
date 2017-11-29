import sqlite3
import user_choice
import add_client
import welcome

base = sqlite3.connect('d:\sqlite\empernar1.db')
cur = base.cursor()


print("Por favor elija una opción: ")
print("1 - Ingrese Sesión o registre un nuevo usuario")
print("2 - Visualise opciones de viaje (Ciudades/Hoteles/Itinerarios)")
print("3 - Si ya decidió su vieja ingrese el n° de Itinerario")
#print("4 - OPCIÓN EN MANTENIMIENTO")

option = int(input())



def main():
    if option == 1:
        welcome.bienvenida()
    elif option == 2:
        user_choice.verTablas()
    elif option == 3:
        print("hola")
    elif option == 4:
        print("hola")
    else:
        print("Ingrese una opción valida, por favor.")

print(main())

