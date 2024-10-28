from hashlib import sha256
from os import system, makedirs
from config import config
from main import run1, run2

cf = config()
#[mode, main_dir, clean, data]

key = (sha256((input('Chave: ').encode())).hexdigest())[:43] + '='
system('cls')

if cf[0] == 0:
    run1(key)

else:
    if cf[2] == 1:
        makedirs(cf[1] + '/files/')
        cf[1] += '/files/'
    run2(key, cf)
