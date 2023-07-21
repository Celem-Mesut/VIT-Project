
l = [1, 5, 4, 12, 45, 1, 2, 54, 65, 77, 8, 55, 2, 72, 12]


uniek = set()
repeat = set()


for i in l:
    if i in uniek:
        repeat.add(i)
    else:
        uniek.add(i)


print(uniek,repeat, sep="\n")