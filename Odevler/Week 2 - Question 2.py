numbers = [42, 29, 17, 15, 10, 9, 6, 4, 2, 1]


total = 0


for i in numbers:
    total += i


average = total / len(numbers)
print(average)


higher = 0
lower = 0

for x in numbers:
    if x > average:
        print("YUKSEK")
        higher += 1

    elif x < average:
        print("DUSUK")
        lower += 1


print("high:{} \low:{}".format(higher,locals))