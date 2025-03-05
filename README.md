# FastAPI Product Management API

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

A FastAPI-based API for managing a product catalog. This API supports CRUD operations (Create, Read, Update, Delete) for products, using a Pydantic model for data validation and structure.

---

## 📋 Code Description

The project is built using **FastAPI** and **Pydantic**. It includes the following features:

### Product Model
The `Product` Pydantic model defines the structure of a product:
- `item`: Name of the product (string).
- `price`: Price of the product (float).
- `amount`: Quantity of the product in stock (integer).

### In-Memory Database
Products are stored in a Python dictionary (`products`), where the keys are product IDs and the values are `Product` objects.

### Endpoints
1. **`GET /`**:
   - Returns the total number of products.
   - Example response:
     ```json
     {
       "total_products": 5
     }
     ```

2. **`GET /products/{product_id}`**:
   - Returns the details of a specific product by its ID.
   - If the product ID does not exist, it returns a `404 Not Found` error.
   - Example response:
     ```json
     {
       "item": "milk",
       "price": 3.0,
       "amount": 5
     }
     ```

3. **`POST /products/`**:
   - Adds a new product to the database.
   - Requires a JSON body with the product details.
   - Example request body:
     ```json
     {
       "item": "chocolate",
       "price": 2.5,
       "amount": 10
     }
     ```
   - Example response:
     ```json
     {
       "item": "chocolate",
       "price": 2.5,
       "amount": 10
     }
     ```

4. **`PUT /products/{product_id}`**:
   - Updates an existing product by its ID.
   - Requires a JSON body with the updated product details.
   - If the product ID does not exist, it returns a `404 Not Found` error.
   - Example request body:
     ```json
     {
       "item": "milk",
       "price": 3.5,
       "amount": 8
     }
     ```
   - Example response:
     ```json
     {
       "item": "milk",
       "price": 3.5,
       "amount": 8
     }
     ```

5. **`DELETE /products/{product_id}`**:
   - Deletes a product by its ID.
   - If the product ID does not exist, it returns a `404 Not Found` error.
   - Example response:
     ```json
     {
       "message": "Product deleted successfully"
     }
     ```

---

## 🚀 How to Run the Project

1. **Install FastAPI** and **Uvicorn**:
   ```bash
   pip install fastapi uvicorn
