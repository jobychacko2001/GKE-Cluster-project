from flask import Blueprint, request, jsonify, send_from_directory
from db import get_db_connection
import os

main = Blueprint('main', __name__)




@main.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')


@main.route('/styles.css')
def styles():
    return send_from_directory('../frontend', 'styles.css')


@main.route('/script.js')
def script():
    return send_from_directory('../frontend', 'script.js')


@main.route('/submit', methods=['POST'])
def submit():
    # Extract data from request body (JSON)
    data = request.json
    name = data.get('name')
    email = data.get('email')

    # Ensure name and email are provided
    if not name or not email:
        return jsonify({'error': 'Missing name or email'}), 400

    try:
        # Connect to the database and insert the data
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        cursor.close()
        conn.close()

        # Return success response
        return jsonify({'message': 'Data received and inserted successfully'}), 200
    except Exception as e:
        # Handle any errors
        return jsonify({'error': str(e)}), 500
