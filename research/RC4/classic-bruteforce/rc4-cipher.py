import os
import time

def rc4_ksa(key):
    """RC4 Key Scheduling Algorithm (KSA)."""
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def rc4_prga(S, length):
    """RC4 Pseudo-Random Generation Algorithm (PRGA)."""
    i = 0
    j = 0
    keystream = []
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)
    return keystream

def rc4_encrypt(plaintext, key):
    """Encrypt plaintext using RC4 cipher with given key."""
    if isinstance(key, str):
        key = key.encode('utf-8')
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    
    S = rc4_ksa(key)
    keystream = rc4_prga(S, len(plaintext))
    ciphertext = bytes([plaintext[i] ^ keystream[i] for i in range(len(plaintext))])
    return ciphertext

def read_key(key_file="key_length.txt"):
    """Read the encryption key from a file."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(script_dir, key_file)
    
    try:
        with open(key_path, 'r') as f:
            key = f.read().strip()
        print(f"Key loaded from '{key_file}': {key}")
        return key
    except FileNotFoundError:
        print(f"Warning: '{key_file}' not found. Using default key 'secret'.")
        return "secret"

def process_ciphers(input_folder="../plaintext_samples", output_folder="ciphertext_samples", key_file="key_length.txt"):
    """Encrypt all plaintext files using RC4 with the same key."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Resolve paths relative to script location
    input_path = os.path.join(script_dir, input_folder)
    output_path = os.path.join(script_dir, output_folder)
    
    # Read the key from file
    key = read_key(key_file)
    
    if not key:
        print("Error: Key cannot be empty!")
        return
    
    if not os.path.exists(input_path):
        print(f"Error: The folder '{input_path}' does not exist. Run the first script first!")
        return

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    start_time = time.time()
    files_processed = 0

    # List all .txt files in the source folder
    files = sorted([f for f in os.listdir(input_path) if f.endswith('.txt')])

    for filename in files:
        file_input_path = os.path.join(input_path, filename)
        file_output_path = os.path.join(output_path, filename.replace("plain", "rc4"))

        # Read the plaintext
        with open(file_input_path, 'r') as f:
            plaintext = f.read()

        # Encrypt the content
        ciphertext = rc4_encrypt(plaintext, key)

        # Write to the new file (as hex string for readability)
        with open(file_output_path, 'wb') as f:
            f.write(ciphertext)
        
        files_processed += 1

    end_time = time.time()
    
    print("-" * 40)
    print("RC4 Encryption Complete!")
    print(f"Files Processed: {files_processed}")
    print(f"Input Folder: {input_path}")
    print(f"Output Folder: {output_path}")
    print(f"Key: {key}")
    print(f"Key Length: {len(key)}")
    print(f"Time Taken: {end_time - start_time:.6f} seconds")
    print("-" * 40)

if __name__ == "__main__":
    process_ciphers()

