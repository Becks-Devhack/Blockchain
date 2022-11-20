import requests

# curl -H "Content-type:application/json" --data '{"data" : "Some data to the first block"}' http://localhost:3001/mineBlock

x = requests.post("http://localhost:3001/mineBlock", 
                  json={"data" : "Anghel e smecher!"},
                  )
print(x.text)

x = requests.get("http://localhost:3001/blocks")
print(x.text)
