import dbconfig as db

try:
    mydb = db.open()
    #print(mydb)
    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        print(x)

    mycursor.execute("SELECT * FROM  todoitems")

    print(mycursor.fetchall())

finally:
    db.close(mydb)
