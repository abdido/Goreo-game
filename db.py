import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"data\data_sql.db"
# id_chara, name, hp, atk, defence, critical_damage, critical_chance, equipment = None, skin = None

    sql_create_characters_table = """CREATE TABLE IF NOT EXISTS characters (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    weapon_id integer NOT NULL,
                                    item_id integer NOT NULL,
                                    job_id integer NOT NULL,
                                    hp integer NOT NULL,
                                    attack integer  NOT NULL,
                                    defence integer NOT NULL,
                                    crd float NOT NULL,
                                    crc float NOT NULL,

                                    FOREIGN KEY (weapon_id) REFERENCES weapon (id),
                                    FOREIGN KEY (item_id) REFERENCES item (id),
                                    FOREIGN KEY (job_id) REFERENCES job (id)
                                );"""

    sql_create_weapons_table = """ CREATE TABLE IF NOT EXISTS weapons (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        type text NOT NULL,
                                        attack integer NOT NULL,
                                        crd float NOT NULL,
                                        crc float NOT NULL,
                                        effect text NOT NULL,

                                        FOREIGN KEY (type) REFERENCES weapon_types (id)
                                    ); """

    sql_create_weapon_types_table = """ CREATE TABLE IF NOT EXISTS weapon_types (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL
                                    ); """

    sql_create_items_table = """ CREATE TABLE IF NOT EXISTS items (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        type text NOT NULL,
                                        hp integer NOT NULL,
                                        attack integer NOT NULL,
                                        defence integer NOT NULL,
                                        crd float NOT NULL,
                                        crc float NOT NULL,
                                        effect text NOT NULL
                                    ); """
    
    sql_create_jobs_table = """ CREATE TABLE IF NOT EXISTS jobs (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        hp integer NOT NULL,
                                        attack integer  NOT NULL,
                                        defence integer NOT NULL,
                                        crd float NOT NULL,
                                        crc float NOT NULL
                                    ); """    

    sql_create_monsters_table = """ CREATE TABLE IF NOT EXISTS monsters (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    race text NOT NULL,
                                    hp integer NOT NULL,
                                    attack integer  NOT NULL,
                                    defence integer NOT NULL,
                                    crd float NOT NULL,
                                    crc float NOT NULL
                                    ); """


    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_weapons_table)
        create_table(conn, sql_create_monsters_table)
        create_table(conn, sql_create_jobs_table)
        create_table(conn, sql_create_characters_table)
        create_table(conn, sql_create_items_table)
        create_table(conn, sql_create_weapon_types_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()