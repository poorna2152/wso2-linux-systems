import sys, hashlib

password = sys.argv[1]
hash_name = 'sha512'
iterations = 200000
salt = b"Km5d5ivMy8iexuHcZrsD"


dk = hashlib.pbkdf2_hmac(hash_name, password.encode('utf-8'), salt, iterations, dklen=None)

print(dk.hex())
