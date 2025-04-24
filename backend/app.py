from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid 


app = Flask(__name__) 
# Enable CORS for all routes it will allow all origins to access the API
# In production, you should restrict origins to your frontend's domain
CORS(app, resources={r"/*": {"origins": "*"}})

todos = [
    {"id": 1, "task": "Learn Flask", "completed": False},
    {"id": 2, "task": "Build a REST API", "completed": False},
]


@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/api/todos', methods=['POST'])
def add_todo():
    new_todo = request.get_json()
    new_todo['id'] = len(todos) + 1
    new_todo['completed'] = False
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    updated_data = request.get_json()
    todo.update(updated_data)
    return jsonify(todo), 200

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return jsonify({"message": "Todo deleted"}), 200

@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify(todo), 200


