 app.py
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

# app.py 
@app.route('/sync-prestashop-products')
def sync_prestashop_products():
    products = prestashop.get('products')
    for product in products['products']['product']:
        # Assuming product has 'name' and 'price' fields
        product_data = prestashop.get(f'products/{product["id"]}')
        new_item = CarouselItem(
            image_url=f'static/images/{product_data["product"]["id"]}.jpg',  # Placeholder for actual image URL
            alt_text=product_data['product']['name'],
            title=product_data['product']['name'],
            description=f'Price: {product_data["product"]["price"]}'
        )
        db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Products synchronized with PrestaShop'}), 200

