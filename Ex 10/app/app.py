from flask import Flask, jsonify
import psycopg2

 #Flask application code to be executed in the web service
app = Flask(__name__)   

db_config = {
    'dbname': 'frog_database',
    'user': 'admin_frog',
    'password': 'hoppy_boi',
    'host': 'db',
    'port': '5432'
}

# Flask route to fetch test data
@app.route('/') 
def get_frogs():
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Fetching a couple of rows from the Frogs table
    cursor.execute("SELECT * FROM Frogs LIMIT 2;")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)