def max(a, b):
    if a>b:
       b = a
    return b




r=int(input("Введите количество чисел"))
A = [0] * r
k=-100000000000000000000000000000000000000000000000000000000000000
for i in range (r):
    print(i+1, "Введите число:",)
    A[i]=float(input())
    k=max(A[i], k)    
print(k)