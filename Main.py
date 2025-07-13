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


root = Tk()
root.title("Organizador")

Label(root, text="Nombre: ").pack()
entry_nombre_ubi = Entry(root)
entry_nombre_ubi.pack()


def mostrar_contenedores():
    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ubicaciones")
    for row in cursor.fetchall():
        print(f"id: {row[0]}, nombre: {row[1]}")
    conn.close()


Button(root, text="agregar ubicacion", command=agregar_ubicaciones).pack()
Button(root, text="Ver ubiaciones", command=mostrar_contenedores).pack()

root.mainloop()