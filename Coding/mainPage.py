
from flask import Flask, jsonify,request

app = Flask(__name__)
@app.route('/path_of_the_response')
def ReturnJSON():
  pass


if __name__ == "__main__":
  app.run(debug=True)