from menu import mostrar_menu
from registro import registrar_venta
from reporte import generar_reporte

# Lista global para almacenar las ventas
ventas = []

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            registrar_venta(ventas)
        elif opcion == "2":
            generar_reporte(ventas)
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

