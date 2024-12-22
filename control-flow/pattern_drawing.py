length = int(input("Enter the size of the pattern:"))

count = 0
while count < length:
    i = 0
    while i < length:
        print("*", end="")  
        i += 1  
    print()  
    count += 1  
