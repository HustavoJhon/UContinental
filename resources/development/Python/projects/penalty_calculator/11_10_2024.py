import os 

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def menu_principal():
    print("\nMENU PRINCIPAL")
    print("""
        [1]. Registar venta.
        [2]. Reportar venta.
        [3]. Salir.
          """)

def reporte_tipo_servicio():
    print("\n========== REPORTE ==========")
    print(f"Pasaje: IMPERIAL\nPrecio: S/.{precio}:")
    print(f"Su importe en bruto es: {importe_bruto}")
    print(f"Su monto de descuento es: {monto_descuento}")
    print(f"Su importe neto es: {importe_neto}")
    
# Contadores & Acumuladores
total_femenino = 0
neto_importe_mayo = 0
cantidad_masculino_neto = 0
neto_total = 0
importe_neto_tipo_1 = 0
promedio_importe_neto_tipo_1 = 0


limpiar()
print("""
       777
      (^-^)
      (   )~  TRASNPORTE INTERPROVINCIAL |
    ***m*m*******************************
      """)
    

while True:
    menu_principal()
    while True:
        operacion_menu = int(input("Ingrese una operacion:\t\t"))
        if operacion_menu < 1 or operacion_menu > 3:
            print("ERROR. Ingrese una operacion valida")
        else:
            break
    match operacion_menu:
        case 1:
            print("\n\nREGISTRO DE VENTA:")
            tipo_cliente = int(input("Ingrese tipo de cliente (1 0 2): "))
            cantidad_pasajes = int(input("Ingrese la cantidad de pasajes (> 0): "))
            genero_cliente = input("Ingrese su genero (M o F): ").upper()
            tipo_servicio = int(input("Ingrese el tipo de servicio (1. Imperial - 2. VIP - 3. Gold): "))

            match tipo_servicio:
                case 1: # IMPERIAL
                    precio = 80.00
                    limpiar()
                    if cantidad_pasajes == 1:
                        importe_bruto = cantidad_pasajes * precio
                        monto_descuento = importe_bruto
                        importe_neto = importe_bruto #no hay descuento

                        reporte_tipo_servicio()

                    elif cantidad_pasajes >= 2 and cantidad_pasajes <= 5:
                        importe_bruto = cantidad_pasajes * precio
                        monto_descuento = float(importe_bruto * 0.1) 
                        importe_neto = importe_bruto - monto_descuento
                        
                        reporte_tipo_servicio()
                        
                    elif cantidad_pasajes >= 6 and cantidad_pasajes <= 10:
                        importe_bruto = cantidad_pasajes * precio
                        monto_descuento = float(importe_bruto * 0.15) 
                        importe_neto = importe_bruto - monto_descuento
                        
                        reporte_tipo_servicio()
                        
                    elif cantidad_pasajes >= 11:
                        importe_bruto = cantidad_pasajes * precio
                        monto_descuento = float(importe_bruto * 0.2) 
                        importe_neto = importe_bruto - monto_descuento 

                        reporte_tipo_servicio()
                        
                    else:
                        print("Valor no valido")
                        
                case 2: # VIP
                    precio = 100.00
                    limpiar()
                    if cantidad_pasajes == 1:
                        importe_bruto = cantidad_pasajes * precio
                        importe_neto = importe_bruto  #no hay descuento
  
                        reporte_tipo_servicio()

                    elif cantidad_pasajes >= 2 and cantidad_pasajes <= 5:
                        importe_bruto = cantidad_pasajes * precio
                        monto_descuento =  float(importe_bruto * 0.1) 
                        importe_neto = importe_bruto -monto_descuento

                        reporte_tipo_servicio()
                        
                    elif cantidad_pasajes >= 6 and cantidad_pasajes <= 10:
                        importe_bruto = cantidad_pasajes * precio
                        monto_descuento = float(importe_bruto * 0.15) 
                        importe_neto = importe_bruto - monto_descuento

                        reporte_tipo_servicio()
                        
                    elif cantidad_pasajes >= 11:
                        importe_bruto = cantidad_pasajes * precio
                        monto_descuento = float(importe_bruto * 0.20) 
                        importe_neto = importe_bruto - monto_descuento
   
                        reporte_tipo_servicio()
                        
                    else:
                        print("Valor no valido")
                        
                case 3: # GOLD
                    precio = 120.00
                    limpiar()
                    if cantidad_pasajes == 1:
                        importe_bruto = cantidad_pasajes * 120.00
                        monto_descuento = importe_bruto #no hay descuento
                        importe_neto = importe_bruto #no hay descuento
                        
                        reporte_tipo_servicio()

                    elif cantidad_pasajes >= 2 and cantidad_pasajes <= 5:
                        importe_bruto = cantidad_pasajes * precio
                        monto_descuento = float(importe_bruto * 0.1) 
                        importe_neto = importe_bruto - monto_descuento

                        reporte_tipo_servicio()
                        
                    elif cantidad_pasajes >= 6 and cantidad_pasajes <= 10:
                        importe_bruto = cantidad_pasajes * precio
                        monto_descuento = float(importe_bruto * 0.15) 
                        importe_neto = importe_bruto - monto_descuento
                        
                        reporte_tipo_servicio()
                        
                    elif cantidad_pasajes >= 11:
                        importe_bruto = cantidad_pasajes * precio
                        monto_descuento = float(importe_bruto * 0.2) 
                        importe_neto = importe_bruto - monto_descuento
                        
                        reporte_tipo_servicio()
                        
                    else:
                        print("Valor no valido")
                    
        case 2:
            print("\n========== REPORTAR VENTA ==========")
            while True:
                if genero_cliente == "F":
                    total_femenino = total_femenino + 1
                print(f"Clientes del genero femenino(F): {total_femenino}")   
                break
             
            print(f"Cantidad de ventas cuyo importe neto sea >= 80 y <= 100: {neto_importe_mayo}")
            print(f"Cantidad de ventas de clientes de genero masculino cuyo importe neto sea >= 100 y <= 8: {cantidad_masculino_neto}")
            neto_total += neto_total
            print(f"Acumulador de importe neto: {neto_total}")
            print(f"Acumulador de importe neto de cliente tipo 1: {importe_neto_tipo_1}")
            print(f"Promedio de importe neto de cliente tipo 1: {promedio_importe_neto_tipo_1}")
            
        case 3:
            print("GRACIAS POR USAR EL PROGRAMA")
            break

            

