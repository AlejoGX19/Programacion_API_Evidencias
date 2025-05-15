def aplicar_descuento(precio, porcentaje_descuento):
    if porcentaje_descuento < 0:
        raise ValueError("El precio no puede ser negativo")
    if porcentaje_descuento <= 0 or porcentaje_descuento > 100:
        raise ValueError("El porcentaje debe estar entre 1 y 100")
    
    monto_final = precio * (1 - porcentaje_descuento / 100)
    return round(monto_final, 2)
