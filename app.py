import os
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def handle():
  print('Request received')
  return "bla"

@app.route('/hello', methods=['POST'])
def hello():
  print('Request received')
  name = request.form.get('name')
  return "bla"


if __name__ == '__main__':
   app.run()
