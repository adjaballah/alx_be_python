length = int(input("Enter the size of the pattern:"))

for _ in range(length): 
    for i in range(length): 
        print("*", end="")  
    print()