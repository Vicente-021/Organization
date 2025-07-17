import sqlite3


def act_ubicaciones(menu_opciones_ubi, ubicacion_seleccionada):
    menu_opciones_ubi['menu'].delete(0, 'end')

    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()
    nuevas_opciones = [fila[0] for fila in cursor.execute("SELECT nombre FROM ubicaciones").fetchall()]
    conn.close()

    for opcion in nuevas_opciones:
        menu_opciones_ubi['menu'].add_command(label=opcion,
                                              command=lambda valor=opcion: ubicacion_seleccionada.set(valor))

    if nuevas_opciones:
        ubicacion_seleccionada.set(nuevas_opciones[0])
    else:
        ubicacion_seleccionada.set("Sin ubicaciones")


def agregar_ubicaciones(nombre, menu_opciones_ubi, ubicacion_seleccionada):
    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()

    cursor.execute("Insert into ubicaciones (nombre) values (?)", (nombre,))
    conn.commit()
    conn.close()
    print(f"contenedor {nombre} agregado.")
    act_ubicaciones(menu_opciones_ubi, ubicacion_seleccionada)


def eliminar_ubicacion(nombre_elim,menu_opciones_ubi, ubicacion_seleccionada):
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
    act_ubicaciones(menu_opciones_ubi, ubicacion_seleccionada)


def agregar_caja(nombre, ubicacion):
    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()

    cursor.execute("Insert into cajas (nombre, ubicacion_nombre) values (?, ?)", (nombre, ubicacion))
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
