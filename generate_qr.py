import qrcode
import sys

def generate_qr_code(hostname="localhost"):
    """
    Generates a QR code pointing to the specified hostname.
    Usage: python3 generate_qr.py [hostname_or_ip]
    """
    # Construct the URL
    data = f"http://{hostname}:5000"

    # Generate QR code
    img = qrcode.make(data)

    # Save the image
    img.save("qr_code.png")

    print(f"QR code generated for {data} and saved as qr_code.png")

if __name__ == "__main__":
    # Use the command-line argument if provided, otherwise default to "localhost"
    if len(sys.argv) > 1:
        hostname_arg = sys.argv[1]
        generate_qr_code(hostname_arg)
    else:
        generate_qr_code()
