from rich.table import Table
from rich.console import Console
from libreria.calculadora import (contador_calculos, contador_categoria_A, contador_categoria_E,
                         acumulador_monto_pagar, acumulador_categoria_B, acumulador_monto_1000)


console = Console()

def mostrar_reporte():
    table = Table(title="Reporte de Cálculos")
    table.add_column("Descripción", justify="center", style="bold")
    table.add_column("Cantidad", justify="center")

    table.add_row("Total de cálculos realizados", str(contador_calculos))
    table.add_row("Cálculos con Categoría A", str(contador_categoria_A))
    table.add_row("Cálculos con Categoría E", str(contador_categoria_E))
    table.add_row("Monto acumulado a pagar", f"S/. {acumulador_monto_pagar:,.2f}")
    table.add_row("Monto acumulado categoría B", f"S/. {acumulador_categoria_B:,.2f}")
    table.add_row("Monto acumulado ≥ 1000", f"S/. {acumulador_monto_1000:,.2f}")
    
    console.print(table)
