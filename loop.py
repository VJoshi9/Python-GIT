# 1. Write a program to print the following number patterns using a loop.
# a)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# b)
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
a = [int(1)]
while a[-1] <=5:
    print(*a)
    a = [*a, a[-1]+1]







