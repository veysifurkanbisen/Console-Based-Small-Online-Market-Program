### Veysi_Furkan_Bisen ### Talha_Sagdan ###

from datetime import datetime   #Imported to show the date and time in bill

users = {"ahmet": "sehir123", "meryem": "4444"}     #Saved profiles to enter the program

inventory = {'asparagus': [10, 5], 'broccoli': [15, 6], 'carrots': [18, 7],         #
             'apples': [20, 5], 'banana': [10, 8], 'berries': [30, 3],              # Saved Inventory
             'eggs': [50, 2], 'mixed fruit juice': [0, 8], 'fish sticks': [25, 12], #
             'ice cream': [32, 6], 'apple juice': [40, 7], 'orange juice': [30, 8], #
             'grape juice': [10, 9]}

basket = {"ahmet":{},"meryem":{}}   #Empty baskets that users are going to save their products in
list=[]
def user():     #The function that lets users to enter valid creditantials to enter the program
    global username
    print "****Welcome to Online Market****"
    print "Please log in by providing your user credentials:"
    while True:
        username=raw_input("User Name:")
        password=raw_input("Password:")
        welcome="Welcome, "+username+"! Please choose one of the following options by entering the corresponding menu number."
        if username in users and  users[username] == password:    #the possibility of both username and password is correct
            print "Successfully logged in!"
            print welcome
            main_menu()
            pass
        else:   #the possibilty of eigther username or pass word is wrong
            print "Your user name and/or password is not correct. Please try again!"
            continue

def main_menu():  #the function for user to make decision about what they want to do
    mainmenu=raw_input("Please choose one of the following services:" +"\n\t"+"1. Search for a product" +"\n\t"+"2. See Basket"+"\n\t"+"3. Check Out"+"\n\t"+"4. Logout"+"\n\t"+"5. Exit"+2*"\n"+"Your Choice:")

    if mainmenu=="1":
        searchingfor = raw_input("What are you searching for?\n").lower()
        if searchingfor==0:
            main_menu()
        else:
            search(searchingfor)
    elif mainmenu=="2":
        print "\nYour basket contains:"
        see_basket()
    elif mainmenu=="3":
        checkout()
    elif mainmenu=="4":
        user()
    elif mainmenu=="5":
        exit()
    else:
        main_menu()

def search(searchingfor):   # the search function(with the information that was given by username which is searchingfor). it is for user to find the items
    i=1
    for items in inventory:
        if searchingfor in items:
            if inventory[items][0]!=0:
                print str(i)+".",items,"$"+str(inventory[items][1])
                i = i + 1
                list.append((items,inventory[items][0],inventory[items][1]))

    wrongchoice(searchingfor)   #calls the wrongchoice function after the for loop ends and finds the all items that includes what user is looking for

def wrongchoice(searchingfor):      #the wrongchoice function created for if users input does not match any items.
    while True:
        if len(list)==0:
            wrongchoice = raw_input("Your search did not match any items. Please try something else (Enter 0 for main menu):").lower()

            if wrongchoice=="0":
                main_menu()
            search(wrongchoice)
        else:
            del list[:]
            basketma(searchingfor)
        break

def basketma(searchingfor):     #the basketma function is for saving the choosen items in the users basket
    select = raw_input("Please select which item you want to add to your basket (Enter 0 for main menu):" )
    i = 0
    if select=="0":
        return main_menu()
    else:
        for items in inventory:
            if searchingfor in items:
                if inventory[items][0]!=0:
                    i = i + 1
                    if str(i)==select:
                        basket[username][items]=(items,int(inventory[items][0]),inventory[items][1])
                        amountfunc(items)

def amountfunc(items):  #the function for determine the amount
    amount = raw_input("Adding " + items + ". Enter Amount:")
    into="Added "+items+" into your Basket.\nGoing back to main menu...\n"
    if amount=="0":
        main_menu()
    elif inventory[items][0]<int(amount):
        sorry_amount(into,items)
    elif inventory[items][0]>=int(amount)>0:
        basket[username][items] = (amount, inventory[items][1])
        print into
        main_menu()
    else:
        main_menu()

def sorry_amount(into,items):   #the function for user to get a warning about the stock
    sorry = raw_input("Sorry! The amount exceeds the limit, Please try again with smaller amount\n\t" + "Amount (Enter 0 for main menu):")   #the promt that is gonig to warn the users and ask them give another amount and saves it
    if sorry == "0":
        main_menu()
    elif inventory[items][0]<int(sorry):
        sorry_amount(into,items)
    elif inventory[items][0]>=int(sorry)>0:
        basket[username][items] = (sorry, inventory[items][1])
        print into
        main_menu()
    else:
        main_menu()

