import sqlite3

def crear_base_de_datos():
    conexion = sqlite3.connect('data.db')
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(40),
            kilolitro FLOAT,
            precio_produccion FLOAT,
            precio_venta FLOAT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(40),
            apellido VARCHAR(40),
            direccion VARCHAR(60),
            telefono INTEGER,
            correo VARCHAR(60)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha DATETIME
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Inventario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto INTEGER,
            venta INTEGER,
            fecha_vencimiento DATETIME,
            FOREIGN KEY (producto) REFERENCES Productos(id),
            FOREIGN KEY (venta) REFERENCES Ventas(id)
        )
    ''')

    conexion.commit()
    conexion.close()

def abrir_conexion():
    con = sqlite3.connect('data.db')
    cursor = conexion.cursor()
    return con, cursor


def ver_productos():
    try:
        con, cursor = abrir_conexion()

        cursor.execute("SELECT * FROM Productos")
        productos = cursor.fetchall()

        productos_lista = []
        for producto in productos:
            producto_dict = {
                "id": producto[0],
                "nombre": producto[1],
                "kilolitro": producto[2],
                "precio_produccion": producto[3],
                "precio_venta": producto[4]
            }
            productos_lista.append(producto_dict)

        con.close()

        return productos_lista
    except:
        return None


def crear_producto(nombre, kilolitro, precio_produccion, precio_venta):
    try:
        con, cursor = abrir_conexion()

        cursor.execute('''
            INSERT INTO Productos (nombre, kilolitro, precio_produccion, precio_venta)
            VALUES (?, ?, ?, ?)
        ''', (nombre, kilolitro, precio_produccion, precio_venta))

        conexion.commit()

        con.close()

        return True
    except:
        return False

    