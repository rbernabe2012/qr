import qrcode

# Data to be encoded
data = "http://localhost:5000"

# Generate QR code
img = qrcode.make(data)

# Save the image
img.save("qr_code.png")

print("QR code generated and saved as qr_code.png")
