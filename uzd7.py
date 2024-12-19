import random
uzminamais = random.randint(1, 10)
atbilde = int(input("uzmini ciparu no 1-10 "))
while uzminamais != atbilde:
    if uzminamais > atbilde:
        print("cipars ir lielaks")
        atbilde = int(input("uzmini ciparu no 1-10 "))
    elif uzminamais < atbilde:
        print("cipars ir mazaks")
        atbilde = int(input("uzmini ciparu no 1-10 "))
if uzminamais == atbilde:
    print("tu uzmineji pareizo ciparu!!!")