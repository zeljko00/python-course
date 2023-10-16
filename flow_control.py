def if_flow(a,b):
    if a>b:
        print(a,">",b)
    elif a<b:
        print(a,"<",b)
    elif a==b:
        print(a,"=",b)
    else:
        # do nothing
        pass

def for_flow(range):
    for item in range:
        print(range)

def for_index_flow(range):
    for index in enumerate(range):
        print(index)

def for_zip_flow(range1,range2):
    for tuple in zip(range1,range2):
        print(tuple)

def while_flow(n):
    while n>0:
        print(n)
        n=n-1