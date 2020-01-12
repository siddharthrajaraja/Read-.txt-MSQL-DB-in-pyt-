import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)

print(mydb)

file=open('sql.txt','r+')

ele=file.readlines()
#print(ele)
final_executable_queries=[]

for i in range(0,len(ele)):
    query=ele[i].split('mysql>')
    if len(query)==2:
        final_executable_queries.append(query[1])
        print(query[1])
        mydb.cursor().execute(query[1])
    else:
        if query!=['\n']:
            final_executable_queries.append(query[0])
            print(query[0])
            mydb.cursor().execute(query[0])
        mydb.commit()
