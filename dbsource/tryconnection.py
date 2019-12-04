import mysql.connector
mydb = mysql.connector.Connect(host = "127.0.0.1", user = "root", password= "Ab5524%@%", database = "medico_plus", auth_plugin='mysql_native_password', buffered = True)
mydbc = mydb.cursor()
mydbc.execute('select * from doctor;')
for i in mydbc:
        for j in i:
                print(j)
        print()
mydbc.execute('select * from department;')
for i in mydbc:
        for j in i:
                print(j)
        print()