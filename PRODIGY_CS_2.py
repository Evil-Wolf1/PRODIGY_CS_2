from PIL import Image

def encrypt_image(image_path, encryption_key):
    try:
        # Open the image
        img = Image.open(image_path)
        pixels = img.load()
        width, height = img.size
        
        # Encrypt each pixel in the image
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # Example encryption: swap red and blue values
                r, b = b, r
                # Apply basic mathematical operation (addition) with encryption key
                r = (r + encryption_key) % 256
                g = (g + encryption_key) % 256
                b = (b + encryption_key) % 256
                pixels[x, y] = (r, g, b)
        
        # Save the encrypted image
        encrypted_image_path = image_path.split('.')[0] + '_encrypted.png'
        img.save(encrypted_image_path)
        print("Image encrypted successfully!")
        return encrypted_image_path
    except Exception as e:
        print("Error occurred while encrypting the image:", e)
        return None

def decrypt_image(encrypted_image_path, encryption_key):
    try:
        # Open the encrypted image
        img = Image.open(encrypted_image_path)
        pixels = img.load()
        width, height = img.size
        
        # Decrypt each pixel in the image
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # Apply the reverse of encryption operations
                r = (r - encryption_key) % 256
                g = (g - encryption_key) % 256
                b = (b - encryption_key) % 256
                # Example decryption: swap red and blue values back to original
                r, b = b, r
                pixels[x, y] = (r, g, b)
        
        # Save the decrypted image
        decrypted_image_path = encrypted_image_path.split('_encrypted')[0] + '_decrypted.png'
        img.save(decrypted_image_path)
        print("Image decrypted successfully!")
        return decrypted_image_path
    except Exception as e:
        print("Error occurred while decrypting the image:", e)
        return None

# Example Usage
image_path = 'example_image.png'  # Replace with the path to your image
encryption_key = 123  

# Encrypt the image
encrypted_image_path = encrypt_image(image_path, encryption_key)
if encrypted_image_path:
    print("Encrypted image saved as:", encrypted_image_path)

# Decrypt the image
decrypted_image_path = decrypt_image(encrypted_image_path, encryption_key)
if decrypted_image_path:
    print("Decrypted image saved as:", decrypted_image_path)
