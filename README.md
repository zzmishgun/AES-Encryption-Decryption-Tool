# AES Encryption/Decryption Tool

This is a simple AES encryption/decryption tool implemented in Python using the `cryptography` library. It allows you to encrypt and decrypt files using a symmetric encryption algorithm.

## Getting Started

1. Install the required dependencies:

pip install cryptography

markdown


2. Run the `encryption_tool.py` script:

python encryption_tool.py

markdown


## Usage

1. Run the script and choose an option:
- Encrypt a file (e)
- Decrypt a file (d)

2. If you choose to encrypt a file:
- Provide the path of the file you want to encrypt.
- The encrypted file will be saved with the extension `.encrypted`.

3. If you choose to decrypt a file:
- Provide the decryption key that was used during encryption.
- Provide the path of the encrypted file you want to decrypt.
- The decrypted file will be saved with the extension `.decrypted`.

**Note:** This is a basic example for educational purposes. For real-world encryption, use secure key management practices and consult security experts.

## Security Considerations

- Do not use this tool for sensitive data without proper review and testing.
- Securely manage encryption keys and avoid hardcoding them in the script.
- For sensitive data, consider using proper key exchange and secure key management practices.
- Regularly update and patch your dependencies to ensure security.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
