def cube(n):
    sum=0
    while(n>=0):
        for i in range(1, n+1):
            sum = sum + i**3
        return sum
n=3
print(cube(n))