# E-commerce_API

This E-Commerce API is a Flask-based application designed to manage an online store's core functionalities including customer management, order processing, and product inventory. It provides a robust backend setup, complete with an API that supports various operations crucial for e-commerce platforms.

Features
Customer Management
Create, Read, Update, and Delete (CRUD) Operations: Manage customer details including name, email, and phone number.
Customer Authentication: Handle customer accounts with unique usernames and passwords.
Order Processing
Order Placement: Allows customers to place orders, specifying details such as order date and the products purchased.
Order Tracking: Retrieve and manage orders by customer or individual order IDs.
Product Management
Product Inventory: Add, update, or delete products from the inventory. Manage details such as product name, price, and stock levels.
Product Queries: Fetch all products or get details of a specific product by ID.
Technical Specifications
Framework: Built with Flask, a lightweight WSGI web application framework.
Database: Uses MySQL with SQLAlchemy as the ORM layer for database operations.
Data Validation: Incorporates Marshmallow for request data validation, ensuring robust data handling.
API Documentation: Detailed API routes are provided for managing resources, suitable for integration with frontend platforms or third-party applications.
