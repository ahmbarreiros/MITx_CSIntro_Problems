# -- Problem 2 of Unit 2 in Introduction to Computer Science and Programming Using Python --

"""
pseudocode:
 input = balance
 input = annualInterestRate
 newbalance = balance
 fixpay = 0

 while newbalance > 0:
  unpaid = newbalance - fixpay
  newbalance = unpaid + ((annualInterestRate / 12.0) * unpaid)
  fixpay += 10

  minPay = fixpay / 12
  print minPay
"""

balance = 3926000000000000000
annualInterestRate = 0.2
newBalance = balance
fixPay = 32


while True:
    unpaid = balance - fixPay
    # print(unpaid)
    newBalance = unpaid + ((annualInterestRate / 12.0) * unpaid)
    aft12 = unpaid + (annualInterestRate * unpaid)
    if aft12 - (fixPay * 12) < 0:
        break
    else:
        fixPay += 32
    # print("---FIXPAY", fixPay)


print(fixPay)
