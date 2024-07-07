# app.py
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from config import Config
from prestapyt import PrestaShopWebServiceDict

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
mail = Mail(app)

# Define the CarouselItem model
class CarouselItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)
    alt_text = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'image_url': self.image_url,
            'alt_text': self.alt_text,
            'title': self.title,
            'description': self.description
        }

# Define the Contact model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)

# Routes and API endpoints
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email')
def send_email():
    user = {'name': 'John Doe', 'email': 'recipient@example.com'}
    msg = Message('Welcome to Audiimpact.it',
                  recipients=[user['email']])
    msg.html = render_template('emails/welcome.html', user=user)
    mail.send(msg)
    return 'Email sent!'

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@app.route('/data-request', methods=['POST'])
def data_request():
    request_data = request.json
    user_email = request_data.get('email')
    request_type = request_data.get('request_type')

    if request_type == 'request_data':
        response_message = f'Data request received for {user_email}. We will process it and get back to you soon.'
    elif request_type == 'delete_data':
        response_message = f'Deletion request received for {user_email}. We will process it and delete your data.'

    return jsonify({'message': response_message})

@app.route('/manage-carousels')
def manage_carousels():
    return render_template('manage_carousels.html')

@app.route('/api/carousel-items', methods=['GET'])
def get_carousel_items():
    items = CarouselItem.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/api/carousel-items', methods=['POST'])
def add_carousel_item():
    data = request.json
    new_item = CarouselItem(
        image_url=data['image_url'],
        alt_text=data['alt_text'],
        title=data.get('title'),
        description=data.get('description')
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Carousel item added successfully'}), 201

@app.route('/api/carousel-items/<int:id>', methods=['DELETE'])
def delete_carousel_item(id):
    item = CarouselItem.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Carousel item deleted successfully'}), 200

@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([{'id': c.id, 'email': c.email, 'name': c.name} for c in contacts])

@app.route('/api/contacts', methods=['POST'])
def add_contact():
    data = request.json
    new_contact = Contact(email=data['email'], name=data['name'])
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({'message': 'Contact added successfully'}), 201

# Configure PrestaShop API
PRESTASHOP_API_URL = 'http://your-prestashop-site/api'
PRESTASHOP_API_KEY = 'your-prestashop-api-key'
prestashop = PrestaShopWebServiceDict(PRESTASHOP_API_URL, PRESTASHOP_API_KEY)

@app.route('/sync-prestashop-contacts')
def sync_prestashop_contacts():
    resources = prestashop.get('customers')
    for resource in resources['customers']['customer']:
        contact = Contact.query.filter_by(email=resource['email']).first()
        if not contact:
            new_contact = Contact(
                email=resource['email'],
                name=resource['firstname'] + ' ' + resource['lastname']
            )
            db.session.add(new_contact)
    db.session.commit()
    return jsonify({'message': 'Contacts synchronized with PrestaShop'}), 200

@app.route('/send-carousel-update-email', methods=['POST'])
def send_carousel_update_email():
    contacts = Contact.query.all()
    for contact in contacts:
        msg = Message('New Carousel Update at Audiimpact.it',
                      recipients=[contact.email])
        msg.body = f'Hello {contact.name}, check out our new carousel updates on the website!'
        mail.send(msg)
    return jsonify({'message': 'Emails sent successfully'}), 200

if __name__ == '__main__':
    app.run(ssl_context=('certificate.crt', 'private.key'), debug=True)

