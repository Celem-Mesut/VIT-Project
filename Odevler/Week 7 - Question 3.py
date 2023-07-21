def read_folder():
    folder_name = input("Folder Name:")
    Total = 0
    with open(folder_name,"r") as d:
        my_list = d.readlines()
        for x in my_list:
            Total += int(x)
            average = Total / len(my_list)
    print("Average:",average)

read_folder()