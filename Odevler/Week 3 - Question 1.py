my_list = [2,12, 9, 50, 7, 66,91,14, 143,23, 48, 19,100,71,28]




a = int(input("Enter a number:"))
my_list.insert(0,a)
print(my_list)


odd_numbers = [x for x in my_list if x % 2 != 0]


my_list.sort()
odd_numbers.sort()

print(my_list[::-1], odd_numbers[::-1], sep="\n")