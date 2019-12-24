from flask import Flask,redirect, url_for, request,render_template,session
import mysql.connector
import os
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mysql",
  database="Neonatal"
)
mycursor = mydb.cursor()
app = Flask(__name__)
app.secret_key = os.urandom(24)
mycursor.execute("SELECT Doctors.id FROM Doctors")
myresult = mycursor.fetchall()
mycursor.execute("SELECT Doctors.name FROM Doctors")
result=mycursor.fetchall()

@app.route('/log_in', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST': 
     
        req = request.form
        Name= req.get('name')
        ID= req.get('id')
        mycursor.execute("SELECT * From Neonates JOIN DOC_Neo ON Neonates.id=DOC_Neo.N_code JOIN Doctors ON DOC_Neo.D_code=Doctors.id WHERE Doctors.id=%s",(ID,))
        
        if not (ID,) in myresult:
            session["USERNAME"] = Name
            print(session["USERNAME"])
            print("correct id")
            print(ID)
            return redirect(url_for('doc_neo'))
            
        else:
            print('incorrect')
            return redirect(request.url)
                
                
   return render_template("log_in.html")

@app.route('/doc_neo')
def doc_neo():

    if not session.get("USERNAME") is None:
        Name = session.get("USERNAME")
        
    else:
        print("No username found in session")
        return redirect(url_for("log_in"))
   
    data = mycursor.fetchall()
    return render_template('doc_neo.html',data=data,Name=Name)

@app.route("/sign_out")
def sign_out():

    session.pop("USERNAME", None)

    return redirect(url_for('log_in'))

@app.route('/neonates',methods = ['POST', 'GET'])
def neonates():
   if request.method == 'POST': 
      firstname = request.form['firstname']
      lastname = request.form['lastname']
      id = request.form['id']
      birthdate=request.form['bday']
      gender= request.form['sex']
      status=request.form['text']
      print(firstname,lastname,id)
      sql = "INSERT INTO Neonates (firstname,lastname,id,birthdate,gender,status) VALUES (%s, %s, %s,%s,%s,%s)"
      val = (firstname,lastname,id,birthdate,gender,status)
      mycursor.execute(sql, val)
      mydb.commit() 
      
      return ('Done')
   else:
      return render_template('neonates.html')

                

if __name__ == '__main__':
   app.run()
    
     
    


