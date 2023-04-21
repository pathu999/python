def topten():

    a=1

    while a <= 10:
        sq = a*a
        yield sq
        a += 1
values = topten()

for i in values:
    print(i)