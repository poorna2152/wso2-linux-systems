import sys, hashlib, os

password = sys.argv[1]
hash_name = 'sha512'
iterations = 200000

salt = os.urandom(32)


dk = hashlib.pbkdf2_hmac(hash_name, password.encode('utf-8'), salt, iterations, dklen=None)

print(dk.hex())
