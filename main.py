# Marvish Chandra
# Auto Loan Calculator 


def calculatePayment(carCost,loanTerm,interestRate,downPayment,salesTax,titleCost):
    findAuto = (carCost / loanTerm) * (interestRate / 100) - downPayment * (salesTax / 100) + titleCost
    print(findAuto)


calculatePayment(157000,60,0.7,10000,13,3000)
