def spam():
    egg = 'spam'
    print(egg)

def bacon():
    egg = 'bacon'
    print(egg)
    spam()
    print(egg)

egg = 'global'
bacon()