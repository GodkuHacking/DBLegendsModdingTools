# decrypt.py
# Made by Godku...

import os
import sys

# Function to decrypt a file
def decrypt_file(file_path):
    # Read file into memory
    with open(file_path, 'rb') as file:
        file_bytes = bytearray(file.read())

    # Decrypt the bytes
    for i in range(len(file_bytes)):
        file_bytes[i] = (~file_bytes[i] + 256) & 0xFF

    # Write back to file
    with open(file_path, 'wb') as file:
        file.write(file_bytes)

def Decrypt(filename):
    # Get the folder path where the module is located
    folder_path = os.path.dirname(os.path.abspath(__file__))
    target_file_path = os.path.join(folder_path, filename)
    
    try:
        decrypt_file(target_file_path)
        print(f"File '{filename}' decrypted successfully.")
    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    Decrypt(filename)
