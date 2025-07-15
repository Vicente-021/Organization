from tkinter import *
import sqlite3
from creaciones import *


def mostrar_contenedores():
    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ubicaciones")
    for row in cursor.fetchall():
        print(f"id: {row[0]}, nombre: {row[1]}")
    conn.close()


root = Tk()
root.title("Organizador")

Label(root, text="Nombre: ").pack()
entry_nombre_ubi = Entry(root)
entry_nombre_ubi.pack()

Label(root, text="Quitar ubicacion").pack()
entry_nombre_ubi_del = Entry(root)
entry_nombre_ubi_del.pack()

Button(root, text="agregar ubicacion", command=agregar_ubicaciones(entry_nombre_ubi.get())).pack()
Button(root, text="Ver ubiaciones", command=mostrar_contenedores).pack()
Button(root, text="Eliminar ubicación", command=eliminar_ubicacion(entry_nombre_ubi_del.get())).pack()

root.mainloop()
