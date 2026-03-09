import random
import string
import time
import os
import secrets

def generate_repeatable_files(num_files=70, seq_length=10, master_seed=42):
    # Setup directory
    folder_name = "plaintext_samples"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    start_time = time.time()
    chars = string.ascii_letters + string.digits
    
    print(f"Generating {num_files} files in '{folder_name}'...")

    for i in range(1, num_files + 1):
        filename = f"plain-text-{i}.txt"
        file_path = os.path.join(folder_name, filename)
        
        # Unique seed per file ensures absolute repeatability for each filename
        random.seed(master_seed + i)
        
        # Generate the 10 character sequence
        content = ''.join(random.choice(chars) for _ in range(seq_length))
        
        with open(file_path, 'w') as f:
            f.write(content)
            
    end_time = time.time()
    
    print("-" * 35)
    print("Process Complete!")
    print(f"Destination: {os.path.abspath(folder_name)}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    print("-" * 35)
