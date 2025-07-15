from tkinter import *
import sqlite3
import creaciones
from creaciones import *


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
        print(f"id:{row[0]}, nombre: {row[1]}")


root = Tk()
root.title("Organizador")
root.geometry("500x200")

# Labels y entradas para la creación y eliminación de las ubicaciones
Label(root, text="Nombre Ubicación: ").grid(column=0, row=0, padx=10)
entry_nombre_ubi = Entry(root)
entry_nombre_ubi.grid(column=0, row=1, padx=10)

Label(root, text="Quitar ubicacion").grid(column=0, row=2, padx=10)
entry_nombre_ubi_del = Entry(root)
entry_nombre_ubi_del.grid(column=0, row=3, padx=10)

# Botones para la creación, eliminación y visualización de las ubicaciones
Button(root,
       text="Agregar ubicacion",
       command=lambda: creaciones.agregar_ubicaciones(entry_nombre_ubi.get())).grid(column=0, row=4, padx=10)
Button(root,
       text="Eliminar ubicación",
       command=lambda: creaciones.eliminar_ubicacion(entry_nombre_ubi_del.get())).grid(column=0, row=5, padx=10)

Button(root,
       text="Ver ubiaciones",
       command=mostrar_ubicaciones).grid(column=0, row=6, padx=10)

# Labels y entradas para ingresar nombres de cajas, eliminación y creación
Label(root, text="Nombre Caja: ").grid(column=1, row=0, padx=10)
entry_nombre_caja = Entry(root)
entry_nombre_caja.grid(column=1, row=1, padx=10)

Label(root, text="Quitar caja: ").grid(column=1, row=2, padx=10)
entry_nombre_caja_elim = Entry(root)
entry_nombre_caja_elim.grid(column=1, row=3, padx=10)

# Botones para la creación, eliminación y visualización de las cajas
Button(root,
       text="Agregar caja",
       command=lambda: creaciones.agregar_caja(entry_nombre_caja.get())).grid(column=1, row=4, padx=10)
Button(root,
       text="Quitar caja",
       command=lambda: creaciones.eliminar_caja(entry_nombre_caja_elim.get())).grid(column=1, row=5, padx=10)
Button(root,
       text="Ver cajas",
       command=mostrar_cajas).grid(column=1, row=6, padx=10)

root.mainloop()
