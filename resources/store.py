import uuid
from flask import request
from flask.views import MethodView
from flask_smorest  import Blueprint, abort
from db import stores 



blp = Blueprint( "stores", __name__, description="Operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id], 200
        except:
            abort(404, message="Store not found")
    
    def delete(self, store_id):
        try:
            del stores[store_id]
            return f"Store with id {store_id} has been deleted", 200
        except:
            abort(404, message="Store not found")
            
            
@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}, 200
    
    def post(self):
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
    
    def put(self, store_id):
        store_data = request.get_json()
        if "name" not in store_data:
            abort(400, message="Store must include name")
        try:
            store = stores[store_id]
            store |= store_data
            return store, 200
        except KeyError:
            abort(404, message="Store not found")
        