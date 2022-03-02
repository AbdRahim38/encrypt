#!/usr/bin/env python3
#Creating encryption Key
# make sure you install the cryptography module, $ pip install cryptography

from cryptography.fernet import Fernet

key = Fernet.generate_key()

crypter = Fernet(key)
pw = crypter.encrypt(b'World Peace Always! ;)')
print(f'\nEncrypt Secret \nVersion 1 : {pw}')
print(f'Version 2 : ' + str(pw, 'utf8'))

decryptString = crypter.decrypt(pw)
print(f'\nDecrypt Secret : ' + str(decryptString, 'utf8'))