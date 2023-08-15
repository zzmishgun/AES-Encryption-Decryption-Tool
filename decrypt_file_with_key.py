from cryptography.fernet import Fernet

def decrypt_file_with_key(encrypted_file_path, decryption_key):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    fernet = Fernet(decryption_key)
    decrypted_data = fernet.decrypt(encrypted_data)

    decrypted_file_path = encrypted_file_path.replace('.encrypted', '.decrypted')
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    return decrypted_file_path

def main():
    decryption_key = input("Enter the decryption key: ")
    option = input("Decrypt a file (d)? ").strip().lower()

    if option == 'd':
        encrypted_file_path = input("Enter the path of the encrypted file: ")
        decrypted_file_path = decrypt_file_with_key(encrypted_file_path, decryption_key)
        print(f"File decrypted and saved as: {decrypted_file_path}")
    else:
        print("Invalid option. Exiting...")

if __name__ == "__main__":
    main()
