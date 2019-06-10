from pycipher import ColTrans
plaintext=input("Enter String")
key=input("Enter Key")
encryption=ColTrans(key).encipher(plaintext)
print("Encryption of ",plaintext,"is",encryption)
decryption=ColTrans(key).decipher(encryption)
print("Decryption",decryption)
