"""
Problem #2
Even Fibonacci Numbers
"""
previous = 1
current = 2
evenSum = 0

while (current < 4000000):
    if (current % 2 == 0):
        evenSum += current
    temp = current + previous
    previous = current
    current = temp

print("Answer: " + str(evenSum))