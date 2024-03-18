n = int(input("n="))
k = c = 0
while n != 0:
    c = n % 10
    if c == 5:
        k = k + 1
        n = n / 10
    n = int(input("n="))
