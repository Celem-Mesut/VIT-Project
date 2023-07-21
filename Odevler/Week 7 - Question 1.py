folder = input("Folder Name:")
line = 1
with open(folder,"r+") as d:
    my_list = d.readlines()
    d.seek(0)
    for x in my_list:
        row = (str(line),"-",x)
        line += 1
        d.writelines(row)
print(folder)
