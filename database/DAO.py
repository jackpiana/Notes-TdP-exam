from database.f1_classes import Result, Driver

from database.DB_connect import DBConnect

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getter():
        """
        :return: lista di tuple contenenti gli attributi selezionati dalla query
        """
        conn = DBConnect.get_connection()
        result = []
        if conn is None:
            print("Connection failed")
        else:
            cursor = conn.cursor()
            query = """select *
                        from drivers"""
            cursor.execute(query)
            for row in cursor:
                result.append(row) #row è una tupla contenente tutti gli attributi selezionati dalla query
            cursor.close()
            conn.close()
        return result

    @staticmethod
    def getter_oggetti():
        """
        usa unpacking di dizionari per creare oggetti di classe avente tutte le righe di data tabella
        return: mappa key= id, value= oggetto
        """
        conn = DBConnect.get_connection()
        result = {}
        if conn is None:
            print("Connection failed")
        else:
            cursor = conn.cursor(dictionary=True)
            query = """SELECT *
                        FROM tabella
                        """
            cursor.execute(query)
            for row in cursor:
                result[row["id"]] = (Oggetto(**row))  #**row è un operatore di unpacking (espansione) di un dizionario. nb: serve che tutti i nomi degli attributi combacino
            cursor.close()
            conn.close()
        return result

    @staticmethod
    def getter_drivers():
        conn = DBConnect.get_connection()
        result = {}
        if conn is None:
            print("Connection failed")
        else:
            cursor = conn.cursor(dictionary=True)
            query = """SELECT *
                        FROM results
                        """
            cursor.execute(query)
            for row in cursor:
                result[row["driverId"]] = (Driver(**row))  #**row è un operatore di unpacking (espansione) di un dizionario. nb: serve che tutti i nomi degli attributi combacino
            cursor.close()
            conn.close()
        return result

    @staticmethod
    def getter_result():
        conn = DBConnect.get_connection()
        result = {}
        if conn is None:
            print("Connection failed")
        else:
            cursor = conn.cursor(dictionary=True)
            query = """SELECT *
                        FROM results
                        """
            cursor.execute(query)
            for row in cursor:
                result[row["resultId"]] = (Result(**row))  #**row è un operatore di unpacking (espansione) di un dizionario. nb: serve che tutti i nomi degli attributi combacino
            cursor.close()
            conn.close()
        return result


if __name__ == '__main__':
    DAO = DAO()
    for item in DAO.getter_result().values():
        print(type(item), item)


