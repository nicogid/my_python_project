import mysql.connector

# Put your DB configuration
def open():
    return mysql.connector.connect(host="XXXX",
                     user="XXXX",
                     passwd="XXXX",
                     db="XXXX")
def close(mydb):
    mydb.close()
