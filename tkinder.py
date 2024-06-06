import tkinter as tk
from tkinter import messagebox
import mysql.connector
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="informatica1",
        password="bio123",
        database="informatica1"
    )

def registrar_usuario(username, password):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO usuario (username, password) VALUES (%s, %s)"
    try:
        cursor.execute(query, (username, password))
        conexion.commit()
        messagebox.showinfo("Éxito", "Usuario registrado exitosamente.")
    except mysql.connector.IntegrityError as e:
        if e.errno == 1062:
            messagebox.showerror("Error", "El nombre de usuario ya existe. Por favor, elija otro.")
        else:
            messagebox.showerror("Error", f"Error al insertar usuario: {e}")
    finally:
        cursor.close()
        conexion.close()

def iniciar_sesion(username, password):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT * FROM usuario WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    usuario = cursor.fetchone()
    cursor.close()
    conexion.close()
    return usuario is not None

def menu_principal(root):
    root.withdraw()
    main_menu = tk.Toplevel(root)
    main_menu.title("Menú Principal")

    tk.Button(main_menu, text="Gestionar Medicamentos", command=lambda: menu_medicamentos(main_menu)).pack(pady=10)
    tk.Button(main_menu, text="Gestionar Proveedores", command=lambda: menu_proveedores(main_menu)).pack(pady=10)
    tk.Button(main_menu, text="Gestionar Ubicaciones", command=lambda: menu_ubicaciones(main_menu)).pack(pady=10)
    tk.Button(main_menu, text="Salir", command=root.quit).pack(pady=10)

def menu_proveedores(parent):
    parent.withdraw()
    prov_menu = tk.Toplevel(parent)
    prov_menu.title("Menú Proveedores")

    tk.Button(prov_menu, text="Ingresar un nuevo proveedor", command=lambda: crear_proveedor(prov_menu)).pack()
    tk.Button(prov_menu, text="Actualizar información de un proveedor", command=lambda: actualizar_proveedor(prov_menu)).pack()
    tk.Button(prov_menu, text="Buscar un proveedor", command=lambda: buscar_proveedor(prov_menu)).pack()
    tk.Button(prov_menu, text="Ver todos los proveedores", command=lambda: leer_proveedores(prov_menu)).pack()
    tk.Button(prov_menu, text="Eliminar un proveedor", command=lambda: eliminar_proveedor(prov_menu)).pack()
    tk.Button(prov_menu, text="Volver al menú principal", command=lambda: volver_principal(parent, prov_menu)).pack()

def menu_ubicaciones(parent):
    parent.withdraw()
    ubi_menu = tk.Toplevel(parent)
    ubi_menu.title("Menú Ubicaciones")

    tk.Button(ubi_menu, text="Ingresar una nueva ubicación", command=lambda: crear_ubicacion(ubi_menu)).pack()
    tk.Button(ubi_menu, text="Actualizar información de una ubicación", command=lambda: actualizar_ubicacion(ubi_menu)).pack()
    tk.Button(ubi_menu, text="Buscar una ubicación", command=lambda: buscar_ubicacion(ubi_menu)).pack()
    tk.Button(ubi_menu, text="Ver todas las ubicaciones", command=lambda: leer_ubicaciones(ubi_menu)).pack()
    tk.Button(ubi_menu, text="Eliminar una ubicación", command=lambda: eliminar_ubicacion(ubi_menu)).pack()
    tk.Button(ubi_menu, text="Volver al menú principal", command=lambda: volver_principal(parent, ubi_menu)).pack()

