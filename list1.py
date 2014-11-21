def prime(x):
    for i in range(2,x):
        if x % i == 0:
            return


    return x;
nums = range(2,100)
result = filter(prime,nums)
print result
