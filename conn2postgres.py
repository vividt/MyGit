import psycopg2
import time
import datetime

for i in range(1, 1000):
   try:
      #establishing the connection
      conn = psycopg2.connect(
         database="postgres", user='qa_user', password='2kA5Cr3JfBGa{_D@', host='pgbouncer-dev.nextdrive.io', port= '15432'
      )
      #Creating a cursor object using the cursor() method
      cursor = conn.cursor()
      #Executing an MYSQL function using the execute() methodls
      cursor.execute("select "+str(i))
      # Fetch a single row using fetchone() method.
      data = cursor.fetchone()
      print("Connection established at ", datetime.datetime.now()) 
        
   except:
      print("Connection failed at ", datetime.datetime.now())
   
   #Closing the connection
   conn.close()

   i=i+1
   time.sleep(1)    



