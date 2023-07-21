duration = input("Enter the duration in seconds:")
second = int(duration)
minute = second // 60
hour = minute // 60
day = hour // 24
print("{} day,{}hour,{}minute,{}second".format(day,hour,minute,second))