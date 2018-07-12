N=int(input())
if type(N)==int:
    if N<=1 or N<=100000:
        if N%2==0:
            print("Even")
        else:
            print("Odd")
else:
    print("invalid")
