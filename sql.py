import sqlite3

def crear_base_de_datos(conexion, cursor):

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
                noIdProducto INTEGER PRIMARY KEY AUTOINCREMENT, 
				NombreProducto text NOT NULL, 
				medida text NOT NULL, 
				Fechavencimiento date NOT NULL, 
				PrecioProduccion integer NOT NULL, 
				PrecioVenta integer NOT NULL
		)''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clientes (
            noIdCliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre text NOT NULL,
            apellido text NOT NULL,
            direccion text NOT NULL,
            telefono integer NOT NULL,
            correo text NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Ventas (
            noIdVentas INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha DATETIME,
            producto INTEGER,
            cliente INTEGER,
            cantidad INTEGER,
            FOREIGN KEY (producto) REFERENCES Productos(noIdProducto),
            FOREIGN KEY (cliente) REFERENCES Clientes(noIdCliente)
        )
    ''')

    # cursor.execute('''
    #     CREATE TABLE IF NOT EXISTS Inventario (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         producto INTEGER,
    #         venta INTEGER,
    #         fecha_vencimiento DATETIME,
    #         FOREIGN KEY (producto) REFERENCES Productos(id),
    #         FOREIGN KEY (venta) REFERENCES Ventas(id)
    #     )
    # ''')

    conexion.commit()
    conexion.close()

def abrir_conexion():
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
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
                "medida": producto[2],
                "fecha_vencimiento": producto[3],
                "precio_produccion": producto[4],
                "precio_venta": producto[5]
            }
            productos_lista.append(producto_dict)

        con.close()

        return productos_lista
    except:
        return None


def crear_producto(nombre, medida, fechaVencimiento, precioProduccion, precioVenta,):
    try:
        con, cursor = abrir_conexion()
        cursor.execute('''
            INSERT INTO productos (NombreProducto, medida, Fechavencimiento, PrecioProduccion, PrecioVenta)
            VALUES(?, ?, ?, ?, ?)
        ''', (nombre, medida, fechaVencimiento, precioProduccion, precioVenta))

        con.commit()

        con.close()

        return True
    except Exception as e:
        print(e)
        return False

def listar_clientes():
    conn, cursor = abrir_conexion()
    cursor.execute("SELECT noIdCliente, nombre, apellido, direccion, telefono, correo FROM Clientes")
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def accion_cliente_detalle(id_cliente):
    conn, cursor = abrir_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT noIdCliente, nombre, apellido, direccion, telefono, correo FROM Clientes WHERE noIdCliente = ?", (id_cliente,))
    cliente = cursor.fetchone()
    conn.close()
    return cliente

def accion_cliente_cambiar_direccion(nueva_direccion, id_cliente):
    conn, cursor = abrir_conexion()
    cursor.execute("UPDATE Clientes SET direccion = ? WHERE noIdCliente = ?", (nueva_direccion, id_cliente))
    conn.commit()
    conn.close()


def accion_ver_historico_ventas_cliente(id_cliente):
    conn, cursor = abrir_conexion()
    cursor.execute('''
        SELECT noIdVentas, fecha, producto, cantidad FROM Ventas WHERE cliente = ?
    ''', (id_cliente,))
    ventas = cursor.fetchall()
    conn.close()
    return ventas

def accion_registrar_venta_cliente(fecha_venta, producto_id, id_cliente, cantidad):
    conn, cursor = abrir_conexion()
    try:
        cursor.execute('''
            INSERT INTO Ventas (fecha, producto, cliente, cantidad)
            VALUES (?, ?, ?, ?)
        ''', (fecha_venta, producto_id, id_cliente, cantidad))
        conn.commit()

        conn.close()
        return True
    
    except:
        return False

def accion_borrar_venta(id_venta):
    conn, cursor = abrir_conexion()
    cursor.execute('''
            DELETE FROM Ventas WHERE noIdVentas = ?
        ''', (id_venta,))
    conn.commit()
    if cursor.rowcount > 0:
        return True
    else:
        False


def crear_cliente(nombre, apellido, direccion, telefono, correo):
    try:
        conn, cursor = abrir_conexion()
        cursor.execute('''
            INSERT INTO Clientes (nombre, apellido, direccion, telefono, correo)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, apellido, direccion, telefono, correo))
        conn.commit()
        conn.close()

        return True
    except:
        return False    

if __name__ == "__main__":
    con, cursor = abrir_conexion()
    crear_base_de_datos(con, cursor)
