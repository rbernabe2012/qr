from flask import Flask, render_template, request
from flask_mail import Mail, Message
import csv
import os

app = Flask(__name__)

# --- Flask-Mail Configuration ---
# For security, these values are loaded from environment variables.
# Ensure you set EMAIL_USER and EMAIL_PASS in your environment.
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('EMAIL_USER')

mail = Mail(app)
# -----------------------------

# Define the path for the CSV file
CSV_FILE = 'customers.csv'
RECIPIENT_EMAIL = 'gabriela.axisbrokers@gmail.com'

@app.route('/')
def index():
    """Serves the main page with the form."""
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    """
    Handles form submission by saving data to a CSV file
    and sending an email notification.
    """
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']

    # --- Save data to CSV file ---
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Name', 'Phone', 'Email'])
        writer.writerow([name, phone, email])
    # -----------------------------

    # --- Send email notification ---
    try:
        msg = Message(
            subject="Nuevo Contacto de Cliente",
            recipients=[RECIPIENT_EMAIL],
            body=f"Has recibido un nuevo contacto:\n\nNombre: {name}\nTeléfono: {phone}\nCorreo: {email}"
        )
        mail.send(msg)
    except Exception as e:
        # Log the error and continue without crashing
        app.logger.error(f"Error sending email: {e}")
        return "¡Gracias! Tus datos han sido enviados, pero encontramos un problema al enviar el correo de notificación."
    # -----------------------------

    return "¡Gracias! Tus datos han sido enviados."

if __name__ == '__main__':
    # For production, consider using a proper WSGI server instead of the dev server.
    app.run(debug=True, host='0.0.0.0', port=5000)
