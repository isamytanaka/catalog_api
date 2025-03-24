## Catalog API
![](api-svgrepo-com.svg)
> This API allows you to manage a product catalog with the following operations:

**Add a product**: Add a new product to the catalog.

**Get all products**: Retrieve a list of all products.

**Get a specific product**: Retrieve details of a specific product by its ID.

**Update a product**: Update details of an existing product by its ID.

**Delete a product**: Remove a product from the catalog by its ID.


## Available Endpoints:

1. `POST /products/`: Add a new product.


2. `GET /products/`: List all products.


3. `GET /products/{product_id}`: Get a product by ID.


4. `PUT /products/{product_id}`: Update a product by ID.


5. `DELETE /products/{product_id}`: Delete a product by ID.



Each product includes the following fields: ``name``, ``description``, ``price``, ``category``, and ``stock``.
