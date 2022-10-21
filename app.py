from flask import Flask,  render_template, url_for
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)

class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

# def __repr__(self):
#     return '<Task %r>' % self.id

def __repr__(self):
        return f'<todo {self.firstname}>'

# def __init__(self,id, content, completed, date_created):
#    self.id = id
#    self.content = content
#    self.completed = completed
#    self.date_created = date_created

@app.route('/')
def index():
    print("Haiiii")
    return "Hii sir"

@app.route('/next')
def next():
    return render_template('next.html')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page1')
def page1():
    return render_template('/page1.html')

if __name__ == "__main__":
    app.run(debug=True)