# app.py
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-password'

mail = Mail(app)

@app.route('/send-email')
def send_email():
    msg = Message('Hello from Audiimpact.it',
                  sender='your-email@example.com',
                  recipients=['recipient@example.com'])
    msg.body = 'This is a test email sent from a Flask web application!'
    mail.send(msg)
    return 'Email sent!'

if __name__ == '__main__':
    app.run(debug=True)
