# Simple REST API

This is a simple REST API capable of CRUD operations on a "person" resource. The language used in its development is Python. The framework is Django REST framework. The database used in production is PostgreSQL.

## Set Up
1. Clone this repository to your local machine by running the following command in your terminal; `git clone hhttps://github.com/Shosanvader/HNGx-Backend-Stage2`
2. Go to the directory by running `cd HNGx-Backend-Stage2`
3. Install the required packages by running `pip install -r requirements.txt`

**Make sure you do everything in a virtual environment.**

## Using the Application
1. To (C)reate a new "person" send a POST request to the `/api` endpoint.
2. To (R)ead, (U)pdate or (D)elete a "person" resource, send a GET, PUT(or PATCH) or DELETE request to the `/api/{user_id}` endpoint.