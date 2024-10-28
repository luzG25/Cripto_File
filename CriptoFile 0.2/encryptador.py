def encryptor(file_dir, key):
    from cryptography.fernet import Fernet
    import os

    file = open(file_dir, 'rb')
    file_content = file.read()
    file.close()

    f = Fernet(key)
    file_encrypted = f.encrypt(file_content)
    file = open(file_dir + '.enc', 'wb')
    os.remove(file_dir)
    file.write(file_encrypted)
    file.close()

def encryptor2(file_dir, key):
    from cryptography.fernet import Fernet

    file = open(file_dir, 'rb')
    file_content = file.read()
    file.close()

    cb = '\ '
    while cb[:1] in file_dir:
        file_dir = file_dir[file_dir.index(cb[:1]) + 1:]

    f = Fernet(key)
    file_encrypted = f.encrypt(file_content)
    file = open(file_dir + '.enc', 'wb')
    file.write(file_encrypted)
    file.close()

