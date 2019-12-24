import mysql.connector
from flask import Flask, session, render_template, request, redirect, url_for
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
users = {
    "samar": {
        "username": "samar",
        "email": "samar@gmail.com",
        "password": "example",
        
    },
    "ghada": {
        "username": "ghada",
        "email": "ghada@gmail.com",
        "password": "10000",
       
    }
}

@app.route('/log_in', methods=['GET', 'POST'])
def login():

    if request.method == "POST":

        req = request.form

        username = req.get('name')
        password = req.get('id')

        if not username in users:
            print("Username not found")
            return redirect(request.url)
        else:
            user = users[username]

        if not password == user["password"]:
            print("Incorrect password")
            return redirect(request.url)
        else:
            session["USERNAME"] = user["username"]
            print(session["USERNAME"])
            print("session username set")
            return redirect(url_for('homepage'))

    return render_template("log_in.html")

@app.route('/homepage')
def homepage():

    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        user = users[username]
        print(username)
        return render_template("homepage.html", user=user)
    else:
        print("No username found in session")
        return redirect(url_for("log_in"))
    
@app.route("/sign_out")
def sign_out():

    session.pop("USERNAME", None)

    return redirect(url_for('log_in'))

@app.route('/doctors',methods = ['POST', 'GET'])
def doctors():
   if request.method == 'POST': 
      name = request.form['name']
      department = request.form['department']
      id = request.form['id']
      gender= request.form['sex']
      Birthdate=request.form['bday']
      print(name,department,id)
      sql = "INSERT INTO Doctors (name,department, id,gender,Birthdate) VALUES (%s, %s, %s,%s,%s)"
      val = (name,department,id,gender,Birthdate)
      mycursor.execute(sql, val)
      mydb.commit()   
     
      return render_template('homepage.html')
   else:
      return render_template('doctors.html')

@app.route('/viewdoctor', methods = ['POST', 'GET'])
def viewdoctor():
     if request.method == 'POST':
        return render_template('homepage.html')
     else:
        mycursor.execute("SELECT * FROM Doctors")
        row_headers=[x[0] for x in mycursor.description] 
        myresult = mycursor.fetchall()
        data={
         'message':"data retrieved",
         'rec':myresult,
         'header':row_headers
           }
        return render_template('viewdoctor.html',data=data)

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
      
      return render_template('homepage.html')
   else:
      return render_template('neonates.html')

@app.route('/viewneonates',methods = ['POST', 'GET'])
def viewneonates():
     if request.method == 'POST':
        return render_template('homepage.html')
     else:
        mycursor.execute("SELECT * FROM Neonates")
        row_headers=[x[0] for x in mycursor.description] 
        myresult = mycursor.fetchall()
        data={
         'message':"data retrieved",
         'rec':myresult,
         'header':row_headers
           }
        return render_template('viewneonates.html',data=data)

@app.route('/nurses',methods = ['POST', 'GET'])
def nurses():
   if request.method == 'POST': 
      name = request.form['name']
      Code = request.form['id']
      gender= request.form['sex']
      bday=request.form['bday']
      print(name,Code,gender,bday)
      sql = "INSERT INTO nurses (name,Code, gender,bday) VALUES (%s, %s, %s,%s)"
      val = (name,Code,gender,bday)
      mycursor.execute(sql, val)
      mydb.commit()   
     
      return render_template('homepage.html')
   else:
      return render_template('nurses.html')
  

@app.route('/viewnurses',methods = ['POST', 'GET'])
def viewnurses():
     if request.method == 'POST':
        return render_template('homepage.html')
     else:
        mycursor.execute("SELECT * FROM nurses")
        row_headers=[x[0] for x in mycursor.description] 
        myresult = mycursor.fetchall()
        data={
         'message':"data retrieved",
         'rec':myresult,
         'header':row_headers
           }
        return render_template('viewnurses.html',data=data)

@app.route('/parents',methods = ['POST', 'GET'])
def parents():
   if request.method == 'POST': 
      firstname = request.form['firstname']
      lastname = request.form['lastname']
      ssn = request.form['ssn']
      address= request.form['text']
      phone= request.form['ph']
      sex=request.form['sex']
      print(firstname,lastname,ssn,address,phone,sex)
      sql = "INSERT INTO parents (firstname,lastname,ssn,address,phone,sex) VALUES (%s, %s, %s, %s, %s, %s)"
      val = (firstname,lastname,ssn,address,phone,sex)
      mycursor.execute(sql, val)
      mydb.commit()   
     
      return render_template('homepage.html')
   else:
      return render_template('parents.html')

@app.route('/viewparents',methods = ['POST', 'GET'])
def viewparents():
     if request.method == 'POST':
        return render_template('homepage.html')
     else:
        mycursor.execute("SELECT * FROM  parents ")
        row_headers=[x[0] for x in mycursor.description] 
        myresult = mycursor.fetchall()
        data={
         'message':"data retrieved",
         'rec':myresult,
         'header':row_headers
           }
        return render_template('viewparents.html',data=data)

    
@app.route('/done',methods = ['POST', 'GET'])
def done():
     if request.method == 'POST':
        return ("hello")
     else:
        mycursor.execute("SELECT * FROM Complaints")
        row_headers=[x[0] for x in mycursor.description] 
        myresult = mycursor.fetchall()
        data={
         'message':"data retrieved",
         'rec':myresult,
         'header':row_headers
           }
        return render_template('done.html',data=data)

@app.route('/equip',methods = ['POST', 'GET'])
def equip():
   if request.method == 'POST': 
      id = request.form['id']
      LOCATION = request.form['text']
      device_name = request.form['name']
      print(id,LOCATION,device_name)
      sql = "INSERT INTO NICU (id,LOCATION,device_name) VALUES (%s, %s, %s)"
      val = (id,LOCATION,device_name)
      mycursor.execute(sql, val)
      mydb.commit()   
     
      return render_template('homepage.html')
   else:
      return render_template('equip.html')
  
@app.route('/viewequip',methods = ['POST', 'GET'])
def viewequip():
     if request.method == 'POST':
        return render_template('homepage.html')
     else:
        mycursor.execute("SELECT * FROM  NICU ")
        row_headers=[x[0] for x in mycursor.description] 
        myresult = mycursor.fetchall()
        data={
         'message':"data retrieved",
         'rec':myresult,
         'header':row_headers
           }
        return render_template('viewequip.html',data=data)

  

  

if __name__ == '__main__':
   app.run()