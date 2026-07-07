contador_calculos = 0
contador_categoria_A = 0
contador_categoria_E = 0
acumulador_monto_pagar = 0
acumulador_categoria_B = 0
acumulador_monto_1000 = 0

def calcular_penalidad(monto_base, categoria, tipo_cambio):
    global contador_calculos, contador_categoria_A, contador_categoria_E
    porcentaje_penalidad = 0
    
    if categoria == "A":
        if monto_base <= 60:
            porcentaje_penalidad = 0.05
            contador_categoria_A += 1
    elif categoria == "B":
        if 61 <= monto_base <= 100:
            porcentaje_penalidad = 0.07
    elif categoria == "C":
        if 101 <= monto_base <= 149:
            porcentaje_penalidad = 0.09
    elif categoria == "D":
        if 150 <= monto_base <= 200:
            porcentaje_penalidad = 0.12
    elif categoria == "E":
        if monto_base > 200:
            porcentaje_penalidad = 0.15
            contador_categoria_E += 1
    else:
        return 0, 0, 0

    monto_base_soles = monto_base * tipo_cambio
    monto_penalidad = monto_base_soles * porcentaje_penalidad
    monto_pagar = monto_base_soles + monto_penalidad
    
    global acumulador_monto_pagar, acumulador_categoria_B, acumulador_monto_1000
    acumulador_monto_pagar += monto_pagar
    if categoria == "B":
        acumulador_categoria_B += monto_pagar
    if monto_pagar >= 1000:
        acumulador_monto_1000 += monto_pagar

    contador_calculos += 1

    return monto_base_soles, monto_penalidad, monto_pagar
