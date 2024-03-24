while True:
    name = input('Enter your name: ')
    if name != 'joe':
        continue
    password = input('Hello Joe, Enter your password: ')
    if password == 'fish':
        break
print('Access granted')