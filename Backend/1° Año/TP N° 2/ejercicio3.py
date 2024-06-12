#3. Que nos calcule el total de una factura tras aplicarle el IVA. La función debe recibir la
#cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Sise invoca
#la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

#Definimos la función y realizamos las operaciones de agregado de IVA. Si el usuario no ingresa el iva, por defecto
#se aplicara el 21%
def factura_total(factura, iva_total=21):
    total = factura * (1 + iva_total / 100)
    return total

#Solicitamos el monto de la factura sin iva, y le pedimos que ingrese el iva a aplicar
factura_sin_iva = float(input('Ingrese el total de la factura: '))
iva_total = float(input('Ingrese el iva a aplicar: '))

total = factura_total(factura_sin_iva, iva_total)
print(f"El total de la factura después de aplicarle un {iva_total}% de IVA es: {total}")