### productos.py
import sqlite3

#crear un nuevo producto, actualizar su nombre y consultar la información
#vigente de un producto.
from sql import crear_producto, ver_productos

def main_productos(func_regresar):
    ventana_productos = tk.Tk()
    ventana_productos.title("Productos")
    ventana_productos.geometry("300x250")
    ventana_productos.config(bg="white")  # Fondo blanco

    def regresar():
        ventana_productos.destroy() 
        func_regresar() 

    btn_regresar = tk.Button(ventana_productos, text="Regresar", command=regresar, bg="yellow", fg="black")
    btn_regresar.pack(pady=20, fill="x")

    btn_ver_productos = tk.Button(ventana_productos, text="Ver Productos", command=ver_productos, bg="yellow", fg="black")
    btn_ver_productos.pack(pady=5, fill="x")

    btn_agregar_producto = tk.Button(ventana_productos, text="Agregar Producto", command=lambda: registrar_producto(func_regresar), bg="yellow", fg="black")
    btn_agregar_producto.pack(pady=5, fill="x")

    ventana_productos.mainloop()

def mostrar_productos():
    # Crear una ventana Toplevel
    ventana_toplevel = tk.Toplevel()
    ventana_toplevel.title("Lista de Productos")
    ventana_toplevel.geometry("400x400")

    # Crear un Canvas y un Frame dentro de él para hacer el frame scrollable
    canvas = tk.Canvas(ventana_toplevel)
    scrollbar = tk.Scrollbar(ventana_toplevel, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    # Configurar el canvas y la barra de desplazamiento
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Obtener los productos
    productos = ver_productos()

    if productos:
        # Iterar sobre los productos y agregarlos al frame
        for producto in productos:
            for campo, valor in producto.items():
                # Crear etiquetas para cada atributo del producto
                etiqueta = tk.Label(scrollable_frame, text=f"{campo.capitalize()}: {valor}", anchor="w", padx=10, pady=5)
                etiqueta.pack(fill="x")
    
        # Actualizar el tamaño del canvas después de añadir los productos
        scrollable_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
    else:
        # Mostrar un mensaje si no hay productos
        messagebox.showinfo("No hay productos", "No se encontraron productos en la base de datos.")


def registrar_producto():
    ventana_toplevel = tk.Toplevel()
    ventana_toplevel.title("Registrar Producto")
    ventana_toplevel.geometry("300x300")

    tk.Label(ventana_toplevel, text="Nombre del Producto:").pack(pady=5)
    entry_nombre = tk.Entry(ventana_toplevel)
    entry_nombre.pack(pady=5)

    tk.Label(ventana_toplevel, text="Kilolitros:").pack(pady=5)
    entry_kilolitro = tk.Entry(ventana_toplevel)
    entry_kilolitro.pack(pady=5)

    tk.Label(ventana_toplevel, text="Precio de Producción:").pack(pady=5)
    entry_precio_produccion = tk.Entry(ventana_toplevel)
    entry_precio_produccion.pack(pady=5)

    tk.Label(ventana_toplevel, text="Precio de Venta:").pack(pady=5)
    entry_precio_venta = tk.Entry(ventana_toplevel)
    entry_precio_venta.pack(pady=5)

    def registrar():
        nombre = entry_nombre.get()
        kilolitro = float(entry_kilolitro.get())
        precio_produccion = float(entry_precio_produccion.get())
        precio_venta = float(entry_precio_venta.get())

        crear_producto(nombre, kilolitro, precio_produccion, precio_venta)

        ventana_toplevel.destroy()

    btn_registrar = tk.Button(ventana_toplevel, text="Registrar Producto", command=registrar)
    btn_registrar.pack(pady=20)
