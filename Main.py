#Change Calculator
# Read in a cost
# Read in the amount given
# Calculate the change
# Break the change into how many nickels, dimes, quarters
# loonies, toonies, $5s, $10s, $20s, $50s, $100s
# If amount is below the cost, say how much more they owe.
cost=float(input("How much does the item cost?"))
amount=float (input("What's the payment?"))
change=amount-cost
print ("Your change is", change)
hundred=change//100
change=change%100
if hundred>0:
    print (hundred, " x $100")
fifty=change//50
change=change%50
if fifty>0:
    print (fifty, " x $50")
twenty=change//20
change=change%20
if twenty>0:
    print (twenty, " x $20")
ten=change//10
change=change%10
if ten>0:
    print (ten, " x $10")
five=change//5
change=change%5
if five>0:
    print (five, " x $5")
toonie=change//2
change=change%2
if toonie>0:
    print (toonie, " x $2")
one=change//1
change=change%1
if one>0:
    print (one, " x $1")
quarter=change//0.25
change=change%0.25
if quarter>0:
    print (quarter, " x $0.25")
dime=change//0.10
change=change%0.10
if dime>0:
    print (dime, " x $0.10")
nickle=change//0.05
change=change%0.05
if nickle>0:
    print (nickle, " x $0.05")
if change<0.03:
    nickle=nickle + 0.05





