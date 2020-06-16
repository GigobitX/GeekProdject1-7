revenue = int(input("Введите выручку вашей фирмы: "))
costs = int(input("Введите издержки вашей фирмы: "))
resultJob = revenue - costs
profitability = str(int(revenue/costs*100))
if resultJob>0:
    print("Ваша кампания прибыльна, рентабельность равна = " + profitability+"%")
elif resultJob<0:
    print("Ваша компания убыточна")
amountEmp = (int(input("Введите количество сотрудников в вашей компании: ")))
revAmountEmp = str(int(revenue/amountEmp))
print("Прибыль на одного сотрудника равна = " + revAmountEmp)