# QR Code Customer Data Form

This project provides a simple web application to collect customer data (name, phone, and email) using a form and a QR code that links to it. The backend is built with Flask and saves the data to a `customers.csv` file.

## How to Use

### Prerequisites
- Python 3
- pip

### 1. Installation
First, install the necessary Python libraries. Navigate to the project directory in your terminal and run:

```bash
pip install Flask "qrcode[pil]"
```

### 2. Run the Application
To start the web application, run the following command from the project directory:

```bash
python3 app.py
```

This will start a Flask development server, typically accessible at `http://127.0.0.1:5000`. To allow other devices on your network to access it, you should use your computer's local IP address (e.g., `http://192.168.1.10:5000`).

### 3. Use the QR Code
The included `qr_code.png` is configured to work with the default server address (`http://localhost:5000`). You can print it or display it for your customers.

If you need to link the QR code to a different address (like a public URL if you deploy the application), you can regenerate it. Open the `generate_qr.py` file and change the `data` variable to your new URL:
```python
# Data to be encoded
data = "http://your-new-url.com"
```

Then, run the script to create a new `qr_code.png`:
```bash
python3 generate_qr.py
```