def see_basket():   #the function that displays users what is inside in their baskets
    totalprice=0
    i=1
    for shopping in basket[username]:
        totalprice +=float(basket[username][shopping][1]) * float(basket[username][shopping][0])
        basketprompt="\t"+str(i)+"."+str(shopping)+" price=$"+str(basket[username][shopping][1])+" amount=" +str(basket[username][shopping][0])+" total="+str(float(basket[username][shopping][1])*float(basket[username][shopping][0]))

        print basketprompt
        i=i+1
    print "Total $" + str(totalprice)+"\n"
    see_basket_menu()


def see_basket_menu():  #the function for user to see the sub menu in the basket section of the main menu
    seebasketmenu="Please Choose an option:\n\t1.Update amount\n\t2.Remove an item\n\t3.Check out\n\t4.Go back to main menu\n"
    print seebasketmenu
    sbmask=raw_input("Your selection:")
    if sbmask=="1":
        updateamount()
    elif sbmask=="2":
        delitem()
    elif sbmask=="3":
        checkout()
    elif sbmask=="4":
        main_menu()
    else:
        see_basket_menu()

def updateamount():     #The updadete amount function for user to be able to make changes in the amounts of the products that they added into their baskets
    changeamount=raw_input("Please select which item to change its amount:")
    i=0
    for items in basket[username]:
            i = i + 1
            if str(i) == changeamount:
                basket[username][items] = (items, inventory[items][0], inventory[items][1])
                updateamount_2(items)

def updateamount_2(items):  #the updateamout_2 function is for user to write the new amount they want
    changeamountnumber = raw_input("Please type the new amount:")
    nowbasket="Your basket now contains:\n"
    while True:
        if inventory[items][0]<int(changeamountnumber):
           update_amount3(items,nowbasket)
        else:
            basket[username][items] = (changeamountnumber, inventory[items][1])
            print nowbasket
            see_basket()

def update_amount3(items,nowbasket):    #the function for if inventory amount and users imput does not match
    sorry = raw_input("Sorry! The amount exceeds the limit, Please try again with smaller amount\n\t" + "Amount (Enter 0 for main menu):")  #asks user to write a new amount and saves it
    while True:
        if sorry == "0":
            main_menu()
        elif inventory[items][0] >= int(sorry):
            basket[username][items] = (sorry, inventory[items][1])
            print nowbasket
            return see_basket()
        elif inventory[items][0] < int(sorry):
            update_amount3(items,nowbasket)


def delitem():    # the function for deleting items from the inventory
    remove=raw_input("Please select which item to remove from your basket:")
    i = 0
    for items in basket[username]:
        i = i + 1
        if str(i) == remove:
            del[basket[username][items]]
            see_basket()


def checkout():     #this is th checkout function where user sees their bills and finish their shopping
    receipt="Processing your receipt...\n"+(7*"*")+"    Online Market    "+(8*"*")+"\n"+(36*"*")+"\n\t44 44 0 34\n\tonline.shop.com"+"\n"+(36*"-")  #the recipt is sets equal to the receipt value
    print receipt
    totalprice=0
    for shopping in basket[username]:
        totalprice += float(basket[username][shopping][1]) * float(basket[username][shopping][0])
        basketprompt = str(shopping) + " $" + str(basket[username][shopping][1]) + " amount=" + str(basket[username][shopping][0]) + " total=" + str(float(basket[username][shopping][1]) * float(basket[username][shopping][0]))

        print basketprompt
    receipt2=(36*"-")+"\n Total\t$"+str(totalprice)+"\n"+(36*"-")
    print receipt2
    print datetime.now().strftime('%Y-%m-%d %H:%M')
    print "Thank You for using our Market!"
    decrease_inventory()

def decrease_inventory():   #this is the final function of this program and after the checkout it decreeses the choosen amounts form the inventory.
    for items in basket[username]:
        if items in inventory:
            itemnumber=basket[username][items][0]
            inventory[items][0]-=int(basket[username][items][0])
    for items in basket[username]:
        if items in inventory:
            basket[username].clear()
        break
    main_menu()


print user()

#P.S The little mistakes that we couldnt fix

#1. in the first item selection part if you will write bigger than item number, its going back to asking username
#2. in the update amount selecting item part if you write bigger than basket total item number, its going back to asking username
#3. in the remove item part if you will write bigger than item number, its going back to asking username