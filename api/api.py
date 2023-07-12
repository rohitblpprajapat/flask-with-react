from flask_restful import Api, Resource
from flask import Flask, request

app = Flask(__name__)
api = Api(app)

todos = {}
class ToDo(Resource):
    def get(self):
        return todos,200
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}
    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}
    
api.add_resource(ToDo, '/<string:todo_id>')

if __name__ == "__main__":
    app.run(debug=True)