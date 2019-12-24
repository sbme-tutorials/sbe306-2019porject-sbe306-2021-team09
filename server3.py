import mysql.connector
from flask import Flask, request,render_template


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mysql",
  database="Neonatal"
)
mycursor = mydb.cursor()
app = Flask(__name__)

@app.route('/')
def homepage():
    
    return render_template('home_page.html')

@app.route('/sign_in',methods = ['POST', 'GET'])
def sign_in():
   if request.method == 'POST': 
      name = request.form['name']
      specialrequest = request.form['complaint']
      
      print(name,specialrequest)
      sql = "INSERT INTO Complaints(name,specialrequest) VALUES (%s, %s)"
      val = (name,specialrequest)
      mycursor.execute(sql, val)
      mydb.commit()   
      
      return ("Done")
   else:
      return render_template('sign_in.html')


if __name__ == '__main__':
   app.run()


