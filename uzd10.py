def fibonacci():
    x=1
    y=0
    z=0
    sum=0
    while z <= int(4000000):
        for i in range(1, 40):
            z = x + y
            x = y
            y = z
            print(sum)
            if z % 2 == 0:
                sum += z
    print(sum)
fibonacci()