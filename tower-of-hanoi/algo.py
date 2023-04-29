def func(n,a,b,c):
    if n == 1:
        print("Place ring 1 in stick", b)
    elif n%2 == 0:
        func(n-1,a,b,c)
        print("Place ring", n, "in stick", c)
        func(n-1,b,c,a)
    else:
        func(n-1,a,b,c)
        print("Place ring", n, "in stick", b)
        func(n-1,c,a,b)

func(int(input("Please enter the height of the stack - ")),"A","B","C")
