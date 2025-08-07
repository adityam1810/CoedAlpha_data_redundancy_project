import csv
import os
from flask import Flask, request, jsonify

app = Flask(__name__)
DATA_FILE = "data.csv"

def initialize_csv():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'email'])
            writer.writeheader()

def is_duplicate(entry):
    with open(DATA_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['email'] == entry['email']:
                return True
    return False

def add_entry(entry):
    if not is_duplicate(entry):
        with open(DATA_FILE, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'email'])
            writer.writerow(entry)
        return True
    return False

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Missing name or email"}), 400

    success = add_entry({"name": name, "email": email})
    if success:
        return jsonify({"message": "Entry added successfully"}), 200
    else:
        return jsonify({"message": "Duplicate entry"}), 409

if __name__ == '__main__':
    initialize_csv()
    app.run(debug=True)