def crear_medicamento(parent):
    parent.withdraw()
    window_add = tk.Toplevel(parent)
    window_add.title("Agregar Medicamento")

    tk.Label(window_add, text="Lote").grid(row=0, column=0)
    entry_lote = tk.Entry(window_add)
    entry_lote.grid(row=0, column=1)

    tk.Label(window_add, text="Nombre").grid(row=1, column=0)
    entry_nombre = tk.Entry(window_add)
    entry_nombre.grid(row=1, column=1)

    tk.Label(window_add, text="Distribuidor").grid(row=2, column=0)
    entry_distribuidor = tk.Entry(window_add)
    entry_distribuidor.grid(row=2, column=1)

    tk.Label(window_add, text="Cantidad").grid(row=3, column=0)
    entry_cantidad = tk.Entry(window_add)
    entry_cantidad.grid(row=3, column=1)

    tk.Label(window_add, text="Fecha de Llegada").grid(row=4, column=0)
    entry_fecha_llegada = tk.Entry(window_add)
    entry_fecha_llegada.grid(row=4, column=1)

    tk.Label(window_add, text="Precio de Venta").grid(row=5, column=0)
    entry_precio_venta = tk.Entry(window_add)
    entry_precio_venta.grid(row=5, column=1)

    def submit():
        lote = int(entry_lote.get())
        nombre = entry_nombre.get()
        distribuidor = entry_distribuidor.get()
        cantidad = int(entry_cantidad.get())
        fecha_llegada = entry_fecha_llegada.get()
        precio_venta = float(entry_precio_venta.get())

        conexion = conectar()
        cursor = conexion.cursor()
        query = "INSERT INTO medicamentos (lote, nombre, distribuidor, cantidad, fecha_llegada, precio_venta) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (lote, nombre, distribuidor, cantidad, fecha_llegada, precio_venta))
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("Éxito", "Medicamento creado exitosamente.")
        window_add.destroy()
        parent.deiconify()

    tk.Button(window_add, text="Agregar", command=submit).grid(row=6, column=1)

def actualizar_medicamento(parent):
    parent.withdraw()
    window_update = tk.Toplevel(parent)
    window_update.title("Actualizar Medicamento")

    tk.Label(window_update, text="Lote").grid(row=0, column=0)
    entry_lote = tk.Entry(window_update)
    entry_lote.grid(row=0, column=1)

    tk.Label(window_update, text="Nuevo Nombre").grid(row=1, column=0)
    entry_nombre = tk.Entry(window_update)
    entry_nombre.grid(row=1, column=1)

    tk.Label(window_update, text="Nuevo Distribuidor").grid(row=2, column=0)
    entry_distribuidor = tk.Entry(window_update)
    entry_distribuidor.grid(row=2, column=1)

    tk.Label(window_update, text="Nueva Cantidad").grid(row=3, column=0)
    entry_cantidad = tk.Entry(window_update)
    entry_cantidad.grid(row=3, column=1)

    tk.Label(window_update, text="Nueva Fecha de Llegada").grid(row=4, column=0)
    entry_fecha_llegada = tk.Entry(window_update)
    entry_fecha_llegada.grid(row=4, column=1)

    tk.Label(window_update, text="Nuevo Precio de Venta").grid(row=5, column=0)
    entry_precio_venta = tk.Entry(window_update)
    entry_precio_venta.grid(row=5, column=1)

    def submit():
        lote = int(entry_lote.get())
        nombre = entry_nombre.get()
        distribuidor = entry_distribuidor.get()
        cantidad = int(entry_cantidad.get())
        fecha_llegada = entry_fecha_llegada.get()
        precio_venta = float(entry_precio_venta.get())

        conexion = conectar()
        cursor = conexion.cursor()
        query = "UPDATE medicamentos SET nombre = %s, distribuidor = %s, cantidad = %s, fecha_llegada = %s, precio_venta = %s WHERE lote = %s"
        cursor.execute(query, (nombre, distribuidor, cantidad, fecha_llegada, precio_venta, lote))
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("Éxito", "Medicamento actualizado exitosamente.")
        window_update.destroy()
        parent.deiconify()

    tk.Button(window_update, text="Actualizar", command=submit).grid(row=6, column=1)

