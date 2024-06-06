# Autores: Juan David Arrieta Arrieta

import mysql.connector
from validaciones import validar_fecha, validar_numero
SERVER = 'localhost'
USER = 'informatica1'
PASSWD = 'bio123'
cnx = mysql.connector.connect(host=SERVER, user=USER , password=PASSWD)
cursor = cnx.cursor()
cursor.execute("CREATE DATABASE informatica1")
cnx = mysql.connector.connect(host="localhost", user="informatica1" , password="bio123", database="informatica1")
cursor=cnx.cursor()

cursor.execute("CREATE TABLE usuario (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")
cursor.execute("CREATE TABLE medicamentos (lote INT PRIMARY KEY, nombre VARCHAR(255), distribuidor VARCHAR(255), cantidad INT, fecha_llegada DATE,precio_venta DECIMAL(10, 2))")
cursor.execute("CREATE TABLE proveedores (codigo INT PRIMARY KEY, nombre VARCHAR(255), apellido VARCHAR(255), documento_identidad VARCHAR(225), entidad VARCHAR(255))")
cursor.execute("CREATE TABLE ubicaciones (codigo VARCHAR(225) PRIMARY KEY, nombre VARCHAR(255), telefono VARCHAR(2555))")

cursor.execute("INSERT INTO usuario (username, password) VALUES ('admin', 'admin123')")
cnx.commit()
cursor.execute("INSERT INTO medicamentos (lote, nombre, distribuidor, cantidad, fecha_llegada, precio_venta) VALUES (1, 'Paracetamol', 'Distribuidor A', 100, '2023-06-01', 500.00), (2, 'Ibuprofeno', 'Distribuidor B', 200, '2023-06-02', 300.00)")
cnx.commit()
cursor.execute("INSERT INTO proveedores (codigo, nombre, apellido, documento_identidad, entidad) VALUES (1, 'Juan', 'Perez', '12345678', 'Proveedor A'), (2, 'Ana', 'Gomez', '87654321', 'Proveedor B')")
cnx.commit()
cursor.execute("INSERT INTO ubicaciones (codigo, nombre, telefono) VALUES ('A1', 'Almacén Central', '3001234567'), ('B2', 'Sucursal Norte', '3007654321')")
cnx.commit()

def conectar():
    """
    Establece una conexión a la base de datos.

    Returns:
    mysql.connector.connection_cext.CMySQLConnection: Objeto de conexión a la base de datos.
    """
    return mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database="informatica1"
    )

def registrar_usuario(username, password):
    """
    Registra un nuevo usuario en la base de datos.

    Args:
    username (str): Nombre de usuario.
    password (str): Contraseña del usuario.
    """
    conexion = cnx
    cursor = conexion.cursor()
    query = "INSERT INTO usuario (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Usuario registrado exitosamente.")

def iniciar_sesion(username, password):
    """
    Inicia sesión de usuario.

    Args:
    username (str): Nombre de usuario.
    password (str): Contraseña del usuario.

    Returns:
    bool: True si el inicio de sesión es exitoso, False de lo contrario.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT * FROM usuario WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    usuario = cursor.fetchone()
    cursor.close()
    conexion.close()
    return usuario is not None

def crear_medicamento():
    """
    Crea un nuevo registro de medicamento en la base de datos.
    """
    lote = validar_numero("Lote del medicamento: ")
    nombre = input("Nombre del medicamento: ")
    distribuidor = input("Distribuidor del medicamento: ")
    cantidad = validar_numero("Cantidad en bodega: ")
    fecha_llegada = validar_fecha("Fecha de llegada (YYYY-MM-DD): ")
    precio_venta = float(input("Precio de venta: "))

    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO medicamentos (lote, nombre, distribuidor, cantidad, fecha_llegada, precio_venta) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (lote, nombre, distribuidor, cantidad, fecha_llegada, precio_venta)
    cursor.execute(query, val)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Medicamento creado exitosamente.")

def leer_medicamentos():
    """
    Lee y muestra todos los medicamentos registrados en la base de datos.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM medicamentos")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    for medicamento in resultados:
        print(medicamento)

def buscar_medicamento():
    """
    Busca un medicamento por su lote en la base de datos.
    """
    lote = validar_numero("Lote del medicamento a buscar: ")
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT * FROM medicamentos WHERE lote = %s"
    cursor.execute(query, (lote,))
    medicamento = cursor.fetchone()
    cursor.close()
    conexion.close()
    if medicamento:
        print(medicamento)
    else:
        print("Medicamento no encontrado.")

