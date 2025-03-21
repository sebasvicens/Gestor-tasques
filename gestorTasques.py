import constants as const
import mysql.connector

# Funció per obrir la connexió amb la base de dades
def obrirConnexio():

    # Connexió a la base de dades
    conn = mysql.connector.connect(
        host=const.HOST,
        user=const.USER,
        port=const.PORT,
        database=const.DATABASE
    )

    cursor = conn.cursor()

    return [conn, cursor]

def tancarConnexio(cursor, conn):
    # Tancar la connexió
    cursor.close()
    conn.close()

def tascaToString(tasca):
    print()
    print(f"########## TASCA ID: {tasca[0]} ##########")
    print(f"Titol: {tasca[1]}")
    print(f"Descripció: {tasca[2]}")
    print(f"Data creació: {tasca[3]}")
    print(f"Data venciment: {tasca[4]}")
    print(f"Estat: {tasca[5]}")
    print(f"Prioritat: {tasca[6]}")
    print(f"#################################")
    print()

def mostrarTasques(cursor):
    query_select_tasks = "SELECT * FROM tasklist"

    # Executa una consulta SQl
    cursor.execute(query_select_tasks)

    # Obtenir els resultats
    resultats = cursor.fetchall()
    for fila in resultats:
        tascaToString(fila)

def afegirTasques(cursor, conn):
    titol = input("Títol: ")
    descripcio = input("Descripció: ")
    creacio = input("Data inici (YYYY-MM-DD): ")
    venciment = input("Data tancament (YYYY-MM-DD): ")
    estat = input("Estat: ")
    prioritat = input("Prioritat: ")

    query_insert_task = "INSERT INTO TASKLIST (titol, descripcio, data_creacio, data_venciment, estat, prioritat) " \
    "VALUES ('" + titol + "' , '" + descripcio + "' , '" +creacio + "' , '" + venciment + "' , '" + estat + "' , '" + prioritat + "')"

    cursor.execute(query_insert_task)
    conn.commit() # Important per desar els canvis

def eliminarTasques(cursor, conn):
    id = input("Quina tasca vols eliminar? (Insereix l'ID corresponent)")

    query_remove_task = "DELETE FROM TASKLIST WHERE ID = " + id

    cursor.execute(query_remove_task)
    conn.commit()

def modificarTasques(cursor, conn):
    id = input("Quina tasca vols actualitzar? (Insereix l'ID corresponent)")

    query_select_tasks = "SELECT * FROM tasklist WHERE ID = " + id

    # Executa una consulta SQl
    cursor.execute(query_select_tasks)

    # Obtenir els resultats
    resultats = cursor.fetchall()
    for fila in resultats:
        tascaToString(fila)

    titol = input("Títol: ")
    descripcio = input("Descripció: ")
    creacio = input("Data inici (YYYY-MM-DD): ")
    venciment = input("Data tancament (YYYY-MM-DD): ")
    prioritat = input("Prioritat: ")

    query_update_task = "UPDATE tasklist " \
    "SET titol = '" + titol + "', descripcio = '" + descripcio + "', " \
    "data_creacio = '" + creacio + "', data_venciment = '" + venciment + "', " \
    "prioritat = '" + prioritat + "' " \
    "WHERE id = " + id

    cursor.execute(query_update_task)
    conn.commit()

def canviarEstat(cursor, conn):
    id = input("Quina tasca vols canviar l'estat? (Insereix l'ID corresponent)")

    query_select_tasks = "SELECT * FROM tasklist WHERE ID = " + id

    # Executa una consulta SQl
    cursor.execute(query_select_tasks)

    # Obtenir els resultats
    resultats = cursor.fetchall()
    for fila in resultats:
        tascaToString(fila)

    estat = input("Introdueix el nou estat de la tasca: ")

    query_update_task = "UPDATE tasklist " \
    "SET estat = '" + estat + "' " \
    "WHERE id = " + id

    cursor.execute(query_update_task)
    conn.commit()


def menu(cursor, conn):

    opcio = 0

    menu = "Quina opció vols dur a terme?\n1. Mostrar tasques\n2. Afegir tasques\n3. Eliminar tasques\n4. Modificar tasques\n5. Canviar estat d'una tasca\n6. Sortir\n"

    while opcio != 6:
        opcio = int(input(menu))

        if opcio == 1:
            print("Has triat la opció 1. Visualització de tasques:")
            mostrarTasques(cursor)

        elif opcio == 2:
            print("Has triat la opció 2. Afegir tasques:")
            afegirTasques(cursor, conn)

        elif opcio == 3:
            print("Has triat la opció 3. Eliminació de tasques:")
            eliminarTasques(cursor, conn)

        elif opcio == 4:
            print("Has triat la opció 4. Modificació de tasques:")
            modificarTasques(cursor, conn)

        elif opcio == 5:
            print("Has triat la opció 5. Canvi d'estat de les tasques:")
            canviarEstat(cursor, conn)

        elif opcio == 6:
            print("Has triat la opció 6. Gràcies per utilitzar l'aplicació")
            break
        
        else:
            print("L'opció que has triat no és vàlida. Per favor, introdueix una opció vàlida.")



# Obrim connexió
[conn, cursor] = obrirConnexio()

# Executar menu
menu(cursor, conn)

# Tancam la connexió
tancarConnexio(conn, cursor)