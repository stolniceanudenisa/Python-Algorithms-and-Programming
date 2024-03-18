n = int(input("n="))
k = int(input("k="))
for i in range(k+1):
    if n ** i <= k:
        print(n**i)
