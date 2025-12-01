from flask import Flask, render_template, request, url_for
from flask_mail import Mail, Message
import csv
import os

BASE_PATH = "/axisbrokers"

app = Flask(__name__, static_url_path=f"{BASE_PATH}/static")

# --- Flask-Mail Configuration for SendGrid ---
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = os.environ.get("SENDGRID_KEY")
app.config['MAIL_DEFAULT_SENDER'] = 'rbernabe@sempitecno.com'

mail = Mail(app)

# CSV path
CSV_FILE = 'customers.csv'
RECIPIENT_EMAIL = 'gabriela.axisbrokers@gmail.com'


@app.route(f"{BASE_PATH}/")
def index():
    return render_template("index.html")


@app.route(f"{BASE_PATH}/submit", methods=['POST'])
def submit():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    consent = request.form.get('consent')  # Returns 'on' if checked, None otherwise

    # Save to CSV
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Name', 'Phone', 'Email', 'Consentimiento_Datos'])
        # Store a more readable value
        consent_status = "Aceptado" if consent == "on" else "No Aceptado"
        writer.writerow([name, phone, email, consent_status])
 # Send email
    try:
        msg = Message(
            subject="Nuevo Contacto de Cliente",
            recipients=[RECIPIENT_EMAIL],
            body=f"Has recibido un nuevo contacto:\n\nNombre: {name}\nTeléfono: {phone}\nCorreo: {email}"
        )
        mail.send(msg)
    except Exception as e:
        app.logger.error(f"Error sending email: {e}")
        return "¡Gracias! Tus datos han sido enviados, pero hubo un problema al enviar la notificación."

    return "¡Gracias! Tus datos han sido enviados."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
