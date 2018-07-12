N=int(input())
K=int(input())
sum1=0
array=[]
for num in range(N):
    n=int(input())
    array.append(n)
for num1 in range(K):
    sum1 = sum1 + array[num1]       
print(sum1)
