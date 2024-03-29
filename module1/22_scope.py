def spam():
    global egg          # error without this line
    print(egg)
    egg = 'spam'
    print(egg)

egg = 'global'
spam()