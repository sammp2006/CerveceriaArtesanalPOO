import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from productos import main_productos
from clientes import main_clientes
from ventas import main_ventas
from facturacion import main_facturacion

def iniciar_programa():
    ventana = tk.Tk()
    ventana.title("Programa Principal")

    ventana.geometry("400x400")
    ventana.config(bg="#FFEC99")  
    bienvenida = tk.Label(ventana, text="Bienvenido a la cerveceria artesanal", font=("Helvetica", 16), bg="#FFEC99", fg="black")
    bienvenida.pack(pady=10)

    try:
        logo_imagen = Image.open("./static/logo.png")
        logo_imagen = logo_imagen.resize((100, 100))  # Ajusta el tamaño
        logo_imagen_tk = ImageTk.PhotoImage(logo_imagen)

        canvas = tk.Canvas(ventana, width=120, height=120, bg="#FFEC99", bd=0, highlightthickness=2)
        canvas.create_rectangle(0, 0, 120, 120, outline="black", width=4)  # Contorno negro
        canvas.create_image(60, 60, image=logo_imagen_tk)
        canvas.pack(pady=10)

    except Exception as e:
        print(f"Error al cargar el logo: {e}")
    
    def abrir_seccion(seccion):
        ventana.destroy()
        if seccion == "Productos":
            main_productos(iniciar_programa)

        elif seccion == "Clientes":
            main_clientes(iniciar_programa)

        elif seccion == "Facturacion":
            main_facturacion(iniciar_programa)
        
        elif seccion == "Ventas":
            main_ventas(iniciar_programa)
            
        else:
            print("Error, reinicia el programa")
        print(f"Abrir {seccion}")

    boton_productos = tk.Button(ventana, text="Modulo de Productos", command=lambda: abrir_seccion("Productos"), 
                                bg="yellow", fg="black", relief="solid", bd=2)
    boton_productos.pack(pady=5, fill="x")

    boton_clientes = tk.Button(ventana, text="Modulo de Clientes (+ Ventas y Facturacion)", command=lambda: abrir_seccion("Clientes"), 
                               bg="yellow", fg="black", relief="solid", bd=2)
    boton_clientes.pack(pady=5, fill="x")

    nota_pie_pagina = tk.Label(ventana, text="Para registrar una venta o facturarla \n primero seleccione el cliente en cuestion", relief="solid", bd=2)
    nota_pie_pagina.pack(pady=5, fill="x")

    boton_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.quit, bg="red", fg="black", relief="solid", bd=2)
    boton_cerrar.pack(pady=10, fill="x")

    ventana.mainloop()

def run():
    iniciar_programa()

if __name__ == "__main__":
    run()