def menu_medicamentos(parent):
    parent.withdraw()
    med_menu = tk.Toplevel(parent)
    med_menu.title("Menú Medicamentos")

    tk.Button(med_menu, text="Ingresar un nuevo medicamento", command=lambda: crear_medicamento(med_menu)).pack()
    tk.Button(med_menu, text="Actualizar la información de un medicamento", command=lambda: actualizar_medicamento(med_menu)).pack()
    tk.Button(med_menu, text="Buscar un medicamento", command=lambda: buscar_medicamento(med_menu)).pack()
    tk.Button(med_menu, text="Ver la información de todos los medicamentos", command=lambda: leer_medicamentos(med_menu)).pack()
    tk.Button(med_menu, text="Eliminar un medicamento", command=lambda: eliminar_medicamento(med_menu)).pack()
    tk.Button(med_menu, text="Volver al menú principal", command=lambda: volver_principal(parent, med_menu)).pack()

def eliminar_medicamento(parent):
    parent.withdraw()
    window_delete = tk.Toplevel(parent)
    window_delete.title("Eliminar Medicamento")

    tk.Label(window_delete, text="Lote").grid(row=0, column=0)
    entry_lote = tk.Entry(window_delete)
    entry_lote.grid(row=0, column=1)

    def submit():
        lote = int(entry_lote.get())

        conexion = conectar()
        cursor = conexion.cursor()
        query = "DELETE FROM medicamentos WHERE lote = %s"
        cursor.execute(query, (lote,))
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("Éxito", "Medicamento eliminado exitosamente.")
        window_delete.destroy()
        parent.deiconify()

    tk.Button(window_delete, text="Eliminar", command=submit).grid(row=1, column=1)

def buscar_medicamento(parent):
    parent.withdraw()
    window_search = tk.Toplevel(parent)
    window_search.title("Buscar Medicamento")

    tk.Label(window_search, text="Lote").grid(row=0, column=0)
    entry_lote = tk.Entry(window_search)
    entry_lote.grid(row=0, column=1)

    def submit():
        lote = int(entry_lote.get())

        conexion = conectar()
        cursor = conexion.cursor()
        query = "SELECT * FROM medicamentos WHERE lote = %s"
        cursor.execute(query, (lote,))
        medicamento = cursor.fetchone()
        cursor.close()
        conexion.close()

        if medicamento:
            messagebox.showinfo("Medicamento Encontrado", f"Medicamento: {medicamento}")
        else:
            messagebox.showerror("Error", "Medicamento no encontrado.")
        window_search.destroy()
        parent.deiconify()

    tk.Button(window_search, text="Buscar", command=submit).grid(row=1, column=1)

def leer_medicamentos(parent):
    parent.withdraw()
    window_read = tk.Toplevel(parent)
    window_read.title("Todos los Medicamentos")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM medicamentos")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()

    text_area = tk.Text(window_read)
    for medicamento in resultados:
        text_area.insert(tk.END, f"{medicamento}\n")
    text_area.pack()

    tk.Button(window_read, text="Volver", command=lambda: volver_principal(parent, window_read)).pack()

def crear_proveedor(parent):
    parent.withdraw()
    window_create = tk.Toplevel(parent)
    window_create.title("Crear Proveedor")

    tk.Label(window_create, text="Código").grid(row=0, column=0)
    entry_codigo = tk.Entry(window_create)
    entry_codigo.grid(row=0, column=1)

    tk.Label(window_create, text="Nombre").grid(row=1, column=0)
    entry_nombre = tk.Entry(window_create)
    entry_nombre.grid(row=1, column=1)

    tk.Label(window_create, text="Apellido").grid(row=2, column=0)
    entry_apellido = tk.Entry(window_create)
    entry_apellido.grid(row=2, column=1)

    tk.Label(window_create, text="Documento de Identidad").grid(row=3, column=0)
    entry_documento = tk.Entry(window_create)
    entry_documento.grid(row=3, column=1)

    tk.Label(window_create, text="Entidad").grid(row=4, column=0)
    entry_entidad = tk.Entry(window_create)
    entry_entidad.grid(row=4, column=1)

    def submit():
        codigo = int(entry_codigo.get())
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        documento = entry_documento.get()
        entidad = entry_entidad.get()

        conexion = conectar()
        cursor = conexion.cursor()
        query = "INSERT INTO proveedores (codigo, nombre, apellido, documento_identidad, entidad) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (codigo, nombre, apellido, documento, entidad))
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("Éxito", "Proveedor creado exitosamente.")
        window_create.destroy()
        parent.deiconify()

    tk.Button(window_create, text="Crear", command=submit).grid(row=5, column=1)

