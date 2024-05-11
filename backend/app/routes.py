from flask import Blueprint, jsonify, request
from .db import get_db_connection
api_bp = Blueprint('api', __name__)

@api_bp.route('/post-data', methods=['POST'])
def post_data():
    try:
        # Extract data from request
        data = request.get_json()

        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert data into database
        cursor.execute("INSERT INTO students (name) VALUES (%s)", (data['name'],))
        conn.commit()

        # Close database connection
        cursor.close()
        conn.close()

        return jsonify({"message": "Data posted successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@api_bp.route('/get-data', methods=['GET'])
def get_data():
    try:
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Fetch data from database
        cursor.execute("SELECT * FROM students ORDER BY id")
        data = cursor.fetchall()

        # Close database connection
        cursor.close()
        conn.close()

        # Convert data to a list of dictionaries
        data_list = [{'id': row[0], 'name': row[1]} for row in data]

        return jsonify(data_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route('/update-data/<int:id>', methods=['PUT'])
def update_data(id):
    try:
        # Extract data from request
        data = request.get_json()

        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Update data in the database
        cursor.execute("UPDATE students SET name = %s WHERE id = %s", (data['name'], id))
        conn.commit()

        # Close database connection
        cursor.close()
        conn.close()

        return jsonify({"message": "Data updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route('/delete-data/<int:id>', methods=['DELETE'])
def delete_data(id):
    try:
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()
        # Delete data from the database
        cursor.execute("DELETE FROM students WHERE id = %s", (id,))
        conn.commit()

        # Close database connection
        cursor.close()
        conn.close()

        return jsonify({"message": "Data deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500