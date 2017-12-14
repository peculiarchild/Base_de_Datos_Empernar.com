import sqlite3
import user_choice
import welcome


base = sqlite3.connect('c:\sqlite\empernar.db')
cur = base.cursor()





def main():
    print("Por favor elija una opción: ")
    print("1 - Ingrese Sesión o registre un nuevo usuario.")
    print("2 - Visualise opciones de viaje (Ciudades/Hoteles).")
    print("3 - Si ya decidió su viaje ingrese para reservar su vuelo.")

    option = int(input())

    if option == 1:
        welcome.bienvenida()

    elif option == 2:
        user_choice.verTablas()
        main()

    elif option == 3:
        user_choice.generarNumeroDeVuelo()

    else:
        print("Ingrese una opción valida, por favor.")

print(main())

