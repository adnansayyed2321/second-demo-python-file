n = int(input())
for i in range(1,n+1):
    print("* " * i)
k = n - 1 
for i in range(1,n):
    print("* " * k)
    k = k - 1
print("END")