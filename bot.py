from flask import Flask, request, jsonify
import json
import requests
import os

app = Flask(__name__)
port = int(os.environ["PORT"])
print(port)

@app.route('/', methods=['POST'])
def index():
  print(port)
  data = json.loads(request.get_data().decode('utf-8'))

  # FETCH THE CRYPTO NAME
  defwords = data["nlp"]["entities"]["defwords"][0]["raw"]

  # FETCH DATA
  r = requests.get("https://coveo.concur.concurtech.org/secured-intranet-search#"+defwords+"t=Tab_All&sort=relevancy")

  return jsonify(
    status=200,
    replies=[{
      'type': 'text',
      'content': 'Here are the top results for te definition of %s: ""' % (defwords, r.json())
    }]
  )

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

  app.run(port=port, host="0.0.0.0")

