from data import MENU,resources
choice=input("What would you like? (espresso/latte/cappuccino):")
coffee_machine=True
profit=0

def check_sufficient_resources(selected_drink):
    """checks if the coffee machine has enough ingredients with resources"""
    #printing the ingredients of your selected drink
    print(selected_drink)
    for item in selected_drink:
        if selected_drink[item]>resources[item]:
            print(f"oops! sorry there is not enough {item}")
            return False
        else:
            return True
def count_amount():
    """Here you will enter the amount and total amount will be returned"""
    print("Pls insert your coins")
    total=int(input("insert number of quarters"))*0.25
    total += int(input("insert number of dimes"))*0.1
    total += int(input("insert number of nickles"))*0.05
    total += int(input("insert number of pennies"))*0.01
    return total

def is_transaction_successful(total_amount,actual_cost):
    """This takes your amount and cost of your item and returns change"""
    if total_amount>actual_cost:
        print("congrats you have enough money and transaction is successful!!")
        change=(total_amount-actual_cost)
        change=round(change,2)
        print(f"Here is your change:${change}")
        global profit
        profit = round(profit + selected_drink["cost"], 2)
        return True
    else:
        print("'Sorry that's not enough money. Money refunded.'")
        return False

def remaining_quantity(selected,resources):
    """This will return the remaining quantity of the coffee machine"""
    for item in selected:
        selected[item]=selected[item]-resources[item]
    #printing remaining items in resources
    print(selected)
    return selected




if coffee_machine:
    if choice == "report":
        for fur in resources:
            #printing the resources of the coffee machine
            print(f"{fur}:{resources[fur]}ml")
            print(f"profit={profit}")
    elif choice=="off":
        #switch off the coffee machine if choice=off
      coffee_machine=False
      print("switching off the coffe Machine!!")
    else:
        #printing the ingredients of your choice along with cost
        print(MENU[choice])
        selected_drink=MENU[choice]
        check=check_sufficient_resources(selected_drink["ingredients"])
        if check:
            print("There are enough resources to prepare your item")
            total_amount=count_amount()
            print(f"total amount you entered is :{total_amount}")
            result=is_transaction_successful(total_amount,selected_drink["cost"])


if coffee_machine:
    if result: #Here i checked if the amount entered is less(here i got result=False)
        remaining_quant=remaining_quantity(selected_drink["ingredients"],resources)
        #updating the remaining amount to resources
        for item in remaining_quant:
            resources[item]=remaining_quant[item]
        print("remaining items in coffee machine is: ",end="")
        print(resources)
        print(f"profit added to your coffee machine is: {profit}")
        print(f"“Here is your {choice}. Enjoy!”")











