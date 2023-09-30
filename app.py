from flask import Flask , jsonify , request


app = Flask(__name__)


stores = {}
items = {}


# Return a list of stores
@app.get("/store")
def get_stores():
    return {"stores": stores}, 200

# Create a new store with given name
@app.post("/store")
def create_store():
   request_data = request.get_json()
   new_store = {"name": request_data["name"], "items": []}
   stores.append(new_store)
   return new_store, 201




# Create a new item inside a store with given name
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404


#  Return a store with given name and its info (items)
@app.post("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items" : store["items"]}, 200
    return {"message": "Store not found"}, 404
