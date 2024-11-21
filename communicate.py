from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Encrypt a message using DES
def encrypt_message(des_key, plaintext):
    cipher_des = DES.new(des_key, DES.MODE_ECB)
    return cipher_des.encrypt(pad(plaintext, DES.block_size))

# Decrypt a message using DES
def decrypt_message(des_key, ciphertext):
    cipher_des = DES.new(des_key, DES.MODE_ECB)
    return unpad(cipher_des.decrypt(ciphertext), DES.block_size)

# Example usage
if __name__ == "__main__":
    des_key = b"<8-byte DES key>"
    plaintext = b"Hello, Bob!"

    # Encrypt the message
    ciphertext = encrypt_message(des_key, plaintext)
    print("Ciphertext:", ciphertext)

    # Decrypt the message
    decrypted_text = decrypt_message(des_key, ciphertext)
    print("Decrypted Text:", decrypted_text)
