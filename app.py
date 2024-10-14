import os
from flask import Flask, jsonify, request
import pyodbc

app = Flask(__name__)

@app.route('/')
def handle():
  print('Request received')
  # data = { 
  #   "Modules" : 15, 
  #   "Subject" : "Data Structures and Algorithms",
  # } 
  
  # return jsonify(data)

  connection_string = os.environ["SQLCONNSTR_connectionString1"]
  conn = pyodbc.connect(connection_string)
  cursor = conn.cursor()
  cursor.execute("SELECT TOP 20 * FROM SalesLT.ProductCategory")

  data = { 
    "Modules" : 15, 
    "Subject" : cursor.fetchall()[0][2],
  } 
  
  return jsonify(data)

# @app.route('/hello', methods=['POST'])
# def hello():
#   print('Request received')
#   name = request.form.get('name')
#   return "bla"


if __name__ == '__main__':
   app.run()
