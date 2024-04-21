# Image Encryption Tool

This is a simple Python tool for encrypting and decrypting images using pixel manipulation techniques.

## Features

- Encrypt images by swapping pixel values and applying a basic mathematical operation.
- Decrypt encrypted images to recover the original image.
- Simple and easy-to-use command-line interface.

## Requirements

- Python 3.x
- Pillow library (`pip install Pillow`)

## Usage

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/image-encryption-tool.git
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Encrypt an image:

    ```
    python encrypt_image.py --image <image_path> --key <encryption_key>
    ```

4. Decrypt an encrypted image:

    ```
    python decrypt_image.py --image <encrypted_image_path> --key <encryption_key>
    ```

5. The encrypted/decrypted image will be saved in the same directory with the filename appended with `_encrypted` or `_decrypted`, respectively.

## Example

Encrypt an image named `example_image.png` with an encryption key `123`:

