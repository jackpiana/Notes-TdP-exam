from database.bike_store_classes import Product
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
            query = """
            
                    """
            cursor.execute(query)
            for row in cursor:
                result.append(row) #row è una tupla contenente tutti gli attributi selezionati dalla query
            cursor.close()
            conn.close()
        return result

# **row è un operatore di unpacking (espansione) di un dizionario, nb: serve che tutti i nomi degli attributi combacino
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
            query = """
                    
                    """
            cursor.execute(query)
            for row in cursor:
                result[row["id"]] = (Oggetto(**row))
            cursor.close()
            conn.close()
        return result

    @staticmethod
    def getter_prodotti():
        conn = DBConnect.get_connection()
        result = {}
        if conn is None:
            print("Connection failed")
        else:
            cursor = conn.cursor(dictionary=True)
            query = """
                    select *
                    from products p 
                            """
            cursor.execute(query)
            for row in cursor:
                result[row["product_id"]] = Product(Result(**row))
            cursor.close()
            conn.close()
        return result


if __name__ == '__main__':
    DAO = DAO()

    for item in DAO.getter():
        print(type(item), item)

    for item in DAO.getter_prodotti().values():
        print(type(item), item)


