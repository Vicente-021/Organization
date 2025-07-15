import sqlite3


def agregar_ubicaciones(nombre):
    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()

    cursor.execute("Insert into ubicaciones (nombre) values (?)", (nombre,))
    conn.commit()
    conn.close()
    print(f"contenedor {nombre} agregado.")


def eliminar_ubicacion(nombre_elim):
    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()

    cursor.execute("SELECT nombre FROM ubicaciones WHERE nombre = (?)", (nombre_elim,))
    if not cursor.fetchone():
        print(f"Error: No existe una ubicacion con nombre: {nombre_elim}")
        return False

    cursor.execute("Delete from ubicaciones Where nombre = (?)", (nombre_elim,))

    conn.commit()
    print(f"Caja con ID {nombre_elim} eliminada correctamente")

    conn.commit()
    conn.close()
    print("ubicacion eliminada")


def agregar_caja(nombre):
    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()

    cursor.execute("Insert into cajas (nombre) values (?)", (nombre, ))
    conn.commit()
    conn.close()
    print(f"contenedor {nombre} agregado.")


def eliminar_caja(nombre_elim):
    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()

    cursor.execute("Selecto from cajas where nombre = (?)", (nombre_elim, ))
    if not cursor.fetchone():
        print(f"Error: No existe una caja con el nombre: {nombre_elim}")
        return False

    conn.commit()
    conn.close()
    print("Caja eliminada")
