while True:
    try:
        first_number = int(input("First number:"))
        second_number = int(input("Second number:"))
    except ValueError:
        print("Value Error! Enter a number.")
        continue
    total = 0
    for i in range(first_number,second_number+1):
        if i % 2 != 0:
            total = total + i

    print(total)
    break