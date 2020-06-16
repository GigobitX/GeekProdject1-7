uAns = int(input("Введите число: "))
taskAns = uAns % 10
uAns = uAns//10
while uAns>0:
    if uAns % 10>taskAns:
        taskAns = uAns%10
    uAns = uAns//10

print(taskAns)
