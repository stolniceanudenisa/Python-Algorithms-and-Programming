def main():
    n = int(input("n="))

    sum = n * (n + 1) // 2
    print(sum)

    sum = 0
    for i in range (1, n + 1):
        sum += i
    print(sum)

main()