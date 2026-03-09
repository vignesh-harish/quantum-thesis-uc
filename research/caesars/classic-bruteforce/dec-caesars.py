import os
import time

def caesar_encrypt(plaintext, shift):
    """Encrypt plaintext using Caesar cipher with given shift."""
    result = ""
    for char in plaintext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        elif char.isdigit():
            result += chr((ord(char) - ord('0') + shift) % 10 + ord('0'))
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, shift):
    """Decrypt ciphertext using Caesar cipher with given shift."""
    result = ""
    for char in ciphertext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start - shift) % 26 + start)
        elif char.isdigit():
            result += chr((ord(char) - ord('0') - shift) % 10 + ord('0'))
        else:
            result += char
    return result

def brute_force_shift(plaintext, ciphertext):
    """Perform known-plaintext attack to find the shift value."""
    # Try all possible shifts (0-25 for letters, but we'll try more for digits)
    for shift in range(26):
        encrypted = caesar_encrypt(plaintext, shift)
        if encrypted == ciphertext:
            return shift
    return None

def decrypt_all_ciphertexts(plaintext_folder="../plaintext_samples", ciphertext_folder="ciphertext_samples", output_file="decryption_metrics.txt"):
    """Decrypt all ciphertext files using known-plaintext attack and record metrics."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    plain_path = os.path.join(script_dir, plaintext_folder)
    cipher_path = os.path.join(script_dir, ciphertext_folder)
    metrics_path = os.path.join(script_dir, output_file)
    
    if not os.path.exists(plain_path):
        print(f"Error: The folder '{plain_path}' does not exist.")
        return
    
    if not os.path.exists(cipher_path):
        print(f"Error: The folder '{cipher_path}' does not exist.")
        return
    
    # Get all ciphertext files
    cipher_files = sorted([f for f in os.listdir(cipher_path) if f.endswith('.txt')])
    
    if not cipher_files:
        print(f"No .txt files found in {cipher_path}")
        return
    
    print(f"Performing known-plaintext attack on {len(cipher_files)} files...")
    print("=" * 80)
    
    # Store metrics
    metrics = []
    total_attack_time = 0
    total_decrypt_time = 0
    found_shift = None
    
    for filename in cipher_files:
        cipher_file_path = os.path.join(cipher_path, filename)
        plain_filename = filename.replace("cipher", "plain")
        plain_file_path = os.path.join(plain_path, plain_filename)
        
        # Check if corresponding plaintext exists
        if not os.path.exists(plain_file_path):
            print(f"Warning: No plaintext found for {filename}, skipping...")
            continue
        
        # Read plaintext and ciphertext
        with open(plain_file_path, 'r') as f:
            plaintext = f.read()
        with open(cipher_file_path, 'r') as f:
            ciphertext = f.read()
        
        # Time the brute force attack to find the shift
        attack_start = time.time()
        shift = brute_force_shift(plaintext, ciphertext)
        attack_end = time.time()
        attack_duration = attack_end - attack_start
        
        if shift is None:
            print(f"Failed to find shift for {filename}")
            continue
        
        # Store the first found shift as the key
        if found_shift is None:
            found_shift = shift
            print(f"Key found! Shift value: {shift}")
            print("-" * 80)
        
        # Time the actual decryption
        decrypt_start = time.time()
        decrypted = caesar_decrypt(ciphertext, shift)
        decrypt_end = time.time()
        decrypt_duration = decrypt_end - decrypt_start
        
        total_attack_time += attack_duration
        total_decrypt_time += decrypt_duration
        
        # Store metrics
        metrics.append({
            'filename': filename,
            'attack_duration': attack_duration,
            'decrypt_duration': decrypt_duration,
            'shift_found': shift,
            'ciphertext_length': len(ciphertext),
            'plaintext': decrypted
        })
        
        print(f"{filename}: Attack={attack_duration:.6f}s, Decrypt={decrypt_duration:.6f}s, Shift={shift}")
    
    if not metrics:
        print("No files were successfully processed.")
        return
    
    # Write metrics to file in table format
    with open(metrics_path, 'w') as f:
        f.write("=" * 120 + "\n")
        f.write("CAESAR CIPHER KNOWN-PLAINTEXT ATTACK METRICS\n")
        f.write("=" * 120 + "\n\n")
        f.write(f"Key Found (Shift Value): {found_shift}\n")
        f.write(f"Total Files Processed: {len(metrics)}\n")
        f.write(f"Total Attack Time (Key Discovery): {total_attack_time:.6f} seconds\n")
        f.write(f"Total Decryption Time: {total_decrypt_time:.6f} seconds\n")
        f.write(f"Average Attack Time per File: {total_attack_time/len(metrics):.6f} seconds\n")
        f.write(f"Average Decryption Time per File: {total_decrypt_time/len(metrics):.6f} seconds\n\n")
        f.write("=" * 120 + "\n")
        f.write("INDIVIDUAL FILE METRICS\n")
        f.write("=" * 120 + "\n\n")
        
        # Table header
        f.write(f"{'File Name':<25} | {'Length':<8} | {'Attack Time (s)':<16} | {'Decrypt Time (s)':<17} | {'Shift':<6} | {'Decrypted Text':<30}\n")
        f.write("-" * 120 + "\n")
        
        # Table rows
        for metric in metrics:
            filename = metric['filename']
            length = metric['ciphertext_length']
            attack_time = f"{metric['attack_duration']:.6f}"
            decrypt_time = f"{metric['decrypt_duration']:.6f}"
            shift = metric['shift_found']
            plaintext = metric['plaintext'][:30]  # Truncate if too long
            
            f.write(f"{filename:<25} | {length:<8} | {attack_time:<16} | {decrypt_time:<17} | {shift:<6} | {plaintext:<30}\n")
        
        f.write("=" * 120 + "\n")
    
    print("=" * 80)
    print(f"Attack complete!")
    print(f"Key found: Shift = {found_shift}")
    print(f"Total attack time: {total_attack_time:.6f} seconds")
    print(f"Total decryption time: {total_decrypt_time:.6f} seconds")
    print(f"Average attack time per file: {total_attack_time/len(metrics):.6f} seconds")
    print(f"Metrics saved to: {metrics_path}")

if __name__ == "__main__":
    decrypt_all_ciphertexts()