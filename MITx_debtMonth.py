# -- Problem 1 of Unit 2 in Introduction to Computer Science and Programming Using Python --

"""
  input = balance
  input = annualInterestRate
  input = monthlyPaymentRate
  mes = 0
  newbalance = balance
  loop de mes a 12:
      unpaid = newbalance * monthlyPaymentRate
      interest = (annualInterestRate/12.0) * unpaid
      newbalance = unpaid + interest
  print newbalance{:.4f}
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
mes = 0
newbalance = balance

while mes < 12:
    unpaid = round(newbalance - newbalance * monthlyPaymentRate, 2)
    # print("---- UNPAID", unpaid)
    interest = round((annualInterestRate / 12.0) * unpaid, 2)
    # print("---- INTEREST", interest)
    newbalance = round(unpaid + interest, 2)
    # print("---- kawhi", newbalance)
    mes += 1
    # print(mes)
print(round(newbalance, 2))
