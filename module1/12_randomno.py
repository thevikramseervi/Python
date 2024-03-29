# Generate 5 random no and find the squares
import random
import math
for i in range(5):
    n = random.randint(1,5)
    print("random number is", n)
    print("square is", math.pow(n, 2))