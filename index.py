from flask import Flask, request, jsonify
import mysql.connector  


app = Flask(__name__)


DB_CONF_ID = {
    'host': 'localhost',
    'user': 'root',
    'password': 'ramram',
    'database': 'empdb'
}


def get_db_connection():
    return mysql.connector.connect(**DB_CONF_ID)


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Subscription Management API!"})


@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Users (user_id, user_name, email, status) VALUES (%s, %s, %s, %s)",
            (data['user_id'], data['user_name'], data['email'], data.get('status', 'Active'))
        )
        conn.commit()
        return jsonify({"message": "User added successfully!"}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

# Retrieve subscriptions for a specific user
@app.route('/subscriptions/<int:user_id>', methods=['GET'])
def get_user_subscriptions(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Subscriptions WHERE user_id = %s", (user_id,))
    subscriptions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(subscriptions)

# Add a payment
@app.route('/payments', methods=['POST'])
def add_payment():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Payments (payment_id, user_id, amount, payment_date) VALUES (%s, %s, %s, %s)",
            (data['payment_id'], data['user_id'], data['amount'], data['payment_date'])
        )
        conn.commit()
        return jsonify({"message": "Payment added successfully!"}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

# Calculate discount for a user
@app.route('/users/<int:user_id>/discount', methods=['GET'])
def calculate_discount(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT calculate_discount(%s) AS discount", (user_id,))
        discount = cursor.fetchone()[0]
        return jsonify({"user_id": user_id, "discount": discount})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

# Retrieve all payments
@app.route('/payments', methods=['GET'])
def get_payments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Payments")
    payments = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(payments)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

