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


def eliminar_ubicacion(nombre_elim, menu_opciones_ubi, ubicacion_seleccionada):
    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()

    cursor.execute("SELECT nombre FROM ubicaciones WHERE nombre = (?)", (nombre_elim,))
    if not cursor.fetchone():
        print(f"Error: No existe una ubicacion con nombre: {nombre_elim}")
        return False

    cursor.execute("Delete from ubicaciones Where nombre = (?)", (nombre_elim,))

    conn.commit()
    conn.close()
    print("ubicacion eliminada")
    act_ubicaciones(menu_opciones_ubi, ubicacion_seleccionada)


def act_cajas(menu_opciones_cajas, caja_seleccionada):
    menu_opciones_cajas['menu'].delete(0, 'end')

    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()
    nuevas_cajas = [fila[0] for fila in cursor. execute("Select nombre from cajas").fetchall()]
    conn.close()

    for caja in nuevas_cajas:
        menu_opciones_cajas['menu'].add_command(label=caja,
                                                command=lambda valor=caja: caja_seleccionada.set(valor))

    if nuevas_cajas:
        caja_seleccionada.set(nuevas_cajas[0])
    else:
        caja_seleccionada.set("Sin cajas")


def agregar_caja(nombre, ubicacion, menu_opciones_cajas, caja_seleccionada):
    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()

    cursor.execute("Insert into cajas (nombre, ubicacion_nombre) values (?, ?)", (nombre, ubicacion))
    conn.commit()
    conn.close()
    act_cajas(menu_opciones_cajas, caja_seleccionada)
    print(f"contenedor {nombre} agregado.")


def eliminar_caja(nombre_elim, menu_opciones_cajas, caja_seleccionada):
    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()

    cursor.execute("Select nombre from cajas where nombre=(?)", (nombre_elim,))
    if not cursor.fetchone():
        print(f"Error: No existe una caja con nombre: {nombre_elim}")
        return False

    cursor.execute("Delete from cajas where nombre = (?)", (nombre_elim,))

    conn.commit()
    conn.close()

    print("Caja eliminada")
    act_cajas(menu_opciones_cajas, caja_seleccionada)


def agregar_item(nombre, caja):
    conn = sqlite3.connect("organize.db")
    cursor = conn.cursor()

    cursor.execute("insert into items (nombre, caja_nombre) values (?, ?)", (nombre, caja))
    conn.commit()
    conn.close()
    print(f"item {nombre} agregado.")


