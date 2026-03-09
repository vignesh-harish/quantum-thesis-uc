#!/usr/bin/env python3
"""
Sequential RC4 brute-force attack - optimized for small tasks
No multiprocessing overhead - just pure sequential key testing
"""

import os
import time
import string
import itertools

def rc4_ksa(key):
    """RC4 Key Scheduling Algorithm (KSA)."""
    if isinstance(key, str):
        key = key.encode('utf-8')
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

def rc4_decrypt(ciphertext, key):
    """Decrypt ciphertext using RC4 cipher with given key (same as encryption)."""
    if isinstance(key, str):
        key = key.encode('utf-8')
    if not isinstance(ciphertext, bytes):
        ciphertext = ciphertext.encode('utf-8')
    
    S = rc4_ksa(key)
    keystream = rc4_prga(S, len(ciphertext))
    plaintext = bytes([ciphertext[i] ^ keystream[i] for i in range(len(ciphertext))])
    return plaintext

def brute_force_rc4_sequential(plaintext, ciphertext, key_length=5):
    """Sequential brute-force attack - no multiprocessing overhead"""
    alphabet = string.ascii_lowercase + string.digits
    
    attempts = 0
    for candidate_key in itertools.product(alphabet, repeat=key_length):
        attempts += 1
        key_str = ''.join(candidate_key)
        
        try:
            encrypted = rc4_encrypt(plaintext, key_str)
            if encrypted == ciphertext:
                return key_str, attempts
        except:
            continue
        
        # Progress indicator every 100000 attempts
        if attempts % 100000 == 0:
            print(f"      Attempts: {attempts:,} (current: {key_str})")
    
    return None, attempts

def decrypt_all_ciphertexts(plaintext_folder="../plaintext_samples", ciphertext_folder="ciphertext_samples", output_file="decryption_metrics_sequential.txt", key_length=5):
    """Decrypt all ciphertext files using sequential known-plaintext attack."""
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
    
    print(f"SEQUENTIAL MODE: Single-threaded brute force attack")
    print(f"Performing known-plaintext attack on {len(cipher_files)} files...")
    print(f"Key length: {key_length} characters")
    print(f"Keyspace: {36**key_length:,} possible keys")
    print("=" * 130)
    
    # Store metrics
    metrics = []
    total_attack_time = 0
    total_decrypt_time = 0
    found_key = None
    
    for idx, filename in enumerate(cipher_files, 1):
        cipher_file_path = os.path.join(cipher_path, filename)
        plain_filename = filename.replace("rc4", "plain")
        plain_file_path = os.path.join(plain_path, plain_filename)
        
        # Check if corresponding plaintext exists
        if not os.path.exists(plain_file_path):
            print(f"Warning: No plaintext found for {filename}, skipping...")
            continue
        
        # Read plaintext and ciphertext
        with open(plain_file_path, 'r') as f:
            plaintext = f.read()
        with open(cipher_file_path, 'rb') as f:
            ciphertext = f.read()
        
        print(f"\n[{idx}/{len(cipher_files)}] Attacking {filename}...")
        
        # Time the attack to find the key
        attack_start = time.time()
        result = brute_force_rc4_sequential(plaintext, ciphertext, key_length)
        attack_end = time.time()
        attack_duration = attack_end - attack_start
        
        # Handle return value (key, attempts)
        if result is None or result[0] is None:
            print(f"Failed to find key for {filename}")
            continue
        
        key, attempts = result
        
        # Store the first found key
        if found_key is None:
            found_key = key
            print(f"\n    ✓ Key found! RC4 key: {key} (length: {len(key)})")
            print(f"    Found after {attempts:,} attempts")
        
        # Time the actual decryption
        decrypt_start = time.time()
        decrypted = rc4_decrypt(ciphertext, key)
        decrypt_end = time.time()
        decrypt_duration = decrypt_end - decrypt_start
        
        # Verify decryption
        match = decrypted.decode('utf-8', errors='ignore') == plaintext
        
        total_attack_time += attack_duration
        total_decrypt_time += decrypt_duration
        
        # Store metrics
        metrics.append({
            'filename': filename,
            'attack_duration': attack_duration,
            'decrypt_duration': decrypt_duration,
            'key_found': key,
            'key_length': len(key),
            'attempts': attempts,
            'ciphertext_length': len(ciphertext),
            'plaintext': decrypted.decode('utf-8', errors='ignore'),
            'match': match
        })
        
        match_symbol = "✓" if match else "✗"
        rate = attempts / attack_duration if attack_duration > 0 else 0
        print(f"    {filename}: Attack={attack_duration:.6f}s ({rate:,.0f} keys/s), Decrypt={decrypt_duration:.6f}s, Key={key}, Match={match_symbol}")
    
    if not metrics:
        print("No files were successfully processed.")
        return
    
    # Write metrics to file in table format
    with open(metrics_path, 'w') as f:
        f.write("=" * 130 + "\n")
        f.write("RC4 CIPHER KNOWN-PLAINTEXT ATTACK METRICS (Sequential Mode)\n")
        f.write("=" * 130 + "\n\n")
        f.write(f"Key Found: {found_key}\n")
        f.write(f"Key Length: {len(found_key)}\n")
        f.write(f"Total Files Processed: {len(metrics)}\n")
        f.write(f"Total Attack Time (Key Discovery): {total_attack_time:.6f} seconds\n")
        f.write(f"Total Decryption Time: {total_decrypt_time:.6f} seconds\n")
        f.write(f"Average Attack Time per File: {total_attack_time/len(metrics):.6f} seconds\n")
        f.write(f"Average Decryption Time per File: {total_decrypt_time/len(metrics):.6f} seconds\n\n")
        f.write("=" * 130 + "\n")
        f.write("INDIVIDUAL FILE METRICS\n")
        f.write("=" * 130 + "\n\n")
        
        # Table header
        f.write(f"{'File Name':<25} | {'Length':<8} | {'Attack Time (s)':<16} | {'Decrypt Time (s)':<17} | {'Key':<10} | {'Match':<6} | {'Decrypted Text':<30}\n")
        f.write("-" * 130 + "\n")
        
        # Table rows
        for metric in metrics:
            filename = metric['filename']
            length = metric['ciphertext_length']
            attack_time = f"{metric['attack_duration']:.6f}"
            decrypt_time = f"{metric['decrypt_duration']:.6f}"
            key = metric['key_found']
            match = "✓" if metric['match'] else "✗"
            plaintext = metric['plaintext'][:30]  # Truncate if too long
            
            f.write(f"{filename:<25} | {length:<8} | {attack_time:<16} | {decrypt_time:<17} | {key:<10} | {match:<6} | {plaintext:<30}\n")
        
        f.write("=" * 130 + "\n")
    
    print("\n" + "=" * 130)
    print(f"Attack complete!")
    print(f"Key found: {found_key} (length: {len(found_key)})")
    print(f"Total attack time: {total_attack_time:.6f} seconds ({total_attack_time/60:.2f} minutes)")
    print(f"Total decryption time: {total_decrypt_time:.6f} seconds")
    print(f"Average attack time per file: {total_attack_time/len(metrics):.6f} seconds")
    print(f"Metrics saved to: {metrics_path}")

if __name__ == "__main__":
    # Read key length from file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    key_file = os.path.join(script_dir, "key_length.txt")
    
    try:
        with open(key_file, 'r') as f:
            key_from_file = f.read().strip()
            key_length = len(key_from_file)
    except FileNotFoundError:
        key_length = 5  # Default
    
    decrypt_all_ciphertexts(key_length=key_length)


