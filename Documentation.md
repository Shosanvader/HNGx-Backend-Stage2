# API Documentation

## Overview
This API provides access to a database of `Person` objects. Each `Person` has a unique `id` and a `name`. The API allows for the creation, retrieval, update, and deletion of `Person` objects.

## Endpoints

### 1. List and Create Person: `GET / POST /`
- **GET**: Retrieves a list of all `Person` objects.
- **POST**: Creates a new `Person` object. Requires a JSON body with the following structure:
    ```json
    {
        "name": "<name>"
    }
    ```
    The `name` field must be unique, otherwise a validation error will be raised.

### 2. Retrieve, Update, and Delete Person: `GET / PUT / PATCH / DELETE /<str:pk>`
- **GET**: Retrieves the details of a `Person` object with the specified `id`.
- **PUT / PATCH**: Updates the details of a `Person` object with the specified `id`. Requires a JSON body with the following structure:
    ```json
    {
        "name": "<new_name>"
    }
    ```
    The `name` field must be unique, otherwise a validation error will be raised.
- **DELETE**: Deletes the `Person` object with the specified `id`.

## Errors
The API will return meaningful HTTP response codes along with clear error messages for easy debugging.

## Note
This API uses Django Rest Framework and requires appropriate authentication and permissions for all endpoints. Please refer to Django Rest Framework's documentation for more details on this.
### Deployment Instructions
1. Install Django and Django Rest Framework.
2. Clone the repository.
3. Navigate to the project directory and run the following command to start the server:
```bash
python manage.py runserver
```
4. The API will be accessible at `localhost:8000/api/`.

Please note that these instructions assume that you have Python and pip installed on your machine. If not, you will need to install those first. Also, you might need to apply migrations before running the server using this command:
```bash
python manage.py migrate
```
```