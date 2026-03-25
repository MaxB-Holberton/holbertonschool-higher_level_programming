from flask import Flask, render_template, jsonify, request
import json
import csv
import os

app = Flask(__name__)

def render_json():
    with open('products.json') as f:
        return json.load(f)


def render_csv():
    products = []
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row['id']),
                "name": row['name'],
                "category": row['category'],
                "price": float(row['price'])
            })
    return products


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json') as f:
        data = json.load(f)
        items = data.get('items', [])
        return render_template('items.html', items=items)

@app.route('/products')
def products():
    get_source = request.args.get('source')
    get_id = request.args.get('id')

    if get_source != 'json' and get_source != 'csv':
         return render_template('product_display.html', error="Wrong source")

    if get_source == 'json':
        products=render_json()
    elif get_source == 'csv':
        products=render_csv()

    if get_id is None:
        return render_template('product_display.html', products=products)
    else:
        sorted_products = []
        for item in products:
            if str(item['id']) == str(get_id):
                sorted_products.append(item)

        products = sorted_products
    if len(products) == 0:
         return render_template('product_display.html', error="Product not found")
    else:
        return render_template('product_display.html', products=products)

    return render_template('product_display.html', error="500 - unknown error")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
