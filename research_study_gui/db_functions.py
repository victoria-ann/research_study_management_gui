# === some database commands ======

import pymysql
import db_config_file
from tkinter import messagebox

class DatabaseError(Exception):
    def __init__(self, e):
        super().__init__(e)


def open_database():
    try:
        con = pymysql.connect(host=db_config_file.DB_SERVER,
                              user=db_config_file.DB_USER,
                              password=db_config_file.DB_PASS,
                              database=db_config_file.DB,
                              port=db_config_file.DB_PORT)
        return con

    except pymysql.InternalError as e:
        print(e)
        raise DatabaseError(e)
    except pymysql.OperationalError as e:
        print(e)
        raise DatabaseError(e)
    except pymysql.NotSupportedError as e:
        print(e)
        raise DatabaseError(e)


def query_database(con, sql, values=None):
    try:
        cursor = con.cursor()
        cursor.execute(sql, values)
        rows = cursor.fetchall()
        num_of_rows = cursor.rowcount

    except pymysql.InternalError as e:
        print(e)
        raise DatabaseError(e)
    except pymysql.OperationalError as e:
        print(e)
        raise DatabaseError(e)
    except pymysql.ProgrammingError as e:
        print(e)
        raise DatabaseError(e)
    except pymysql.DataError as e:
        print(e)
        raise DatabaseError(e)
    except pymysql.IntegrityError as e:
        print(e)
        raise DatabaseError(e)
    except pymysql.NotSupportedError as e:
        print(e)
        raise DatabaseError(e)
    finally:
        cursor.close()
        con.close()
    return num_of_rows, rows
    
def database_error(err):
        messagebox.showinfo("Error", err)
        return False

def insert_database(con, sql, vals):
        try:
            cursor = con.cursor()
            cursor.execute(sql, vals)
            con.commit()
        except pymysql.ProgrammingError as e:
            database_error(e)
        except pymysql.DataError as e:
            database_error(e)
        except pymysql.IntegrityError as e:
            database_error(e)
        except pymysql.NotSupportedError as e:
            database_error(e)
        except pymysql.OperationalError as e:
            database_error(e)
        except pymysql.InternalError as e:
            database_error(e)
        except pymysql.DatabaseError as e:
            database_error(e)