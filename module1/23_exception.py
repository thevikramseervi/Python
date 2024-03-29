def spam(d):
    try:
        return (42 / d)
    except ZeroDivisionError:
        print('Invalid input')

print(spam(2))
print(spam(0))
print(spam(3))