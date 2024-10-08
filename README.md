# CO528-Contact-Management-System

This project is a simple RESTful API for storing and managing contact information. It provides a set of endpoints to perform basic CRUD (Create, Read, Update, Delete) operations on contact data.

## Features

- **List Contacts**: Retrieve a list of all contacts stored in the database.
- **Get Contact Details**: Retrieve detailed information about a specific contact by its unique ID.
- **Add New Contact**: Create a new contact with necessary details such as name, email, phone number, etc.
- **Update Contact**: Modify the details of an existing contact by providing its ID.
- **Delete Contact**: Remove a contact from the database by its ID.

## Endpoints

### 1. List All Contacts

- **Endpoint**: `GET /api/v1/contacts`
- **Description**: Fetches a list of all contacts stored in the database.
- **Response**: A JSON array of contact objects.

### 2. Get Contact Details

- **Endpoint**: `GET /api/v1/contacts/{id}`
- **Description**: Fetches detailed information about a specific contact.
- **Parameters**:
  - `id`: The unique identifier of the contact.
- **Response**: A JSON object containing the contact details.

### 3. Add a New Contact

- **Endpoint**: `POST /api/v1/contacts`
- **Description**: Creates a new contact with the provided information.
- **Request Body**: A JSON object containing contact details such as name, email, phone number, etc.
- **Response**: The created contact object with a unique ID.

### 4. Update Contact Information

- **Endpoint**: `PUT /api/v1/contacts/{id}`
- **Description**: Updates the information of an existing contact.
- **Parameters**:
  - `id`: The unique identifier of the contact.
- **Request Body**: A JSON object with the updated contact details.
- **Response**: The updated contact object.

### 5. Delete a Contact

- **Endpoint**: `DELETE /api/v1/contacts/{id}`
- **Description**: Deletes a contact from the database.
- **Parameters**:
  - `id`: The unique identifier of the contact.
- **Response**: A confirmation message or the deleted contact object.

