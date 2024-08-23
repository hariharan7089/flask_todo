from flask import Flask, render_template, request, redirect, url_for
from bson import ObjectId
import pymongo

app = Flask(__name__, template_folder="templates")

mongo = pymongo.MongoClient("mongodb+srv://hariharank:HARIHARANK@cluster0.7njml.mongodb.net/")
db = mongo["todo"]
collection = db["task"]

@app.route("/")
def index():
    tasks = collection.find()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_todo():
    todo_content = request.form.get('content')
    if todo_content:
        collection.insert_one({'content': todo_content, 'complete': False})
    return redirect(url_for('index'))

@app.route('/complete/<task_id>')
def complete_todo(task_id):
    collection.update_one({'_id': ObjectId(task_id)}, {'$set': {'complete': True}})
    return redirect(url_for('index'))

@app.route('/delete/<task_id>')
def delete_todo(task_id):
    collection.delete_one({'_id': ObjectId(task_id)})
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
