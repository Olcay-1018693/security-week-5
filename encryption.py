from cryptography.fernet import Fernet

# Sleutel genereren en opslaan
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Laad de sleutel
def load_key():
    return open("secret.key", "rb").read()

# Versleutel het bericht
def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Ontsleutel het bericht
def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
    return decrypted_message
