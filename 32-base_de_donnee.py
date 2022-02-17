

import sqlite3


try:
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()


    # my_username=("memo",)

    # cursor.execute("select * from t_users where user_name= ?", my_username)

    # print(cursor.fetchone()[1])

    # new_user=(cursor.lastrowid,"toto",20)

    # cursor.execute("insert into t_users values (?,?,?)", new_user)
    # connection.commit()

    cursor.execute("select * from t_users")

    #print(cursor.fetchall())

    for row in cursor.fetchall():
        print(row[1])
except Exception as e:
    print("[ERREUR]",e)
    connection.rollback()
finally:     
    connection.close()



    
