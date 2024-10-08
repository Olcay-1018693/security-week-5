from flask import Flask, render_template, request
from encryption import encrypt_message, decrypt_message

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form['message']
    encrypted_message = encrypt_message(message)
    return render_template('index.html', result=encrypted_message.decode(), action="Encrypted")

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_message = request.form['message']
    decrypted_message = decrypt_message(encrypted_message)
    return render_template('index.html', result=decrypted_message, action="Decrypted")

if __name__ == '__main__':
    app.run(debug=True)
