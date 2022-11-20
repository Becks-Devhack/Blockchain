from flask import request, jsonify, Response, Flask
import requests
import json

app = Flask(__name__)
miner_endpoint = "http://localhost:3001"

@app.route("/all_vacantions", methods=["GET"])
def get_all_vacantions():
    global miner_endpoint
    x = requests.get("{}/{}".format(miner_endpoint, "blocks"))
    
    print(x.text)
    
    vacantions = []
    
    for block in json.loads(x.text)[1:]:
        vacantions.append(block.get("data", None))
        
    return vacantions, 200


@app.route("/new_vacantion", methods=["POST"])
def post_new_vacantion():
    global miner_endpoint
    payload = request.get_json(silent=True)
    print(payload)
    if not payload:
        # Error handling
        return Response(status=400)
    x = requests.post("{}/{}".format(miner_endpoint, "mineBlock"), 
                  json={"data" : payload},
                  )
    if x is None:
        return Response(status=404)
    print(x.text)
    
    return Response(status=201)    

if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
