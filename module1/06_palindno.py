num = int(input('Enter the number : '))
num1 = num
rev = 0
while num != 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
if num1 == rev:
    print('palindrome')
else:
    print('not a palindrome')