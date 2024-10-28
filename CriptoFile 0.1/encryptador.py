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
