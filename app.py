from flask import Flask, jsonify, request
from flask_smorest import abort
from db import stores, items
import uuid

app = Flask(__name__)


# Return a list of stores
@app.get("/store")
def get_stores():
    return {"stores": list(stores.values)}, 200


# Create a new store with given name
@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400, message="Store must include name")
    for store in stores.values():
        if store["name"] == store_data["name"]:
            abort(400, message="Store with that name already exists")
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store, 201


# Create a new item inside a store with given name
@app.post("/item")
def create_item():
    item_data = request.get_json()
    if (
        "name" not in item_data
        or "price" not in item_data
        or "store_id" not in item_data
    ):
        abort(400, message="Item must include name, price and store_id")
    for item in items.values():
        if (
            item["name"] == item_data["name"]
            and item["store_id"] == item_data["store_id"]
        ):
            abort(400, message="Item with that name already exists")
    if item_data["store_id"] not in stores:
        abort(404, message="Store not found")

    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return item, 201


# Get an item
@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id], 200
    except:
        abort(404, message="Item not found")


# Get all items
@app.get("/items")
def get_all_items():
    return {"items": list(items.values())}, 200


# Delete an item
@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    if item_id not in items:
        abort(404, message="Item not found")
    del items[item_id]
    return f"Item with id {item_id} has been deleted", 200


# #  Return a store with its given name
# @app.("/store/<string:store_id>")
# def get_store(store_id):
#     try:
#         return stores[store_id], 200
#     except:
#         abort(404, message="Store not found")
