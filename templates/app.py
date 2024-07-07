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
    user_email = request.form['email']
    # Implement logic to handle user data request
    return jsonify({'message': 'Data request received for {}'.format(user_email)})

if __name__ == '__main__':
    app.run(debug=True)

