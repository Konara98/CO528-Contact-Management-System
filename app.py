from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

# Initialize Flask application
app = Flask(__name__)

# Configure the database URL from the environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

# Define the Contact model
class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    street = db.Column(db.String(120), nullable=True)
    city = db.Column(db.String(80), nullable=True)
    state = db.Column(db.String(80), nullable=True)
    zip_code = db.Column(db.String(20), nullable=True)

    def json(self):
        # Convert the Contact object to a JSON-friendly dictionary
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'address': {
                'street': self.street,
                'city': self.city,
                'state': self.state,
                'zip_code': self.zip_code
            }
        }

# Create database tables
db.create_all()

# Route to create a new contact
@app.route('/api/v1/contacts', methods=['POST'])
def create_contact():
    try:
        data = request.get_json()
        
        # Extract address fields from the nested address object
        address = data.get('address', {})
        
        new_contact = Contact(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            phone=data['phone'],
            street=address.get('street'),
            city=address.get('city'),
            state=address.get('state'),
            zip_code=address.get('zip_code')
        )
        # Add the new contact to the database
        db.session.add(new_contact)
        db.session.commit()
        return make_response(jsonify({'message': 'Contact created successfully', 'contact': new_contact.json()}), 201)
    except Exception as e:
        # Handle errors and return a response
        return make_response(jsonify({'message': f'Error creating contact: {str(e)}'}), 500)

# Route to get all contacts
@app.route('/api/v1/contacts', methods=['GET'])
def get_contacts():
    try:
        contacts = Contact.query.all()  # Query all contacts from the database
        return make_response(jsonify([contact.json() for contact in contacts]), 200)
    except Exception as e:
        # Handle errors and return a response
        return make_response(jsonify({'message': f'Error getting contacts: {str(e)}'}), 500)

# Route to get a specific contact by ID
@app.route('/api/v1/contacts/<int:id>', methods=['GET'])
def get_contact(id):
    try:
        contact = Contact.query.filter_by(id=id).first()  # Find the contact by ID
        if contact:
            return make_response(jsonify({'contact': contact.json()}), 200)
        return make_response(jsonify({'message': 'Contact not found'}), 404)
    except Exception as e:
        # Handle errors and return a response
        return make_response(jsonify({'message': f'Error getting contact: {str(e)}'}), 500)

# Route to update a contact
@app.route('/api/v1/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    try:
        contact = Contact.query.filter_by(id=id).first()  # Find the contact by ID
        if contact:
            data = request.get_json()
            # Update contact fields with data from the request, if provided
            contact.first_name = data.get('first_name', contact.first_name)
            contact.last_name = data.get('last_name', contact.last_name)
            contact.email = data.get('email', contact.email)
            contact.phone = data.get('phone', contact.phone)
            contact.street = data.get('street', contact.street)
            contact.city = data.get('city', contact.city)
            contact.state = data.get('state', contact.state)
            contact.zip_code = data.get('zip_code', contact.zip_code)
            db.session.commit()  # Commit the changes to the database
            return make_response(jsonify({'message': 'Contact updated successfully', 'contact': contact.json()}), 200)
        return make_response(jsonify({'message': 'Contact not found'}), 404)
    except Exception as e:
        # Handle errors and return a response
        return make_response(jsonify({'message': f'Error updating contact: {str(e)}'}), 500)

# Route to delete a contact
@app.route('/api/v1/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    try:
        contact = Contact.query.filter_by(id=id).first()  # Find the contact by ID
        if contact:
            db.session.delete(contact)  # Remove the contact from the database
            db.session.commit()
            return make_response(jsonify({'message': 'Contact deleted successfully'}), 200)
        return make_response(jsonify({'message': 'Contact not found'}), 404)
    except Exception as e:
        # Handle errors and return a response
        return make_response(jsonify({'message': f'Error deleting contact: {str(e)}'}), 500)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
