import mysql.connector


def connection():
    cnx = mysql.connector.connect(user='ingridma_neural', password='neural123',
                              host='162.241.2.79',
                              database='ingridma_neural')
    return cnx

# def connection():
#     cnx = mysql.connector.connect(user='ingridma_thuran', password='123qwe',
#                               host='162.241.2.79',
#                               database='ingridma_politica')
#     return cnx