def actualizar_proveedor(parent):
    parent.withdraw()
    window_update = tk.Toplevel(parent)
    window_update.title("Actualizar Proveedor")

    tk.Label(window_update, text="Código").grid(row=0, column=0)
    entry_codigo = tk.Entry(window_update)
    entry_codigo.grid(row=0, column=1)

    tk.Label(window_update, text="Nuevo Nombre").grid(row=1, column=0)
    entry_nombre = tk.Entry(window_update)
    entry_nombre.grid(row=1, column=1)

    tk.Label(window_update, text="Nuevo Apellido").grid(row=2, column=0)
    entry_apellido = tk.Entry(window_update)
    entry_apellido.grid(row=2, column=1)

    tk.Label(window_update, text="Nuevo Documento de Identidad").grid(row=3, column=0)
    entry_documento = tk.Entry(window_update)
    entry_documento.grid(row=3, column=1)

    tk.Label(window_update, text="Nueva Entidad").grid(row=4, column=0)
    entry_entidad = tk.Entry(window_update)
    entry_entidad.grid(row=4, column=1)

    def submit():
        codigo = int(entry_codigo.get())
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        documento = entry_documento.get()
        entidad = entry_entidad.get()

        conexion = conectar()
        cursor = conexion.cursor()
        query = "UPDATE proveedores SET nombre = %s, apellido = %s, documento_identidad = %s, entidad = %s WHERE codigo = %s"
        cursor.execute(query, (nombre, apellido, documento, entidad, codigo))
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("Éxito", "Proveedor actualizado exitosamente.")
        window_update.destroy()
        parent.deiconify()

    tk.Button(window_update, text="Actualizar", command=submit).grid(row=5, column=1)

def eliminar_proveedor(parent):
    parent.withdraw()
    window_delete = tk.Toplevel(parent)
    window_delete.title("Eliminar Proveedor")

    tk.Label(window_delete, text="Código").grid(row=0, column=0)
    entry_codigo = tk.Entry(window_delete)
    entry_codigo.grid(row=0, column=1)

    def submit():
        codigo = int(entry_codigo.get())

        conexion = conectar()
        cursor = conexion.cursor()
        query = "DELETE FROM proveedores WHERE codigo = %s"
        cursor.execute(query, (codigo,))
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("Éxito", "Proveedor eliminado exitosamente.")
        window_delete.destroy()
        parent.deiconify()

    tk.Button(window_delete, text="Eliminar", command=submit).grid(row=1, column=1)

def buscar_proveedor(parent):
    parent.withdraw()
    window_search = tk.Toplevel(parent)
    window_search.title("Buscar Proveedor")
    tk.Label(window_search, text="Código").grid(row=0, column=0)
    entry_codigo = tk.Entry(window_search)
    entry_codigo.grid(row=0, column=1)

    def submit():
        codigo = int(entry_codigo.get())
        conexion = conectar()
        cursor = conexion.cursor()
        query = "SELECT * FROM proveedores WHERE codigo = %s"
        cursor.execute(query, (codigo,))
        proveedor = cursor.fetchone()
        cursor.close()
        conexion.close()

        if proveedor:
            messagebox.showinfo("Proveedor Encontrado", f"Proveedor: {proveedor}")
        else:
            messagebox.showerror("Error", "Proveedor no encontrado.")
        window_search.destroy()
        parent.deiconify()

    tk.Button(window_search, text="Buscar", command=submit).grid(row=1, column=1)

