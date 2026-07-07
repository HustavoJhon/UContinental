# Diccionario de precios por tipo de servicio
PRECIOS = {1: 80.0, 2: 100.0, 3: 120.0}

# Diccionario de descuentos según la cantidad de pasajes
DESCUENTOS = {1: 0.0, 2: 0.1, 6: 0.15, 11: 0.2}

def calcular_descuento(cantidad):
    if cantidad == 1:
        return DESCUENTOS[1]
    elif 2 <= cantidad <= 5:
        return DESCUENTOS[2]
    elif 6 <= cantidad <= 10:
        return DESCUENTOS[6]
    else:
        return DESCUENTOS[11]

def registrar_venta(ventas):
    print("\n--- Registro de Venta ---")
    
    while True:
        try:
            tipo_cliente = int(input("Ingrese el tipo de cliente (1 o 2): "))
            if tipo_cliente in [1, 2]:
                break
            else:
                print("Error: Tipo de cliente debe ser 1 o 2.")
        except ValueError:
            print("Error: Ingrese un número válido.")

    while True:
        try:
            cantidad_pasajes = int(input("Ingrese la cantidad de pasajes (mayor a 0): "))
            if cantidad_pasajes > 0:
                break
            else:
                print("Error: La cantidad debe ser mayor a 0.")
        except ValueError:
            print("Error: Ingrese un número válido.")

    while True:
        genero = input("Ingrese el género del cliente (M o F): ").upper()
        if genero in ["M", "F"]:
            break
        else:
            print("Error: El género debe ser 'M' o 'F'.")

    while True:
        try:
            tipo_servicio = int(input("Ingrese el tipo de servicio (1-Imperial, 2-VIP, 3-Gold): "))
            if tipo_servicio in [1, 2, 3]:
                break
            else:
                print("Error: Tipo de servicio inválido.")
        except ValueError:
            print("Error: Ingrese un número válido.")

    precio = PRECIOS[tipo_servicio]
    descuento = calcular_descuento(cantidad_pasajes)
    importe_bruto = cantidad_pasajes * precio
    monto_descuento = importe_bruto * descuento
    importe_neto = importe_bruto - monto_descuento

    ventas.append({
        "tipo_cliente": tipo_cliente,
        "cantidad_pasajes": cantidad_pasajes,
        "genero": genero,
        "tipo_servicio": tipo_servicio,
        "importe_bruto": importe_bruto,
        "monto_descuento": monto_descuento,
        "importe_neto": importe_neto
    })

    print(f"\nImporte Bruto: S/.{importe_bruto:.2f}")
    print(f"Monto de descuento: S/.{monto_descuento:.2f}")
    print(f"Importe Neto: S/.{importe_neto:.2f}")

