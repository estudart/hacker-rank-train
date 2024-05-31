bill = [2, 4, 6]
k = 2
b = 12

def bonAppetit(bill, k, b):
    # Write your code here
    anna_bill = (sum(bill) - bill[k]) / 2

    if anna_bill == b:
        print("Bon Appetit")
    else:
        print(int((sum(bill) / 2) - anna_bill))
        return int((sum(bill) / 2) - anna_bill)

bonAppetit(bill, k, b)
