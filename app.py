import os
from flask import Flask, jsonify, request
import pyodbc

app = Flask(__name__)

@app.route('/')
def handle():
  print('Request received')

  connection_string = os.environ["SQLCONNSTR_connectionString1"]
  conn = pyodbc.connect(connection_string)
  cursor = conn.cursor()
  cursor.execute("SELECT TOP 20 * FROM SalesLT.ProductCategory")
  cursor.close()
  conn.close()

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
