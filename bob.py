from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from key_management import generate_rsa_keypair

def decrypt_des_key(encrypted_des_key, bob_private_key):
    bob_rsa_key = RSA.import_key(bob_private_key)
    cipher_rsa = PKCS1_OAEP.new(bob_rsa_key)
    return cipher_rsa.decrypt(encrypted_des_key)

if __name__ == "__main__":
    # Simulate RSA key generation for Bob
    bob_public_key, bob_private_key = generate_rsa_keypair("Bob")

    # Placeholder for an encrypted DES key received from Alice
    encrypted_des_key = b"<encrypted DES key from Alice>"
    
    # Decrypt the received DES key
    decrypted_des_key = decrypt_des_key(encrypted_des_key, bob_private_key)
    print("Decrypted DES Key:", decrypted_des_key)
