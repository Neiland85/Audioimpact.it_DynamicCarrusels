# app.py
from flask import Flask, render_template
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
    msg = Message('Hello from Audiimpact.it',
                  recipients=['recipient@example.com'])
    msg.body = 'This is a test email sent from Audiimpact.it'
    mail.send(msg)
    return 'Email sent!'

if __name__ == '__main__':
    app.run(debug=True)

