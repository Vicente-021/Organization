import sqlite3

conn = sqlite3.connect("organize.db")
cursor = conn.cursor()

cursor.execute("""
    create table if not exists ubicaciones (
    id integer primary key autoincrement,
    nombre text not null unique
    );
    """)

cursor.execute("""
    create table if not exists cajas (
    id integer primary key autoincrement,
    nombre text not null,
    ubicacion_nombre text references ubicaciones (nombre),
    id_caja_padre integer references cajas(id)
    );
    """)

cursor.execute("""
    create table if not exists items (
    id integer primary key autoincrement,
    nombre text not null,
    descripcion text,
    caja_id bigint references cajas (id)
    );
    """)


conn.commit()

