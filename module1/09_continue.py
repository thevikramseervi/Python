# print 1-10 except 4 and 6

i = 1
while i <= 10:
    if i == 4 or i == 6:
        i = i + 1
        continue
    print(i)
    i = i + 1