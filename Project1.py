default_UserName="Project@123"
default_PassWord=12345678
balance=1500
def home_details():
    loop2=True
    while loop2:
        print("\n                 HOME    \n \n  	   Welcome "+default_UserName+"\n\nEnter Your Requirement \n	1.Add money to your wallet\n	2.Purchase an item\n	3.Recharge \n	4.Check Balance	\n	5.If You Want To Logout")
        choosen_Number=int(input())
        if choosen_Number==1:
            addMoney()
        elif choosen_Number==2:
            purchase()
        elif choosen_Number==3:
            recharge()
        elif choosen_Number==4:
            checkBalance()
        elif choosen_Number==5:
            loop2=False
        else:
            print("Choose suitable option")
def addMoney():
    amount=int(input("Enter the Amount: "))
    if amount>=1:
        global balance
        balance=balance+amount
        print("\n Amount added successfully to your Wallet")
        checkBalance()
    else:
        print("\n Enter valid amount\n")
        addMoney()
def purchase():
    purchase_Amount=int(input("\nEnter the amount for the purchasing item: "))
    if(purchase_Amount)>0:
        global balance
        if purchase_Amount<=balance:
            balance=balance+purchase_Amount
            print("\nPurchase the item successfully")
            checkBalance()
        else:
            print("\ninsufficient balance\nDo you want Add money?")
            credit=input()
            if (credit=="Y" or credit=="Yes" or credit=="yes" or credit=="y"):
                addMoney()
            """else:
                home_details()"""
    else:
        print("\Enter valid amount")
        purchase()
def recharge():
    recharge_amount=int(input("Enter the recharge amount: "))
    if recharge_amount>0:
        global balance
        if recharge_amount<balance:
            balance=balance-recharge_amount
            checkBalance()
        else:
            print("\ninsufficient balance\nDo you want Add money?")
            credit=input()
            if (credit=="Y" or credit=="Yes" or credit=="yes" or credit=="y"):
                addMoney()
    else:
        print("\Enter valid amount")
        purchase()
def checkBalance():
    print(balance)
def main():
    for i in range(3):
        userName=input("Enter the username: ")
        passWord=input("Enter the password: ")
        if userName==default_UserName and int(passWord)==default_PassWord:
            home_details()
            break
        else:
            print("Invalid Inputs")
main()