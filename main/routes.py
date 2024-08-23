from flask import Blueprint, render_template, request, redirect, url_for
from extension import mongo
from bson import ObjectId

main = Blueprint('main', __name__)

@main.route("/")
def index():
    if mongo.db.task.find():
        tasks=mongo.db.task.find()
        return render_template('index.html', tasks=tasks)
    return render_template('index.html')

@main.route('/add', methods=['POST'])
def add_todo():
    # Insert a new task into the 'task' collection
    todo_content = request.form.get('content')
    if todo_content:
        mongo.db.task.insert_one({'content': todo_content, 'complete': False})
    return redirect(url_for('main.index'))

@main.route('/complete/<task_id>')
def complete_todo(task_id):
    # Mark the task as complete by updating the 'complete' field to True
    mongo.db.task.update_one({'_id': ObjectId(task_id)}, {'$set': {'complete': True}})
    return redirect(url_for('main.index'))

@main.route('/delete/<task_id>')
def delete_todo(task_id):
    # Delete the task from the 'task' collection
    mongo.db.task.delete_one({'_id': ObjectId(task_id)})
    return redirect(url_for('main.index'))