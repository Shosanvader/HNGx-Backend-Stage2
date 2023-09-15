# API Documentation

## Overview
This API provides a simple interface for managing `Person` objects. The API is built using Django and Django Rest Framework.

## Endpoints
The API has the following endpoint:

- `/api/`: This endpoint provides access to the `Person` objects.

### Standard Formats for Requests and Responses

#### GET `/api/`
This endpoint returns a list of all `Person` objects.

- **Request Format:** No body required.
- **Response Format:** A list of `Person` objects. Each object contains an `id` and a `name`.

#### POST `/api/`
This endpoint creates a new `Person` object.

- **Request Format:** A JSON object containing a `name`.
- **Response Format:** The created `Person` object.

#### GET `/api/{id}/`
This endpoint returns a specific `Person` object.

- **Request Format:** No body required.
- **Response Format:** The requested `Person` object.

#### PUT `/api/{id}/`
This endpoint updates a specific `Person` object.

- **Request Format:** A JSON object containing the updated `name`.
- **Response Format:** The updated `Person` object.

#### DELETE `/api/{id}/`
This endpoint deletes a specific `Person` object.

- **Request Format:** No body required.
- **Response Format:** No body returned.

### Sample Usage

#### GET `/api/`
**Request:**
```http
GET /api/
```
**Response:**
```json
[
    {
        "id": 1,
        "name": "John Doe"
    },
    {
        "id": 2,
        "name": "Jane Doe"
    }
]
```

### Known Limitations
The current implementation only supports one field (`name`) for the `Person` model. If more fields are needed, they will need to be added to the model and serializer.

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