def buscar_proveedor(parent):
    parent.withdraw()
    window_search = tk.Toplevel(parent)
    window_search.title("Buscar Proveedor")

    tk.Label(window_search, text="Código").grid(row=0, column=0)
    entry_codigo = tk.Entry(window_search)
    entry_codigo.grid(row=0, column=1)

    def submit():
        codigo = int(entry_codigo.get())

        conexion = conectar()
        cursor = conexion.cursor()
        query = "SELECT * FROM proveedores WHERE codigo = %s"
        cursor.execute(query, (codigo,))
        proveedor = cursor.fetchone()
        cursor.close()
        conexion.close()

        if proveedor:
            messagebox.showinfo("Proveedor Encontrado", f"Proveedor: {proveedor}")
        else:
            messagebox.showerror("Error", "Proveedor no encontrado.")
        window_search.destroy()
        parent.deiconify()

    tk.Button(window_search, text="Buscar", command=submit).grid(row=1, column=1)

def leer_proveedores(parent):
    parent.withdraw()
    window_read = tk.Toplevel(parent)
    window_read.title("Todos los Proveedores")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM proveedores")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()

    text_area = tk.Text(window_read)
    for proveedor in resultados:
        text_area.insert(tk.END, f"{proveedor}\n")
    text_area.pack()

    tk.Button(window_read, text="Volver", command=lambda: volver_principal(parent, window_read)).pack()

def crear_ubicacion(parent):
    parent.withdraw()
    window_create = tk.Toplevel(parent)
    window_create.title("Crear Ubicación")

    tk.Label(window_create, text="Código").grid(row=0, column=0)
    entry_codigo = tk.Entry(window_create)
    entry_codigo.grid(row=0, column=1)

    tk.Label(window_create, text="Nombre").grid(row=1, column=0)
    entry_nombre = tk.Entry(window_create)
    entry_nombre.grid(row=1, column=1)

    tk.Label(window_create, text="Teléfono").grid(row=2, column=0)
    entry_telefono = tk.Entry(window_create)
    entry_telefono.grid(row=2, column=1)

    def submit():
        codigo = entry_codigo.get()
        nombre = entry_nombre.get()
        telefono = entry_telefono.get()

        conexion = conectar()
        cursor = conexion.cursor()
        query = "INSERT INTO ubicaciones (codigo, nombre, telefono) VALUES (%s, %s, %s)"
        cursor.execute(query, (codigo, nombre, telefono))
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("Éxito", "Ubicación creada exitosamente.")
        window_create.destroy()
        parent.deiconify()

    tk.Button(window_create, text="Crear", command=submit).grid(row=3, column=1)

def actualizar_ubicacion(parent):
    parent.withdraw()
    window_update = tk.Toplevel(parent)
    window_update.title("Actualizar Ubicación")

    tk.Label(window_update, text="Código").grid(row=0, column=0)
    entry_codigo = tk.Entry(window_update)
    entry_codigo.grid(row=0, column=1)

    tk.Label(window_update, text="Nuevo Nombre").grid(row=1, column=0)
    entry_nombre = tk.Entry(window_update)
    entry_nombre.grid(row=1, column=1)

    tk.Label(window_update, text="Nuevo Teléfono").grid(row=2, column=0)
    entry_telefono = tk.Entry(window_update)
    entry_telefono.grid(row=2, column=1)

    def submit():
        codigo = (entry_codigo.get())
        nombre = entry_nombre.get()
        telefono = entry_telefono.get()

        conexion = conectar()
        cursor = conexion.cursor()
        query = "UPDATE ubicaciones SET nombre = %s, telefono = %s WHERE codigo = %s"
        cursor.execute(query, (nombre, telefono, codigo))
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("Éxito", "Ubicación actualizada exitosamente.")
        window_update.destroy()
        parent.deiconify()

    tk.Button(window_update, text="Actualizar", command=submit).grid(row=3, column=1)

