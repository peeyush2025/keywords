# input total bill amount
total_bill=float(input("enter the total bill amount: "))
amount_paid=float(input("enter the  amount paid: "))
due_amount= total_bill - amount_paid
if due_amount >0:
    print("no due amount.bill fully paid")
elif due_amount >0:
    print(" due amount: ",due_amount)
else:
    print("extra paid: ",abs(due_amount))
