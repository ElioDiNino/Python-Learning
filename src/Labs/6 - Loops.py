n = int(input("Value of n:"))
for b in range(n*2):
    print("o", end="")
print()
for i in range(n-2):
        for b in range(2):
            print("o",end="")
            for c in range(n*2-2):
                print(" ", end="")
        print()
for b in range(n*2):
    print("o", end="")
print()

