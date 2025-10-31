price = input("Please enter the price of the item")
money = input("Please enter the money amount given by the customer in cents")
if int(money) < int(price):
    print("You don't have enough money")
else:
    change = int(money) - int(price)
    print("the change is", change)
    dollar = change//100
    change_left = change - dollar*100
    quarter = change_left // 25
    change_left = change_left - quarter*25
    dime = change_left // 10
    change_left = change_left - dime*10
    nickel = change_left // 5
    change_left = change_left - nickel*5
    penny = change_left // 1
    change_left = change_left - penny*1
    print('''Dollar is:''', dollar,
          '''Quarter is:''', quarter,
          '''Dime is:''', dime,
          '''Nickel is:''', nickel,
          '''Penny is:''', penny)