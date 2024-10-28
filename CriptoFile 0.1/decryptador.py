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