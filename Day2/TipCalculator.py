print("Welcome to the tip calculator")
bill=input("What was the total bill?")
per=input("What percentage would you like to give? 10 12 or 15?")
ppl=input("how many people would like to split the bill?")
fp=float(bill)*(int(per)/100)
res=(float(bill)+fp)/int(ppl)
print("Each person should pay:"+str(round(res,2)))
