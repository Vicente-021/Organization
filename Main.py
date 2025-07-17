from tkinter import *
import sqlite3
import creaciones
from creaciones import *

columna_ubicaciones = 0
columna_cajas = 1
columna_items = 2


def mostrar_ubicaciones():
    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ubicaciones")

    for row in cursor.fetchall():
        print(f"id: {row[0]}, nombre: {row[1]}")
    conn.close()


def mostrar_cajas():
    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()
    cursor.execute("Select * from cajas")

    for row in cursor.fetchall():
        print(f"id:{row[0]}, nombre: {row[1]}, ubicacion: {row[2]}")


root = Tk()
root.title("Organizador")
root.geometry("500x200")

# Labels y entradas para la creación y eliminación de las ubicaciones
Label(root, text="Nombre Ubicación: ").grid(column=columna_ubicaciones, row=0, padx=10)
entry_nombre_ubi = Entry(root)
entry_nombre_ubi.grid(column=columna_ubicaciones, row=1, padx=10)

# Botones para la creación, eliminación y visualización de las ubicaciones
Button(root,
       text="Agregar ubicacion",
       command=lambda: creaciones.agregar_ubicaciones(entry_nombre_ubi.get(),
                                                      menu_opciones_ubi,
                                                      ubicacion_seleccionada)).grid(column=columna_ubicaciones, row=4, padx=10)
Button(root,
       text="Eliminar ubicación",
       command=lambda: creaciones.eliminar_ubicacion(entry_nombre_ubi.get(),
                                                     menu_opciones_ubi,
                                                     ubicacion_seleccionada)).grid(column=columna_ubicaciones, row=5, padx=10)

Button(root,
       text="Ver ubiaciones",
       command=mostrar_ubicaciones).grid(column=columna_ubicaciones, row=6, padx=10)


# Visualizacion de las ubicaciones
ubicacion_seleccionada = StringVar()
ubicacion_seleccionada.set("Seleccionar ubicación")

ubicaciones = []
menu_opciones_ubi = OptionMenu(root, ubicacion_seleccionada, "-", *ubicaciones)
menu_opciones_ubi.grid(column=columna_ubicaciones, row=7, padx=10, pady=5)
creaciones.act_ubicaciones(menu_opciones_ubi, ubicacion_seleccionada)

# Labels y entradas para ingresar nombres de cajas, eliminación y creación
Label(root, text="Nombre Caja: ").grid(column=columna_cajas, row=0, padx=10)
entry_nombre_caja = Entry(root)
entry_nombre_caja.grid(column=columna_cajas, row=1, padx=10)

# Botones para la creación, eliminación y visualización de las cajas
Button(root,
       text="Agregar caja",
       command=lambda: creaciones.agregar_caja(entry_nombre_caja.get(),
                                               ubicacion_seleccionada.get(),
                                               menu_opciones_cajas,
                                               caja_seleccionada)).grid(column=columna_cajas, row=4, padx=10)
Button(root,
       text="Quitar caja",
       command=lambda: creaciones.eliminar_caja(entry_nombre_caja.get(),
                                                menu_opciones_cajas,
                                                caja_seleccionada)).grid(column=columna_cajas, row=5, padx=10)
Button(root,
       text="Ver cajas",
       command=mostrar_cajas).grid(column=columna_cajas, row=6, padx=10)

# Visualizacion de las cajas
caja_seleccionada = StringVar()
caja_seleccionada.set("Seleccionar caja")

cajas = []
menu_opciones_cajas = OptionMenu(root, caja_seleccionada, "-", *cajas)
menu_opciones_cajas.grid(column=columna_cajas, row=7, padx=10, pady=5)
act_cajas(menu_opciones_cajas, caja_seleccionada)

# Labels y entradas para la creacion de items
Label(root, text="Nombre item: ").grid(column=columna_items, row=0, padx=10)
entry_nombre_item = Entry(root)
entry_nombre_item.grid(column=columna_items, row=1, padx=10)

# Botones para la creación, eliminación y visualización de los items


root.mainloop()
