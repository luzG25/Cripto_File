from encryptador import encryptor
from decryptador import decryptor
from hashlib import sha256
import os

key = (sha256((input('Chave: ').encode())).hexdigest())[:43] + '='
os.system('cls')

while True:
    file = (input('dir:'))
    if file == '':
        break

    else:
        try:
            if '"' in file:
                file = file[1:len(file) - 1]

            if 'enc' in file[len(file) - 4:]:
                decryptor(file, key)
                print('Ficheiro decriptado com Sucesso!')

            else:
                encryptor(file, key)
                print('Ficheiro encriptado com Sucesso')

        except:
            print('Operação Fálida!')
