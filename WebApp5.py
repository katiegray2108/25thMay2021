from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app=Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/school'

db=SQLAlchemy(app)

class school(db.model):
    RegNo=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.String(80))
    Marks=db.Column(db.Integer)

student=school()

@app.route("/addrecord")
def addrecord():
    student.RegNo=21
    student.Name="Katie"
    student.Marks=43
    db.session.add(student)
    db.session.commit()
    return "record inserted"

app.run(debug=True)
