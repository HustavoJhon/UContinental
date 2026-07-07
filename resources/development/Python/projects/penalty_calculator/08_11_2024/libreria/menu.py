from rich.console import Console
from libreria.calculadora import calcular_penalidad
from libreria.reporte import mostrar_reporte
from rich.markdown import Markdown


console = Console()

def mostrar_menu():
    project = """Organización Reguladora Ambiental"""
    title_evidence = Markdown(f"""# {project}""")

    console.print(title_evidence)
    console.print("[bold blue]=== MENÚ PRINCIPAL ===[/bold blue]")
    console.print("1. Calcular")
    console.print("2. Reportar Contador y Acumulador")
    console.print("3. Salir")

def menu_principal():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-3): ").strip()

        if opcion == "1":
            try:
                monto_base = float(input("Ingresa el Monto Base en dólares: "))
                if monto_base <= 0:
                    console.print("[bold red]El monto base debe ser mayor que 0.[/bold red]")
                    continue
                categoria = input("Ingresa la Categoría (A, B, C, D, E): ").strip().upper()
                tipo_cambio = float(input("Ingresa el tipo de cambio a soles: "))
                if tipo_cambio <= 0:
                    console.print("[bold red]El tipo de cambio debe ser mayor que 0.[/bold red]")
                    continue
            except ValueError:
                console.print("[bold red]Por favor ingresa valores válidos.[/bold red]")
                continue

            monto_base_soles, monto_penalidad, monto_pagar = calcular_penalidad(monto_base, categoria, tipo_cambio)

            if monto_base_soles > 0:
                console.print(f"[bold green]Ruido en Decibeles: Más de 200" if categoria == "E" else f"[bold green]Ruido en Decibeles: {categoria}[/bold green]")
                console.print(f"[bold cyan]Monto Base en Soles: S/. {monto_base_soles:,.2f}[/bold cyan]")
                console.print(f"[bold yellow]Monto de Penalidad en Soles: S/. {monto_penalidad:,.2f}[/bold yellow]")
                console.print(f"[bold magenta]Monto a Pagar en Soles: S/. {monto_pagar:,.2f}[/bold magenta]")

        elif opcion == "2":
            mostrar_reporte()

        elif opcion == "3":
            console.print("[bold red]Gracias por usar el programa...[/bold red]")
            break
        else:
            console.print("[bold red]Opción no válida. Por favor elige una opción entre 1 y 3.[/bold red]")
