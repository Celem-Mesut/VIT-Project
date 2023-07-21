import random

rice =[[0],[0],[0],[0],[0],[0]]

repeat = 5000

while repeat > 0:
    point = random.randint(1,6)
    repeat -= 1
    if point == 1:
        rice[point-1][0] += 1
    elif point == 2:
        rice[point-1][0] += 1 
    elif point == 3:
        rice[point-1][0] += 1 
    elif point == 4:
        rice[point-1][0] += 1 
    elif point == 5:
        rice[point-1][0] += 1 
    elif point == 6:
        rice[point-1][0] += 1 


for x,y in enumerate(rice,1):
    print("Probability of getting {} value:{}".format(x,y[0] /100))
