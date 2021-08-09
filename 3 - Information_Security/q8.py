import sys, hashlib, os

text = sys.argv[1]


salt = os.urandom(32)

dk = hashlib.sha512(text.encode('utf-8')+salt).hexdigest()

print(dk)
