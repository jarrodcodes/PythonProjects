global coinAmount
global userContinue
coinAmount = 0
userContinue = str(raw_input('Would you like a coin? Yes or no. '))
def saidYes():
    global userContinue
    global coinAmount
    coinAmount = coinAmount + 1
    if coinAmount == 1:
            print str("Okay, now you have ") + str(coinAmount) + " coin."
    else:        
        print str("Okay, now you have ") + str(coinAmount) + " coins."
    userContinue = str((raw_input('Would you like another coin? ')))
    if userContinue == 'Yes' or userContinue == 'yes' or userContinue == 'y':
        saidYes()

while userContinue == 'Yes' or userContinue == 'yes' or userContinue == 'y':
    saidYes()
else:
    if coinAmount == 1:
            print str("Okay, you have finished with ") + str(coinAmount) + " coin."
    else:
        print "Okay, you have finished with " + str(coinAmount) + " coins."