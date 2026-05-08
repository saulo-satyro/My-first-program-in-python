#Hey, this program will show for you your lowest balance over a period of days, it´s my first program :)

P = int(input("Period of days: ")) #It´s the period of bank transaction days that you want to analyze
balance = int(input("Initial balance: "))
lower_balance = balance

for count in range(int(P)):
    x = int(input("Transition "))
    balance = balance + x
    if balance < lower_balance:
      lower_balance = balance
 
print(lower_balance)