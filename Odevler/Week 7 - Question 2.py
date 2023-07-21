# import os
# import sys
# os.chdir((os.path.dirname(sys.argv[0])))

import json


with open("/Users/ahmetmesutcelem/VIT/Odevler/students.json") as folder:
    students = json.load(folder)
    info = students["students"]
    


while True:
    choose = input("""
    1-> Add student
    2-> Student info
    3-> Quit

    Your choose:
    """)
    if choose  == "3":
        break
    elif choose == "1":
        name = input("Student name:")
        surname = input("Student surname:")
        age = input("Student age:")
        student = {"Name":name,"Surname":surname,"Age":age}
        info.append(student)
        with open("/Users/ahmetmesutcelem/VIT/Odevler/students.json","w") as add:
            json.dump(info,add,indent=4)
    elif choose == "2":
        search = input("Student name:")
        for x in info:
            if search == x["Name"]:
                print("Student Name",x["Name"])
                print("Student Surname:",x["Surname"])
                print("Student Age:",x["Age"])
    else:
        print("Error! Try Again!")