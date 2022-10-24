def myfunc(a):
    newa = a[0:]
    newa += "2"
    a = newa
    print(a)

lst = "kk"
print(lst)
myfunc(lst)
print(lst)