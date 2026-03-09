import os
import time

def caesar_cipher(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            result += chr((ord(char) - start + shift) % 26 + start)
        elif char.isdigit():
            # Shift digits and wrap around 0-9
            result += chr((ord(char) - ord('0') + shift) % 10 + ord('0'))
        else:
            # Leave symbols/spaces as is
            result += char
    return result

def read_key_length(key_file="key_length.txt"):
    """Read the key length (shift value) from a file."""
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(script_dir, key_file)
    
    try:
        with open(key_path, 'r') as f:
            key_length = int(f.read().strip())
        print(f"Key length loaded from '{key_file}': {key_length}")
        return key_length
    except FileNotFoundError:
        print(f"Warning: '{key_file}' not found. Using default shift of 3.")
        return 3
    except ValueError:
        print(f"Warning: Invalid value in '{key_file}'. Using default shift of 3.")
        return 3

def process_ciphers(input_folder="../plaintext_samples", output_folder="ciphertext_samples", key_file="key_length.txt"):
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Resolve paths relative to script location
    input_path = os.path.join(script_dir, input_folder)
    output_path = os.path.join(script_dir, output_folder)
    
    # Read the key length from file
    shift = read_key_length(key_file)
    
    if not os.path.exists(input_path):
        print(f"Error: The folder '{input_path}' does not exist. Run the first script first!")
        return

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    start_time = time.time()
    files_processed = 0

    # List all .txt files in the source folder
    files = [f for f in os.listdir(input_path) if f.endswith('.txt')]

    for filename in files:
        file_input_path = os.path.join(input_path, filename)
        file_output_path = os.path.join(output_path, filename.replace("plain", "cipher"))

        # Read the plaintext
        with open(file_input_path, 'r') as f:
            plaintext = f.read()

        # Encrypt the content
        ciphertext = caesar_cipher(plaintext, shift)

        # Write to the new file
        with open(file_output_path, 'w') as f:
            f.write(ciphertext)
        
        files_processed += 1

    end_time = time.time()
    
    print("-" * 40)
    print("Encryption Complete!")
    print(f"Files Processed: {files_processed}")
    print(f"Input Folder: {input_path}")
    print(f"Output Folder: {output_path}")
    print(f"Shift Value: {shift}")
    print(f"Time Taken: {end_time - start_time:.6f} seconds")
    print("-" * 40)

if __name__ == "__main__":
    process_ciphers()