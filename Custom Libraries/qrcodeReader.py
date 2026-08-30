from PIL import Image
from pyzbar.pyzbar import decode

def read_qr_zbar(image_path):
    # Load the image
    img = Image.open(image_path)
    
    # Decode the QR code
    decoded_objects = decode(img)
    
    if not decoded_objects:
        print("No QR code found.")
        return None
        
    for obj in decoded_objects:
        # Data is returned as bytes, decode it to string
        qr_data = obj.data.decode("utf-8")
        print(f"Type: {obj.type}")
        print(f"Data: {qr_data}")
        return qr_data

# Run the function
read_qr_zbar("qrcode.png")
