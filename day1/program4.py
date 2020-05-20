#sp cp of product
a=int(input("cost price:"))
b=int(input("selling price:"))
profit=b-a
profitpercent=(profit*100)/a
print("profit :",profit)
print("profit percent from this sell:",profitpercent)
newprofit=profitpercent+5
PROFIT=newprofit*a/100
sp=PROFIT+a
print("new sp:",sp)
