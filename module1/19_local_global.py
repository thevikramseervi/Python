# Local and Global Scope

def spam():
    egg = 99
    bacon()
    print(egg)

def bacon():
    egg = 0

spam()