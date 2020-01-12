import mysql.connector
import random
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="alumni_system"
)

mycursor = mydb.cursor()
student=['siddharth','aman','balvinder','srikant','mayank','akilesh','shayantan','pranay','akshay','ritik','aadit','riya','gaurav','ruturaj','siddhu','aniket','sanket','kaushal','mahendra','manthan']
for i in student:
    a=random.randint(1000,9999)
    b=random.randint(1000,9999) 
    c=random.randint(1000,9999)
    n=str(a)+str(b)+str(c)
    aadhar_num=int(n)
    sql = "UPDATE student SET aadhar_id = %s WHERE name = %s"
    val = (aadhar_num, i)
    mycursor.execute(sql, val)

mydb.commit()
