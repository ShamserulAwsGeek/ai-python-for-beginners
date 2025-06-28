
#Get details of loan:
money_owed = float(input("How much money do you owe, in dollars?\n"))  #$50,000
apr = float(input("what is the annual percentage rate of the loan?\n"))  #3%
payment = float(input("How much you will pay each month in dollars?\n")) #1000
months = float(input("How many months do you wants to see the results for?\n"))  #24


monthly_rate = apr/100/12

for i in range(months):
    #calculate interest to pay:
    interest_paid = money_owed * monthly_rate

    #add in interest:
    money_owed = money_owed + interest_paid

    if (money_owed - payment <0):
        print("the last payemtn is", money_owed)
        print("you paid off the laon in", i+1, "months")
        break

    #make payment:
    money_owed = money_owed - payment

    print("paid", payment, "of which", interest_paid, "was interest", end = '')
    print("Now I owe", money_owed)