from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from key_management import get_public_key

def generate_des_key():
    return get_random_bytes(8)  # DES key is 8 bytes

def encrypt_des_key_for_bob(des_key):
    bob_public_key = RSA.import_key(get_public_key("Bob"))
    cipher_rsa = PKCS1_OAEP.new(bob_public_key)
    return cipher_rsa.encrypt(des_key)

if __name__ == "__main__":
    des_key = generate_des_key()
    encrypted_key = encrypt_des_key_for_bob(des_key)
    print("DES Key:", des_key)
    print("Encrypted DES Key:", encrypted_key)
