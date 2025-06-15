n = 5
for i in range(1, n + 1):
    print("*" * i)

n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)


n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))



n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
