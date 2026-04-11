from .reader import read_logs
from .processor import process_data
from .analyzer import analyze_data
from .report import create_report


def mostrar_menu():
    while True:
        print("MENÚ PRINCIPAL")
        print("1. Leer logs")
        print("2. Procesar datos")
        print("3. Analizar datos")
        print("4. Generar reporte")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        match opcion:
            case "1":
                print("Leyendo logs...")
                read_logs()

            case "2":
                print("Procesando datos...")
                process_data()

            case "3":
                print("Analizando datos...")
                analyze_data()

            case "4":
                print("Generando reporte...")
                create_report()

            case "5":
                print("Saliendo del programa.")
                break

            case _:
                print("Opción inválida, intenta de nuevo.")



    mostrar_menu()
``