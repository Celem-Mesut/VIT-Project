#Name, surname and student number were requested from the user.
name = input("Name:")
surname = input("Surname:")
number = input("Student Number:")


#The name of four different lessons and 
#the midterm and final grades of these lessons were requested from the user.
#Lesson1
lesson1 = input("1. Lesson name:")
midterm1 = int(input("1. Lesson midterm:"))
final1 = int(input("1. Lesson final:"))

#Lesson2
lesson2 = input("2. Lesson name:")
midterm2 = int(input("2. Lesson midterm:"))
final2 = int(input("2. Lesson final:"))

#Lesson3
lesson3 = input("3. Lesson name:")
midterm3 = int(input("3. Lesson midterm:"))
final3 = int(input("3. Lesson final:"))

#Lesson4
lesson4 = input("4. Lesson name:")
midterm4 = int(input("4. Lesson midterm:"))
final4 = int(input("4. Lesson final:"))

#The average of the course grades was calculated.
total1 = (midterm1 * 0.4) + (final1 * 0.6)
total2 = (midterm2 * 0.4) + (final2 * 0.6)
total3 = (midterm3 * 0.4) + (final3 * 0.6)
total4 = (midterm4 * 0.4) + (final4 * 0.6)

# Announcement of lessons results
#Lesson1
if total1 >= 50:
    print("{} lesson is passed. Your point:{}".format(lesson1,total1))
elif total1 < 50:
    print("{} lesson is failed. Your point:{}".format(lesson1,total1))

#Lesson2
if total2 >= 50:
    print("{} lesson is passed. Your point:{}".format(lesson2,total2))
elif total2 < 50:
    print("{} lesson is failed. Your point:{}".format(lesson2,total2))

#Lesson3
if total3 >= 50:
    print("{} lesson is passed. Your point:{}".format(lesson3,total3))
elif total3 < 50:
    print("{} lesson is failed. Your point:{}".format(lesson3,total3))

#Lesson4
if total4 >= 50:
    print("{} lesson is passed. Your point:{}".format(lesson4,total4))
elif total4 < 50:
    print("{} lesson is failed. Your point:{}".format(lesson4,total4))