n = int(input("Enter n (n > 2): "))
k = int(input("Enter k (k < n): "))

for i in range(1, n + 1):
    if i % k == 0:
       continue
    print(i)