def actualizar_medicamento():
    """
    Actualiza la información de un medicamento en la base de datos.
    """
    lote = validar_numero("Lote del medicamento a actualizar: ")
    nombre = input("Nuevo nombre del medicamento: ")
    distribuidor = input("Nuevo distribuidor del medicamento: ")
    cantidad = validar_numero("Nueva cantidad en bodega: ")
    fecha_llegada = validar_fecha("Nueva fecha de llegada (YYYY-MM-DD): ")
    precio_venta = float(input("Nuevo precio de venta: "))

    conexion = conectar()
    cursor = conexion.cursor()
    query = "UPDATE medicamentos SET nombre = %s, distribuidor = %s, cantidad = %s, fecha_llegada = %s, precio_venta = %s WHERE lote = %s"
    val = (nombre, distribuidor, cantidad, fecha_llegada, precio_venta, lote)
    cursor.execute(query, val)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Medicamento actualizado exitosamente.")

def eliminar_medicamento():
    """
    Elimina un medicamento de la base de datos.
    """
    lote = validar_numero("Lote del medicamento a eliminar: ")
    conexion = conectar()
    cursor = conexion.cursor()
    query = "DELETE FROM medicamentos WHERE lote = %s"
    cursor.execute(query, (lote,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Medicamento eliminado exitosamente.")

def crear_proveedor():
    """
    Crea un nuevo registro de proveedor en la base de datos.
    """
    codigo = validar_numero("Código del proveedor: ")
    nombre = input("Nombre del proveedor: ")
    apellido = input("Apellido del proveedor: ")
    documento_identidad = input("Documento de identidad del proveedor: ")
    entidad = input("Entidad del proveedor: ")

    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO proveedores (codigo, nombre, apellido, documento_identidad, entidad) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (codigo, nombre, apellido, documento_identidad, entidad))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Proveedor creado exitosamente.")

def leer_proveedores():
    """
    Lee y muestra todos los proveedores registrados en la base de datos.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM proveedores")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    for proveedor in resultados:
        print(proveedor)

def buscar_proveedor():
    """
    Busca un proveedor por su código en la base de datos.
    """
    codigo = validar_numero("Código del proveedor a buscar: ")
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT * FROM proveedores WHERE codigo = %s"
    cursor.execute(query, (codigo,))
    proveedor = cursor.fetchone()
    cursor.close()
    conexion.close()
    if proveedor:
        print(proveedor)
    else:
        print("Proveedor no encontrado.")

def actualizar_proveedor():
    """
    Actualiza la información de un proveedor en la base de datos.
    """
    codigo = validar_numero("Código del proveedor a actualizar: ")
    nombre = input("Nuevo nombre del proveedor: ")
    apellido = input("Nuevo apellido del proveedor: ")
    documento_identidad = input("Nuevo documento de identidad del proveedor: ")
    entidad = input("Nueva entidad del proveedor: ")

    conexion = conectar()
    cursor = conexion.cursor()
    query = "UPDATE proveedores SET nombre = %s, apellido = %s, documento_identidad = %s, entidad = %s WHERE codigo = %s"
    cursor.execute(query, (nombre, apellido, documento_identidad, entidad, codigo))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Proveedor actualizado exitosamente.")

def eliminar_proveedor():
    """
    Elimina un proveedor de la base de datos.
    """
    codigo = validar_numero("Código del proveedor a eliminar: ")
    conexion = conectar()
    cursor = conexion.cursor()
    query = "DELETE FROM proveedores WHERE codigo = %s"
    cursor.execute(query, (codigo,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Proveedor eliminado exitosamente.")

def crear_ubicacion():
    """
    Crea un nuevo registro de ubicación en la base de datos.
    """
    codigo = input("Código de la ubicación: ")
    nombre = input("Nombre de la ubicación: ")
    telefono = input("Teléfono de la ubicación: ")

    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO ubicaciones (codigo, nombre, telefono) VALUES (%s, %s, %s)"
    cursor.execute(query, (codigo, nombre, telefono))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Ubicación creada exitosamente.")

def leer_ubicaciones():
    """
    Lee y muestra todas las ubicaciones registradas en la base de datos.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM ubicaciones")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    for ubicacion in resultados:
        print(ubicacion)

def buscar_ubicacion():
    """
    Busca una ubicación por su código en la base de datos.
    """
    codigo = input("Código de la ubicación a buscar: ")
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT * FROM ubicaciones WHERE codigo = %s"
    cursor.execute(query, (codigo,))
    ubicacion = cursor.fetchone()
    cursor.close()
    conexion.close()
    if ubicacion:
        print(ubicacion)
    else:
        print("Ubicación no encontrada.")

def actualizar_ubicacion():
    """
    Actualiza la información de una ubicación en la base de datos.
    """
    codigo = input("Código de la ubicación a actualizar: ")
    nombre = input("Nuevo nombre de la ubicación: ")
    telefono = input("Nuevo teléfono de la ubicación: ")

    conexion = conectar()
    cursor = conexion.cursor()
    query = "UPDATE ubicaciones SET nombre = %s, telefono = %s WHERE codigo = %s"
    cursor.execute(query, (nombre, telefono, codigo))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Ubicación actualizada exitosamente.")

def eliminar_ubicacion():
    """
    Elimina una ubicación de la base de datos.
    """
    codigo = input("Código de la ubicación a eliminar: ")
    conexion = conectar()
    cursor = conexion.cursor()
    query = "DELETE FROM ubicaciones WHERE codigo = %s"
    cursor.execute(query, (codigo,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Ubicación eliminada exitosamente.")

def menu_medicamentos():
    """
    Muestra el menú de gestión de medicamentos y ejecuta las opciones seleccionadas por el usuario.
    """
    while True:
        print("\nGestión de Medicamentos")
        print("1. Ingresar un nuevo medicamento")
        print("2. Actualizar información de un medicamento")
        print("3. Buscar un medicamento")
        print("4. Ver todos los medicamentos")
        print("5. Eliminar un medicamento")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            crear_medicamento()
        elif opcion == '2':
            actualizar_medicamento()
        elif opcion == '3':
            buscar_medicamento()
        elif opcion == '4':
            leer_medicamentos()
        elif opcion == '5':
            eliminar_medicamento()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_proveedores():
    """
    Muestra el menú de gestión de proveedores y ejecuta las opciones seleccionadas por el usuario.
    """
    while True:
        print("\nGestión de Proveedores")
        print("1. Ingresar un nuevo proveedor")
        print("2. Actualizar información de un proveedor")
        print("3. Buscar un proveedor")
        print("4. Ver todos los proveedores")
        print("5. Eliminar un proveedor")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            crear_proveedor()
        elif opcion == '2':
            actualizar_proveedor()
        elif opcion == '3':
            buscar_proveedor()
        elif opcion == '4':
            leer_proveedores()
        elif opcion == '5':
            eliminar_proveedor()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_ubicaciones():
    """
    Muestra el menú de gestión de ubicaciones y ejecuta las opciones seleccionadas por el usuario.
    """
    while True:
        print("\nGestión de Ubicaciones")
        print("1. Ingresar una nueva ubicación")
        print("2. Actualizar información de una ubicación")
        print("3. Buscar una ubicación")
        print("4. Ver todas las ubicaciones")
        print("5. Eliminar una ubicación")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            crear_ubicacion()
        elif opcion == '2':
            actualizar_ubicacion()
        elif opcion == '3':
            buscar_ubicacion()
        elif opcion == '4':
            leer_ubicaciones()
        elif opcion == '5':
            eliminar_ubicacion()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_principal():
    """
    Muestra el menú principal y ejecuta las opciones seleccionadas por el usuario.
    """
    while True:
        print("\nMenú Principal")
        print("1. Gestionar Medicamentos")
        print("2. Gestionar Proveedores")
        print("3. Gestionar Ubicaciones")
        print("4. Salir")
        try: 
            opcion = int(input("Seleccione una opción: "))
        except:
            print("Debe ingresar un número.")
            continue
        if opcion == 1:
            menu_medicamentos()
        elif opcion == 2:
            menu_proveedores()
        elif opcion == 3:
            menu_ubicaciones()
        elif opcion == 4:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

while True:
    print("\nSistema de Gestión de IPS Medellín")
    print("1. Iniciar sesión")
    print("2. Registrar usuario")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        username = input("Usuario: ")
        password = input("Contraseña: ")
        if iniciar_sesion(username, password):
            print("Inicio de sesión exitoso.")
            menu_principal()
        else:
            print("Credenciales incorrectas. Intente de nuevo.")
    elif opcion == '2':
        try:
            username = input("Nuevo usuario: ")
            password = input("Nueva contraseña: ")
            registrar_usuario(username, password)
        except mysql.connector.IntegrityError as e:
            if e.errno == 1062:
                print("El nombre de usuario ya existe. Por favor, elija otro.")
            else:
                print("Error al insertar usuario:", e)
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Intente de nuevo.")