def eliminar_ubicacion(parent):
    parent.withdraw()
    window_delete = tk.Toplevel(parent)
    window_delete.title("Eliminar Ubicación")

    tk.Label(window_delete, text="Código").grid(row=0, column=0)
    entry_codigo = tk.Entry(window_delete)
    entry_codigo.grid(row=0, column=1)

    def submit():
        codigo = (entry_codigo.get())

        conexion = conectar()
        cursor = conexion.cursor()
        query = "DELETE FROM ubicaciones WHERE codigo = %s"
        cursor.execute(query, (codigo,))
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("Éxito", "Ubicación eliminada exitosamente.")
        window_delete.destroy()
        parent.deiconify()

    tk.Button(window_delete, text="Eliminar", command=submit).grid(row=1, column=1)

def buscar_ubicacion(parent):
    parent.withdraw()
    window_search = tk.Toplevel(parent)
    window_search.title("Buscar Ubicación")

    tk.Label(window_search, text="Código").grid(row=0, column=0)
    entry_codigo = tk.Entry(window_search)
    entry_codigo.grid(row=0, column=1)

    def submit():
        codigo = (entry_codigo.get())

        conexion = conectar()
        cursor = conexion.cursor()
        query = "SELECT * FROM ubicaciones WHERE codigo = %s"
        cursor.execute(query, (codigo,))
        ubicacion = cursor.fetchone()
        cursor.close()
        conexion.close()

        if ubicacion:
            messagebox.showinfo("Ubicación Encontrada", f"Ubicación: {ubicacion}")
        else:
            messagebox.showerror("Error", "Ubicación no encontrada.")
        window_search.destroy()
        parent.deiconify()

    tk.Button(window_search, text="Buscar", command=submit).grid(row=1, column=1)

def leer_ubicaciones(parent):
    parent.withdraw()
    window_read = tk.Toplevel(parent)
    window_read.title("Todas las Ubicaciones")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM ubicaciones")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()

    text_area = tk.Text(window_read)
    for ubicacion in resultados:
        text_area.insert(tk.END, f"{ubicacion}\n")
    text_area.pack()

    tk.Button(window_read, text="Volver", command=lambda: volver_principal(parent, window_read)).pack()

def volver_principal(parent, child):
    child.destroy()
    parent.deiconify()

def inicio_sesion(root):
    def submit_login():
        username = entry_user.get()
        password = entry_pass.get()
        if iniciar_sesion(username, password):
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
            menu_principal(root)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas. Intente de nuevo.")

    root.withdraw()
    login_window = tk.Toplevel(root)
    login_window.title("Inicio de Sesión")

    tk.Label(login_window, text="Usuario").grid(row=0, column=0)
    entry_user = tk.Entry(login_window)
    entry_user.grid(row=0, column=1)

    tk.Label(login_window, text="Contraseña").grid(row=1, column=0)
    entry_pass = tk.Entry(login_window, show="*")
    entry_pass.grid(row=1, column=1)

    tk.Button(login_window, text="Iniciar Sesión", command=submit_login).grid(row=2, column=1)
    tk.Button(login_window, text="Volver", command=lambda: volver_principal(root, login_window)).grid(row=2, column=0)

def registrar(root):
    def submit_register():
        username = entry_user.get()
        password = entry_pass.get()
        registrar_usuario(username, password)

    root.withdraw()
    register_window = tk.Toplevel(root)
    register_window.title("Registrar Usuario")

    tk.Label(register_window, text="Nuevo Usuario").grid(row=0, column=0)
    entry_user = tk.Entry(register_window)
    entry_user.grid(row=0, column=1)

    tk.Label(register_window, text="Nueva Contraseña").grid(row=1, column=0)
    entry_pass = tk.Entry(register_window, show="*")
    entry_pass.grid(row=1, column=1)

    tk.Button(register_window, text="Registrar", command=submit_register).grid(row=2, column=1)
    tk.Button(register_window, text="Volver", command=lambda: volver_principal(root, register_window)).grid(row=2, column=0)

root = tk.Tk()
root.title("Sistema de Gestión de IPS Medellín")

tk.Button(root, text="Iniciar Sesión", command=lambda: inicio_sesion(root)).pack(pady=10)
tk.Button(root, text="Registrar Usuario", command=lambda: registrar(root)).pack(pady=10)
tk.Button(root, text="Salir", command=root.quit).pack(pady=10)

root.mainloop()