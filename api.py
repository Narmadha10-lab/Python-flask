from flask import Flask
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)
todos = {
1:{"task": "task 1","summary":"summary of  task 1"},
2:{"task": "task 2","summary":"summary of  task 2"},
3:{"task": "task 3","summary":"summary of  task 3"}
}
task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task",type=str,help="Task is rquired", required=True)
task_post_args.add_argument("summary",type=str,help="summary is rquired",  required=True)

class ToDoList(Resource):
	def get(self):
		return todos

class ToDo(Resource):
	def get(self, todo_id):
		return todos[todo_id]
	
	def post(self, todo_id):
		args = task_post_args.Parse_args()
		if todo_id in todos:
			abort(409, "Task ID already taken")
		todos[todo_id] = {"task" : args["tasks"],"summary": args["summary"]}
		return todos[todo_id]

api.add_resource(ToDo, '/todos/<int:todo_id>')
api.add_resource(ToDoList, '/todos')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=105)