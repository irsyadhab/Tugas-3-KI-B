from Crypto.PublicKey import RSA

public_key_authority = {}

def generate_rsa_keypair(name):
    key = RSA.generate(2048)
    public_key = key.publickey().export_key()
    private_key = key.export_key()
    public_key_authority[name] = public_key
    return public_key, private_key

def get_public_key(name):
    return public_key_authority.get(name)
