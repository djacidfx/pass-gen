try:
    import random

    number = int(input('Please set number of pasword that you want make:'))
    length = int(input('Please set your password length:'))
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&'
    f = open('your_password.txt', 'w')
    f.write("your password(s): \n")
    for p in range(number):
        password = ''
        for i in range(length):
            password += random.choice(chars)
        f.write(password + '\n')
    f.close()
except BaseException as e:
    print(e.message)
