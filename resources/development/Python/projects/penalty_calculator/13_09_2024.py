#!/usr/bin/env
# Author: JHON GUSTAVO CCARITA VELASQUEZ
# Date: 13/09/2024

#? Elaborar un programa para una organizacion reguladora ambiental, e ingresar: Monto Base en dolares, categori, ruido en decibeles, porcentaje de penalidad (segun la tabla) y tipo de cambio a soles; para mostrar el monto base en soles, el monto de penalidad y el monto a pagar, ambos en soles, para una entidad.

#! Indicadores
#* 1. Ingresar todas las variables requeridas, segun el tipo de dato que corresponde.
#* 2. Realizar el calculo del monto base convertido a soles en su respectiva variable.
#* 3. Realizar el calculo del monto de penalidad en su respectiva variable.
#* 4. Realizar el calculo del monto de pagar en su respectiva variable.
#* 5. Muestra las variables solicitadas, segun el tipo de dato que corresponde.

# pip install rich
import os
from rich import print, box
from rich.table import Table

def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_noise_categories():
    """Display noise categories with rich."""
    noise_table = Table(title="Noise Categories", box=box.SIMPLE)
    
    noise_table.add_column("Category", justify="center", style="cyan", no_wrap=True)
    noise_table.add_column("Description", justify="center", style="green")
    noise_table.add_column("Penalty (%)", justify="center", style="red")

    noise_table.add_row("A", "(50 or less)", "5%")
    noise_table.add_row("B", "(51 - 70)", "7%")
    noise_table.add_row("C", "(71 - 90)", "9%")
    noise_table.add_row("D", "(91 - 110)", "12%")
    noise_table.add_row("E", "(More than 110)", "15%")
    
    print(noise_table)

def calculate_penalty(category, amount_soles):
    """Calculate the penalty based on the category."""
    penalty_percentages = {
        'a': 5,
        'b': 7,
        'c': 9,
        'd': 12,
        'e': 15
    }
    
    if category in penalty_percentages:
        penalty = amount_soles * penalty_percentages[category] / 100
        return penalty
    return None

def check_amount_range(category, amount_dollars):
    """Check if the entered amount in dollars is within the valid range for the category."""
    ranges = {
        'a': (0, 50),
        'b': (51, 70),
        'c': (71, 90),
        'd': (91, 110),
        'e': (111, float('inf'))
    }
    
    min_value, max_value = ranges[category]
    return min_value <= amount_dollars <= max_value

def show_results(category, amount_soles, penalty, amount_to_pay):
    """Display calculation results with rich."""
    results_table = Table(title=f"Results for Category {category.upper()}", box=box.MINIMAL_DOUBLE_HEAD)
    
    results_table.add_column("Description", justify="left", style="bold")
    results_table.add_column("Amount (S/.)", justify="right", style="bold green")
    
    results_table.add_row("Base amount in soles", f"S/. {amount_soles:.2f}")
    results_table.add_row("Penalty amount", f"S/. {penalty:.2f}")
    results_table.add_row("Total amount to pay", f"S/. {amount_to_pay:.2f}")
    
    print(results_table)

while True:
    try:
        # Clear console at the start
        clear_console()
        
        # Program description
        print("[bold red]TEST 1[/bold red]")
        print("[italic blue]This program calculates the penalty amount for an entity based on a noise category and a base amount in dollars.[/italic blue]\n")

        show_noise_categories()

        # Input data
        category = input("Enter the noise category:\t\t").lower()
        if category not in ['a', 'b', 'c', 'd', 'e']:
            print("[bold red]Error: Please enter a valid category (A, B, C, D, E).[/bold red]")
            continue

        base_amount_dollars = float(input("Enter the base amount in dollars:\t"))

        # Validate if the amount in dollars is within the range of the category
        if not check_amount_range(category, base_amount_dollars):
            min_value, max_value = {
                'a': ("50 or less"),
                'b': ("between 51 and 70"),
                'c': ("between 71 and 90"),
                'd': ("between 91 and 110"),
                'e': ("more than 110")
            }[category]
            print(f"[bold red]Error: For category {category.upper()}, the base amount in dollars must be {min_value}.[/bold red]")
            continue

        # Convert dollars to soles
        exchange_rate = 3.77
        amount_soles = base_amount_dollars * exchange_rate

        # Calculate penalty
        penalty = calculate_penalty(category, amount_soles)
        
        # Calculate total amount to pay
        amount_to_pay = amount_soles - penalty

        # Clear console before showing results
        clear_console()

        # Show results
        show_results(category, amount_soles, penalty, amount_to_pay)

    except ValueError:
        print("[bold red]Error: Please enter a valid numeric value for the amount.[/bold red]")
    
    # Option to continue or exit
    repeat = input("Do you want to perform another calculation? (y/n): ").lower()
    if repeat != 'y':
        clear_console()
        print("[bold green]Thank you for using the program. Goodbye![/bold green]")
        break   

'''
# Función principal para calcular las penalidades
def calcular_penalidad(monto_base_usd, porcentaje_penalidad, tipo_cambio):
    # Convertir el monto base de dólares a soles
    monto_base_soles = monto_base_usd * tipo_cambio
    
    # Calcular el monto de penalidad en soles
    monto_penalidad_soles = monto_base_soles * (porcentaje_penalidad / 100)
    
    # Calcular el monto total a pagar en soles
    monto_total_soles = monto_base_soles + monto_penalidad_soles
    
    # Mostrar resultados
    print(f"Monto base en soles: S/ {monto_base_soles:.2f}")
    print(f"Monto de penalidad en soles: S/ {monto_penalidad_soles:.2f}")
    print(f"Monto total a pagar en soles: S/ {monto_total_soles:.2f}")
    
    return monto_base_soles, monto_penalidad_soles, monto_total_soles

# Solicitar los datos al usuario
monto_base_usd = float(input("Ingrese el monto base en dólares: "))
categoria = input("Ingrese la categoría: ")
ruido_decibeles = float(input("Ingrese el ruido en decibeles: "))
porcentaje_penalidad = float(input("Ingrese el porcentaje de penalidad: "))
tipo_cambio = float(input("Ingrese el tipo de cambio (de USD a soles): "))

# Llamar a la función para realizar el cálculo
calcular_penalidad(monto_base_usd, porcentaje_penalidad, tipo_cambio)
'''


