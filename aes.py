from Crypto.Cipher import AES
import hashlib


#the text must be a multiple of 16 bytes in length
#so we have to pad
#the character we will pad with
PADDING = "~"
IV = b'\x14\x10\xbc:\xa7\x0f\x01u\x86\x95\x04V\xac\xbd\xf1\x92'
#takes the message to encrypt and the secret key
#returns the cipher as byte code, the key, and the IV
def encypt_aes(message,key):
    #we need an initialization vector

    #our key must be 16,24,or,32 bytes long
    #luckily sha256 digest always returns a unique 32 byte block for any input string
    key = hashlib.sha256(str.encode(key)).digest()

    while len(message) % 16 != 0:
        message += PADDING
    enc = AES.new(key,AES.MODE_CBC,IV)
    cipher_text = enc.encrypt(message)
    return (cipher_text)

#takes the cipher, key, and iv
#returns the plain text as a string
def decrypt_aes(cipher_text, key):
    key = hashlib.sha256(str.encode(key)).digest()
    dec = AES.new(key, AES.MODE_CBC, IV)
    plain_text = dec.decrypt(cipher_text).decode("utf-8")
    # and now we unpad
    while plain_text.endswith(PADDING):
        plain_text = plain_text[:len(plain_text) - 1]
    return plain_text

