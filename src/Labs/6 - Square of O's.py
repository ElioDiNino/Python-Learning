n = int(input("Value of n:"))
for num in range(2):
    for b in range(n*2):
        print("o", end="")
    print()
    if num == 0:
        for i in range(n-2):
                for b in range(2):
                    print("o",end="")
                    for c in range(n*2-2):
                        print(" ", end="")
                print()

