def run1(key):
    from encryptador import encryptor
    from decryptador import decryptor
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

def run2(key, cf):
    from encryptador import encryptor2
    from decryptador import decryptor2
    while True:
        file = (input('dir:'))
        if file == '':
            break

        else:
            try:
                if '"' in file:
                    file = file[1:len(file) - 1]

                if 'enc' in file[len(file) - 4:]:
                    decryptor2(file, key, cf[1])
                    print('Ficheiro decriptado com Sucesso!')

                else:
                    encryptor2(file, key)
                    print('Ficheiro encriptado com Sucesso')

            except:
                print('Operação Fálida!')

    if cf[2] == 1:
        import os
        for c in os.listdir(cf[1]):
            os.remove(cf[1] + c)
        os.removedirs(cf[1])
