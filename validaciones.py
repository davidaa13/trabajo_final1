def validar_numero(prompt):
    while True:
        try:
            valor = int(input(prompt))
            return valor
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

def validar_fecha(prompt):
    from datetime import datetime
    while True:
        fecha_str = input(prompt)
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
            return fecha_str
        except ValueError:
            print("Error: Por favor ingrese una fecha válida en formato YYYY-MM-DD.")