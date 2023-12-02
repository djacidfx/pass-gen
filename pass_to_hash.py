import hashlib


password = input('enter your password: ')
hashedPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
print(hashedPassword)
