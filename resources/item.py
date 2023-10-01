import uuid 
from flask import request 
from flask.views import MethodView
from flask_smorest import Blueprint, abort 
from db import items


blp = Blueprint("items", __name__, description="Operations on items")



@blp.route("/item/<string:item_id")
class Item(MethodView):
    def get(self, item_id):
        try: 
            return items[item_id], 200
        except:
            abort(404, message="Item not found")
    
    def delete(self, item_id):
        try:
            del items[item_id]
            return f"Item with id of {item_id} has been deleted", 200
        except:
            abort(404, message="Item not found")
            

@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"Items" : list(items.values())}, 200
    
    def post(self):
        item_data = request.get_json()
        if "price" not in item_data or "store_id" not in item_data or "name" not in item_data:
            abort(400, message="The item must include a name, store_id and price")
        for item in item.values()