import random

def elgamal_encrypt(plain_text, public_key):
    k = random.randint(1,public_key[0] - 1)

    y1 = pow(public_key[1], k, public_key[0])

    y2 = (ord(plain_text) * pow(public_key[2], k, public_key[0])) % public_key[0]
    return (y1,y2)

def elgamal_decrypt(cipher, public_key, private_exponent):
    m = (cipher[1] * pow(cipher[0],public_key[0] - 1 - private_exponent, public_key[0])) % public_key[0]
    return chr(m)