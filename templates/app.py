# app.py
from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)

carousel_items = [
    {"image_url": "static/images/image1.jpg", "alt_text": "First Slide"},
    {"image_url": "static/images/image2.jpg", "alt_text": "Second Slide"},
    {"image_url": "static/images/image3.jpg", "alt_text": "Third Slide"},
]

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
    return jsonify(carousel_items)

@app.route('/api/carousel-items', methods=['POST'])
def add_carousel_item():
    new_item = request.json
    carousel_items.append(new_item)
    return jsonify({'message': 'Carousel item added successfully'}), 201

@app.route('/api/carousel-items/<int:index>', methods=['DELETE'])
def delete_carousel_item(index):
    if 0 <= index < len(carousel_items):
        carousel_items.pop(index)
        return jsonify({'message': 'Carousel item deleted successfully'}), 200
    return jsonify({'message': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(ssl_context=('certificate.crt', 'private.key'), debug=True)
