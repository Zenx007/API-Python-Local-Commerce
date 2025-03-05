from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI()

class Product(BaseModel):
    item: str
    price: float
    amount: int

products: Dict[int, Product] = {
    1: Product(item="milk", price=3.0, amount=5),
    2: Product(item="bread", price=2.0, amount=5),
    3: Product(item="eggs", price=3.0, amount=5),
    4: Product(item="apples", price=1.0, amount=5),
    5: Product(item="rice", price=1.0, amount=5),
}

@app.get("/")
def home():
    return {"total_products": len(products)}

@app.get("/products/{product_id}", response_model=Product)
def view_product(product_id: int):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    return products[product_id]

@app.post("/products/", response_model=Product)
def create_product(product: Product):
    new_id = max(products.keys()) + 1 if products else 1
    products[new_id] = product
    return product

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: Product):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    products[product_id] = product
    return product

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    del products[product_id]
    return {"message": "Product deleted successfully"}