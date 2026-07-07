def generar_reporte(ventas):
    print("\n--- Reporte de Ventas ---")
    if len(ventas) == 0:
        print("No hay ventas registradas.")
        return

    total_clientes_femenino = 0
    ventas_rango_80_100 = 0
    ventas_masculino_rango_100_800 = 0
    total_importe_neto = 0
    total_importe_neto_tipo1 = 0
    cantidad_tipo1 = 0

    for venta in ventas:
        if venta["genero"] == "F":
            total_clientes_femenino += 1

        if 80 <= venta["importe_neto"] <= 100:
            ventas_rango_80_100 += 1

        if venta["genero"] == "M" and 100 <= venta["importe_neto"] <= 800:
            ventas_masculino_rango_100_800 += 1

        total_importe_neto += venta["importe_neto"]

        if venta["tipo_cliente"] == 1:
            total_importe_neto_tipo1 += venta["importe_neto"]
            cantidad_tipo1 += 1

    if cantidad_tipo1 > 0:
        promedio_importe_neto_tipo1 = total_importe_neto_tipo1 / cantidad_tipo1
    else:
        promedio_importe_neto_tipo1 = 0

    print(f"Cantidad de clientes de género femenino: {total_clientes_femenino}")
    print(f"Cantidad de ventas con importe neto entre S/.80 y S/.100: {ventas_rango_80_100}")
    print(f"Cantidad de ventas de clientes masculinos con importe neto entre S/.100 y S/.800: {ventas_masculino_rango_100_800}")
    print(f"Total del importe neto: S/.{total_importe_neto:.2f}")
    print(f"Total del importe neto de clientes tipo 1: S/.{total_importe_neto_tipo1:.2f}")
    print(f"Promedio del importe neto de clientes tipo 1: S/.{promedio_importe_neto_tipo1:.2f}")

