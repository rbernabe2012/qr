from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

# Define the path for the CSV file
CSV_FILE = 'customers.csv'

@app.route('/')
def index():
    """Serves the main page with the form."""
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    """Handles form submission and saves data to a CSV file."""
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']

    # Check if the CSV file exists to write headers
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        # Write headers if the file is new
        if not file_exists:
            writer.writerow(['Name', 'Phone', 'Email'])
        # Write the customer data
        writer.writerow([name, phone, email])

    return "Thank you! Your data has been submitted."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
