# app.py
from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)

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

    # Implement logic to handle user data request or deletion
    if request_type == 'request_data':
        # Logic to retrieve user data
        response_message = f'Data request received for {user_email}. We will process it and get back to you soon.'
    elif request_type == 'delete_data':
        # Logic to delete user data
        response_message = f'Deletion request received for {user_email}. We will process it and delete your data.'

    return jsonify({'message': response_message})

if __name__ == '__main__':
    app.run(debug=True)

