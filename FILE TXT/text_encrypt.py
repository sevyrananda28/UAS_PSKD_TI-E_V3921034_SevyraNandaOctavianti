import binascii

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

file_to_encrypt = open('FILE TXT/file_txt.txt', 'rb')
data = file_to_encrypt.readlines()

txt = str(data[11])
txt_binary = txt.encode()

keyPair = RSA.generate(1024)

pubKey = keyPair.publickey()
pubKeyPEM = pubKey.exportKey()

chiper = PKCS1_OAEP.new(pubKey)
encrypted = chiper.encrypt(txt_binary)
binnary = binascii.hexlify(encrypted)
print("Encrypted: ", binascii.hexlify(encrypted))

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
plaintext = decrypted.decode()
print("Decrypted: ", plaintext)

with open('encrypted_file.txt', 'wb') as file_out:
    file_out.write(binnary)

with open('decrypted_file.txt', 'wb') as file:
    file.write(plaintext)