bill = float(raw_input('How much was your dinner bill? '))
tip = float(raw_input('How much did you tip? '))
total = float(bill+tip)
tipvalue = float(tip/bill*100)
print('Okay, so your total was $') + str(total)
print("Your tip percent was ") + str(tipvalue) + "%"
if tipvalue > 20:
    print("You're a great tipper!")
elif tipvalue == 20 or tipvalue > 10:
    print("You're an okay tipper.")
else:
    print("You're a terrible tipper!")