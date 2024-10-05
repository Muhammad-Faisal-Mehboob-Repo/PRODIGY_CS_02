# Image Encryption and Decryption using Pixel Manipulation

This repository contains a simple Python program that allows you to **encrypt** and **decrypt** images using a basic pixel manipulation technique. The program shifts the pixel values by a user-specified key, effectively scrambling the image for encryption and reversing the process for decryption.

## Features

- **Encrypt an image:** Shifts the RGB values of every pixel in the image by a key value.
- **Decrypt an image:** Reverses the pixel shifts using the same key to restore the original image.
- Easy to use with a command-line interface.

## How it Works

The core idea of this program is to shift the pixel values of the image using a numeric key. During encryption, the pixel values are increased by the key, and during decryption, they are decreased by the key. The pixel values are wrapped within the range of 0-255 to ensure valid RGB values.

### Main Functions:

- **shift_pixels:** Takes the image as a NumPy array and shifts each pixel's RGB values by the key for encryption or decryption.
- **encrypt_image:** Encrypts the image using the provided key and saves the result.
- **decrypt_image:** Decrypts the image using the provided key and saves the result.

## How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/image-encryption.git
   cd image-encryption
   ```

2. **Install the dependencies:**
   This script relies on the `Pillow` and `numpy` libraries. You can install them via pip:
   ```bash
   pip install Pillow numpy
   ```

3. **Run the program:**
   ```bash
   python image_encryption.py
   ```

4. **Follow the prompts:**
   - You'll be asked if you want to encrypt or decrypt an image.
   - Provide the image file path, the encryption/decryption key (a non-negative integer), and the output file path to save the processed image.

## Example

### Encrypt an Image:
```
If you want to encrypt the image press 'y' or press 'n' to decrypt the image: y
Enter the path of the image: path/to/your/image.png
Enter the encryption/decryption key (integer value): 42
Enter the path to save the output image: path/to/save/encrypted_image.png
```
After running, the encrypted image will be saved to the specified location.

### Decrypt an Image:
```
If you want to encrypt the image press 'y' or press 'n' to decrypt the image: n
Enter the path of the image: path/to/your/encrypted_image.png
Enter the encryption/decryption key (integer value): 42
Enter the path to save the output image: path/to/save/decrypted_image.png
```
The original image will be restored using the same key.

## Note

Make sure to remember the encryption key! The same key is required to decrypt the image and restore it to its original form. Using an incorrect key will result in a scrambled image.

## License

This project is licensed under the MIT License. Feel free to use and modify it!

---

Feel free to fork this project, suggest improvements, or reach out if you have any questions!
