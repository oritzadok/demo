import os
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def handle():
  print('Request received')
  data = { 
    "Modules" : 15, 
    "Subject" : "Data Structures and Algorithms", 
  } 
  
  return jsonify(data)

# @app.route('/hello', methods=['POST'])
# def hello():
#   print('Request received')
#   name = request.form.get('name')
#   return "bla"


if __name__ == '__main__':
   app.run()
