"""
По данному числу n вычислите сумму 1+122+132+...+1n21+221+321+...+n21.

"""

var = int(input())
sum = 0.0
counter = 1
while counter <= var:
    sum += 1.0 / (counter * counter)
    counter += 1
print("{:.5f}".format(sum))