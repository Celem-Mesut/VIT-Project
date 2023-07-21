my_list = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6,"appel","Netherland"]


print(my_list[2][1])


print(my_list[-1])



new_list = my_list[3:7]
print(new_list)
print(len(new_list))


list_a = [x for x in range(0,20) if x % 2 == 0]
print(len(list_a),list_a)