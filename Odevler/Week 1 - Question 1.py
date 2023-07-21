pi = 3.14
r = (input("Enter the half diameter of the circle:"))
r2 = int(r) ** 2
area = r2 * pi
answer = ("area of the circle:{} m2".format(area))
print(answer, "\n", "-" * len(answer),sep = "")