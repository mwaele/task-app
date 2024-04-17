from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

# Creating a flask applicationn
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
db = SQLAlchemy(app)

# Define a task model
class Task(db):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    date = db.Column()
    priority = db.Column()
    status = db.Column(db.Boolean, default=False)

# Defining a route and a view
@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add-task', method=['POST'])
def add_task():
    task = request.form['task']
    date = request.form['date']
    priority = request.form['priority']
    status = request.form['status']
    Task.create_task(task, date, priority, status)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>')
def update_task(task_id):
    task = Task.get_task(task_id)
    task.status = not task.status
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.all(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))


# Running the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)