from flask import Flask, request, jsonify, abort

app = Flask(__name__)

products_db = {}

class Product:
    def __init__(self, name, description, price, category, stock):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock = stock

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category,
            "stock": self.stock
        }

@app.route("/products/", methods=["POST"])
def add_product():
    data = request.get_json()
    if not data:
        abort(400, description="Invalid input")
    
    product_id = str(len(products_db) + 1)
    product = Product(
        data["name"], 
        data["description"], 
        data["price"], 
        data["category"], 
        data["stock"]
    )
    products_db[product_id] = product
    return jsonify({"id": product_id, "product": product.to_dict()}), 201

@app.route("/products/", methods=["GET"])
def list_products():
    return jsonify([product.to_dict() for product in products_db.values()])

@app.route("/products/<product_id>", methods=["GET"])
def get_product(product_id):
    product = products_db.get(product_id)
    if not product:
        abort(404, description="Product not found")
    return jsonify(product.to_dict())

@app.route("/products/<product_id>", methods=["PUT"])
def update_product(product_id):
    product = products_db.get(product_id)
    if not product:
        abort(404, description="Product not found")
    
    data = request.get_json()
    product.name = data.get("name", product.name)
    product.description = data.get("description", product.description)
    product.price = data.get("price", product.price)
    product.category = data.get("category", product.category)
    product.stock = data.get("stock", product.stock)
    
    return jsonify(product.to_dict())

@app.route("/products/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = products_db.get(product_id)
    if not product:
        abort(404, description="Product not found")
    
    del products_db[product_id]
    return jsonify({"msg": "Product deleted successfully"}), 204

if __name__ == "__main__":
    app.run(debug=True)