from flask import Flask, url_for, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func

app = Flask(__name__, template_folder="template")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    creates_at = db.Column(db.DateTime, default=func.now())

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title} - {self.creates_at}"


@app.route("/", methods=["GET", "POST"])
def fun():
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    alltodos = Todo.query.all()
    # print(alltodos)
    return render_template("todo_app.html", alltodos=alltodos)


@app.route("/edit")
def edit():
    return "showing"


@app.route("/delete/<int:sno>")
def delete(sno):
    # Retrieve the instance to be deleted
    todo = Todo.query.filter_by(sno=sno).first()

    # Check if the instance exists
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return redirect("/")
    else:
        return "Todo item not found", 404


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/back")
def back():
    return redirect("/")


@app.route("/update/<int:sno>", methods=["GET", "POST"])
def update(sno):

    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    todo = Todo.query.filter_by(sno=sno).first()
    return render_template("update.html", todo=todo)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
