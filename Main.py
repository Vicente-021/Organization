from tkinter import *
import sqlite3


def agregar_ubicaciones():
    nombre = entry_nombre_ubi.get()
    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()

    cursor.execute("Insert into ubicaciones (nombre) values (?)", (nombre,))
    conn.commit()
    conn.close()
    print("contenedor agregado")


def eliminar_ubicacion():
    nombre = entry_nombre_ubi_del.get()
    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()

    cursor.execute("SELECT nombre FROM ubicaciones WHERE nombre = (?)", (nombre,))
    if not cursor.fetchone():
        print(f"Error: No existe una ubicacion con Nombre: {nombre}")
        return False

    cursor.execute("Delete from ubicaciones Where nombre = (?)", (nombre,))

    conn.commit()
    print(f"Caja con ID {nombre} eliminada correctamente")

    conn.commit()
    conn.close()
    print("ubicacion eliminada")


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

Button(root, text="agregar ubicacion", command=agregar_ubicaciones).pack()
Button(root, text="Ver ubiaciones", command=mostrar_contenedores).pack()

Button(root, text="Eliminar ubicación", command=eliminar_ubicacion).pack()
root.mainloop()