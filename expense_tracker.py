



import os
from datetime import datetime
import pandas as pd

print("""

Add Income   ---> 1
Add Expense  ---> 2
View Balance ---> 3
View History ---> 4
Exit         ---> 5

""")

balance = 0

if os.path.exists("balance.txt"):
    with open("balance.txt", "r") as f:
        balance = int(f.read())

history = []  

if os.path.exists("expenses.csv"):
    df = pd.read_csv("expenses.csv")
    history = df["Transaction"].tolist()
    print("✅ History loaded!")


while True:
    option = (input("Choose: "))
    
    if option == "1":
        deposit = int(input("Add Income:"))
        if deposit > 0: 
            balance += deposit
            history.append(f"Income: ₹{deposit} | {datetime.now().strftime('%d-%m-%Y')}")
            print(f"✅ ₹{deposit} Added! 💰 Balance: ₹{balance}")
            df = pd.DataFrame(history, columns=["Transaction"])
            df.to_csv("expenses.csv", index=False)
            with open("balance.txt", "w") as f:
                f.write(str(balance))
    elif option == "2":
        enter = int(input("Add Expense:"))
        if enter > 0:
            balance -= enter
            history.append(f"Expense: ₹{enter} | {datetime.now().strftime('%d-%m-%Y')}")
            print(f"✅ ₹{enter} Spent! 💰 Balance: ₹{balance}")
            df = pd.DataFrame(history, columns=["Transaction"])
            df.to_csv("expenses.csv", index=False)
            with open("balance.txt", "w") as f:
                f.write(str(balance))
    elif option == "3":
        print(f"💰 Balance: ₹{balance}")
    elif option == "4":
        print("\n--- Expense History ---")
        if len(history) == 0:
            print("No Expense took place")
        else:                          
            for h in history:
                print(h)
    elif option == "5":
        print("Thank you for Expense ")  
        break
    else:
        print("❌ Invalid Option!")








