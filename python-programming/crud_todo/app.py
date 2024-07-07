from flask import Flask, render_template, request, redirect 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func

app = Flask(__name__ ,template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)  

class Todo(db.Model):
  sno = db.Column(db.Integer,primary_key=True ,autoincrement=True)
  
  title = db.Column(db.String(100),nullable=False)
  desc = db.Column(db.String(200),nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self) -> str:
     return f"{self.sno} - {self.title} -{self.created_at}"


  

@app.route('/',methods=['GET','POST'])
def Home():
  if request.method=='POST':
    title = request.form['title']
    desc = request.form['desc']
    todo = Todo(title=title,desc=desc)
    db.session.add(todo)
    db.session.commit()
    return redirect('/')    
  
  all_todos = Todo.query.all()
  return render_template('index.html',all_todos=all_todos)


@app.route('/delete/<int:sno>')
def delete(sno):
  todo =Todo.query.filter_by(sno=sno).first()
  db.session.delete(todo)
  db.session.commit()
  return redirect('/')
  
  
@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
  
  if request.method == 'POST':
    
    title = request.form['title']
    desc= request.form['desc']
    
    todo =Todo.query.filter_by(sno=sno).first()
    todo.title = title
    todo.desc = desc
    db.session.add(todo)
    db.session.commit()
    return redirect('/')
  todo =Todo.query.filter_by(sno=sno).first()
  return render_template('update.html',todo=todo)
  


if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run(debug=True)