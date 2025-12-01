import qrcode

def generate_qr_code():
    """
    Generates a QR code pointing to the public Axis Brokers form.
    """
    # URL correcta de producción detrás de Nginx
    data = "https://erp.open-revolution.com/axisbrokers"

    # Generate QR code
    img = qrcode.make(data)

    # Save the image
    img.save("qr_code.png")

    print(f"QR code generated for {data} and saved as qr_code.png")

if __name__ == "__main__":
    generate_qr_code()
