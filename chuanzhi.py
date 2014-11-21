a = [4,5]

print a
def f(c):
    #global a
    a = 1
    global a
    print a

f(a)
