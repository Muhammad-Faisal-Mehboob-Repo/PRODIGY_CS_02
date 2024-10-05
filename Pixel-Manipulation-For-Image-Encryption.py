from PIL import Image
import numpy as np

def shift_pixels(image_array, key, encrypt=True):
    shifted_array = np.copy(image_array)
    if encrypt:
        shifted_array = (shifted_array + key) % 256
    else:
        shifted_array = (shifted_array - key) % 256

    return shifted_array.astype(np.uint8)

def encrypt_image(image_path, key, output_path):
    image = Image.open(image_path).convert("RGB")
    image_array = np.array(image)
    encrypted_image_array = shift_pixels(image_array, key, encrypt=True)
    encrypted_image = Image.fromarray(encrypted_image_array)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as: {output_path}")

def decrypt_image(image_path, key, output_path):
    image = Image.open(image_path).convert("RGB")
    image_array = np.array(image)
    decrypted_image_array = shift_pixels(image_array, key, encrypt=False)
    decrypted_image = Image.fromarray(decrypted_image_array)
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as: {output_path}")

if __name__ == "__main__":
    choice = input("If you want to encrypt the image press 'y' or press 'n' to decrypt the image: ").lower()
    image_path = input("Enter the path of the image: ")
    while True:
        try:
            key = int(input("Enter the encryption/decryption key (integer value): "))
            if key < 0:
                raise ValueError("Key must be a non-negative integer.")
            break
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please enter a valid integer.")
    output_path = input("Enter the path to save the output image: ")
    if choice == 'y':
        encrypt_image(image_path, key, output_path)
    elif choice == 'n':
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid choice. Please press 'y' to encrypt or 'n' to decrypt.")
