def showmenu():   
    print()
    print("[Drink Menu]")
    for i in range(0, len(menu)):
        print(i+1, ".", menu[i], "\tPrice : ", price[i])
    print()
def buy(num):    
    if money < price[num]:
        print("Incorrect Amount. Current Balance : %d" %money) 
        return money
    else:
        print("Your Choice",menu[num])
        balance = money - price[num]
        print("Current Balance : ", balance)
        return balance
if __name__ == '__main__':
    
    menu = ("Coke", "Juice", "Water", "Coffe")
    price = (1.50, 4.27, 1.00, 7.58)
    money = 0
    money = float(input("Please Insert Money First : "))
    
    while True:
        showmenu()
        sel = int(input("Select Another Menu or Finish Button 0 : "))
        if sel == 0:
            break
        elif(sel>=1 and sel <= len(menu)):
            money = buy(sel-1)
        else:
            print("Wrong Menu")
        
    print("Finished, Balance %d, Change" %money)

    