#expense_calculator



while True:
    try:
     n = int(input("enter the number of expenses you want to enter: "))
     if n > 0:
          break
        
     else:
          print("enter your valid number")
    except ValueError:
     print("enter your whole valid number")
     

     




expense = []
for i in range(n):
    print("please enter your expenses below")
    print("enter your catogary expense: ")
    while True:
        try:
             
    
            expense_value = float(input("enter your expense: "))

            if expense_value >0:
                 
                break
            else:
                print("please enter positive amount:")
        except ValueError:
             print("enter your valid amount")

    while True:
                    category = str(input("enter your category (shopping/food/travel): ").strip().lower())
                    if category in ["shopping", "food", "travel"]:
                        break
                    else:
                        print("invalide category! please enter your category type [shopping, food, travel]")     
    expense.append((expense_value, category ))

category_total = {}

for amount, category in expense:
        if category in category_total:
            category_total[category]+=amount
        else:
            category_total[category]=amount
print("category-wise expense")



for category,amount in category_total.items():
    print(f"{category}: ₹{amount:.2f}")


total = sum(amount for amount, category in expense)


if expense:
               highest_expense = max(expense, key=lambda x: x[0])
               lowest_expense = min(expense, key=lambda x: x[0])

               print(f"highest amount: ₹{highest_expense[0]:.2f}")
               print(f"highest category:  {highest_expense[1]}")

               print(f"lowest amount: ₹{lowest_expense[0]:.2f}")
               print(f"lowest category: {lowest_expense[1]}")
else:
    print("no expense entered:")



if total >1000:
    print("you have spent more than 1000")
elif total == 1000:
     print("you have spent exactly 1000")
else:
    print("you have spent less than 1000")

print("your expenses are ", expense)
print(f"total expense is: ₹{total:.2f}")
