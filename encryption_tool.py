from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    return encrypted_file_path

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    decrypted_file_path = encrypted_file_path.replace('.encrypted', '.decrypted')
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    return decrypted_file_path

def main():
    key = generate_key()
    print(f"Generated Key: {key}")

    option = input("Encrypt (e) or Decrypt (d) a file? ").strip().lower()

    if option == 'e':
        file_path = input("Enter the path of the file to encrypt: ")
        encrypted_file_path = encrypt_file(file_path, key)
        print(f"File encrypted and saved as: {encrypted_file_path}")
    elif option == 'd':
        encrypted_file_path = input("Enter the path of the encrypted file: ")
        decrypted_file_path = decrypt_file(encrypted_file_path, key)
        print(f"File decrypted and saved as: {decrypted_file_path}")
    else:
        print("Invalid option. Exiting...")

if __name__ == "__main__":
    main()
