def decryptor(file_dir, key):
    from cryptography.fernet import Fernet
    import os

    file = open(file_dir, 'rb')
    file_content = file.read()
    file.close()

    f = Fernet(key)
    file_decrypted = f.decrypt(file_content)
    file = open(file_dir[:len(file_dir) - 4], 'wb')
    file.write(file_decrypted)
    os.remove(file_dir)
    file.close()

def decryptor2(file_dir, key, dir):
    from cryptography.fernet import Fernet

    file = open(file_dir, 'rb')
    file_content = file.read()
    file.close()

    f = Fernet(key)
    file_decrypted = f.decrypt(file_content)

    cb = '\ '
    while cb[:1] in file_dir:
        file_dir = file_dir[file_dir.index(cb[:1]) + 1:]

    file = open(dir + file_dir[:len(file_dir) - 4], 'wb')
    file.write(file_decrypted)
    file.close()
