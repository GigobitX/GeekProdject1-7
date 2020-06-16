timeSec = int(input("Введите время в секундах: "))

h = timeSec//3600
m = (timeSec - h*3600) //60
s = timeSec - (h * 3600) - (m * 60)

realTime = f'В часах, минутах и секундах, это: {h}:{m}:{s}'

print(realTime)