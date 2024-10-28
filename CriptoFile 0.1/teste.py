from encryptador import encryptor
from decryptador import decryptor

file = input(':')
if '"' in file:
    file = file[1:len(file) - 1]

key = b'_yAV8dQk_iYSWdqbMDwJvoTlUcB1jLIg6hz2yLB134Y='

encryptor(file, key)

file = input(':')
if '"' in file:
    file = file[1:len(file) - 1]

decryptor(file, key)
