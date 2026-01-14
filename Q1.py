def encrypt_char(char, shift1, shift2):
    """
    Encrypts a single character based on the custom encryption rules.
    """
    if char.islower():
        # Lowercase letters
        if 'a' <= char <= 'm':
            # First half: shift forward by shift1 * shift2
            shift = shift1 * shift2
            new_pos = (ord(char) - ord('a') + shift) % 26
            return chr(ord('a') + new_pos)
        else:  # 'n' <= char <= 'z'
            # Second half: shift backward by shift1 + shift2
            shift = shift1 + shift2
            new_pos = (ord(char) - ord('a') - shift) % 26
            return chr(ord('a') + new_pos)
    
    elif char.isupper():
        # Uppercase letters
        if 'A' <= char <= 'M':
            # First half: shift backward by shift1
            shift = shift1
            new_pos = (ord(char) - ord('A') - shift) % 26
            return chr(ord('A') + new_pos)
        else:  # 'N' <= char <= 'Z'
            # Second half: shift forward by shift2²
            shift = shift2 ** 2
            new_pos = (ord(char) - ord('A') + shift) % 26
            return chr(ord('A') + new_pos)
    
    else:
        # Other characters remain unchanged
        return char


def decrypt_char(char, shift1, shift2):
    """
    Decrypts a single character by reversing the encryption rules.
    """
    if char.islower():
        # Lowercase letters
        if 'a' <= char <= 'm':
            # Reverse: shift backward by shift1 * shift2
            shift = shift1 * shift2
            new_pos = (ord(char) - ord('a') - shift) % 26
            return chr(ord('a') + new_pos)
        else:  # 'n' <= char <= 'z'
            # Reverse: shift forward by shift1 + shift2
            shift = shift1 + shift2
            new_pos = (ord(char) - ord('a') + shift) % 26
            return chr(ord('a') + new_pos)
    
    elif char.isupper():
        # Uppercase letters
        if 'A' <= char <= 'M':
            # Reverse: shift forward by shift1
            shift = shift1
            new_pos = (ord(char) - ord('A') + shift) % 26
            return chr(ord('A') + new_pos)
        else:  # 'N' <= char <= 'Z'
            # Reverse: shift backward by shift2²
            shift = shift2 ** 2
            new_pos = (ord(char) - ord('A') - shift) % 26
            return chr(ord('A') + new_pos)
    
    else:
        # Other characters remain unchanged
        return char


def encrypt_file(input_file, output_file, shift1, shift2):
    """
    Reads from input_file, encrypts the content, and writes to output_file.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        encrypted_content = ''.join(encrypt_char(char, shift1, shift2) for char in content)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(encrypted_content)
        
        print(f"✓ Encryption complete: '{input_file}' → '{output_file}'")
        return True
    
    except FileNotFoundError:
        print(f"✗ Error: File '{input_file}' not found.")
        return False
    except Exception as e:
        print(f"✗ Error during encryption: {e}")
        return False


def decrypt_file(input_file, output_file, shift1, shift2):
    """
    Reads from input_file, decrypts the content, and writes to output_file.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        decrypted_content = ''.join(decrypt_char(char, shift1, shift2) for char in content)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(decrypted_content)
        
        print(f"✓ Decryption complete: '{input_file}' → '{output_file}'")
        return True
    
    except FileNotFoundError:
        print(f"✗ Error: File '{input_file}' not found.")
        return False
    except Exception as e:
        print(f"✗ Error during decryption: {e}")
        return False


def verify_decryption(original_file, decrypted_file):
    """
    Compares the original file with the decrypted file to verify accuracy.
    """
    try:
        with open(original_file, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        with open(decrypted_file, 'r', encoding='utf-8') as f:
            decrypted_content = f.read()
        
        if original_content == decrypted_content:
            print(f"\n✓ SUCCESS: Decryption verified! '{decrypted_file}' matches '{original_file}'")
            return True
        else:
            print(f"\n✗ FAILURE: Decryption mismatch! Files do not match.")
            print(f"   Original length: {len(original_content)} characters")
            print(f"   Decrypted length: {len(decrypted_content)} characters")
            return False
    
    except FileNotFoundError as e:
        print(f"✗ Error: {e}")
        return False
    except Exception as e:
        print(f"✗ Error during verification: {e}")
        return False


def main():
    """
    Main program that orchestrates the encryption/decryption process.
    """
    print("=" * 60)
    print("Custom Text Encryption/Decryption Program")
    print("=" * 60)
    
    # Get user inputs for shift values
    try:
        shift1 = int(input("\nEnter shift1 value (integer): "))
        shift2 = int(input("Enter shift2 value (integer): "))
    except ValueError:
        print("✗ Error: Please enter valid integer values.")
        return
    
    print(f"\nUsing shift1={shift1}, shift2={shift2}")
    print("-" * 60)
    
    # Step 1: Encrypt the file
    print("\n[Step 1] Encrypting...")
    if not encrypt_file("raw_text.txt", "encrypted_text.txt", shift1, shift2):
        return
    
    # Step 2: Decrypt the file
    print("\n[Step 2] Decrypting...")
    if not decrypt_file("encrypted_text.txt", "decrypted_text.txt", shift1, shift2):
        return
    
    # Step 3: Verify the decryption
    print("\n[Step 3] Verifying...")
    verify_decryption("raw_text.txt", "decrypted_text.txt")
    
    print("\n" + "=" * 60)
    print("Process complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
