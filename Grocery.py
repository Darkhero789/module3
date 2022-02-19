class Main:
    def Main():
        #The intro and main function of the program. 
        #It is the most used function of the code as the user will always come back to this function until they finish the program.
        print("Welcome to the grocery list program")
        items = []
        prices = []
        quantities = []
        loop = True
        found = False
        while loop == True:
            #This loop is the main piece of coding for the program. 
            #It allows the user to tell the program what they want to do and connects to the rest of the program. 
            #The program gives the user 5 choices 
            #Add an item 
            #Change an items price
            #Change an items quantity
            #Delete an item
            #or finish the program
            print("Please choose one of the following options by inputting their number.")
            print("1. add item")
            print("2. change price of item")
            print("3. change quantity of the item")
            print("4. delete an item")
            print("5. Finish program and give the total price")
            choice = int(input(""))
            if choice == 1:
                #This piece of code is used to add an item onto the grocery list
                List = Grocery.One()
                items.append(List[0])
                prices.append(List[1])
                quantities.append(List[2])
                print("Grocery list")
                length = len(items)
                for i in range(length):
                    print(f"{items[i]} ${prices[i]} #{quantities[i]}")
            elif choice == 2:
                #The code here changes the price of a previously added item in the grocery list
                change = Grocery.Two()
                length = len(items)
                for i in range(length):
                    if items[i] == change[0]:
                        place = i
                        found = True
                if found == True:
                    prices[place] = change[1]
                    print("Updated grocery list")
                    for i in range(length):
                        print(f"{items[i]} ${prices[i]} #{quantities[i]}")
                else:
                    print("Item not found.")
            elif choice == 3: 
                #Like the last piece of code this alters an item on the grocery list, however this alters the quantity of the item
                change = Grocery.Three()
                length = len(items)
                for i in range(length):
                    if items[i] == change[0]:
                        place = i
                        found = True
                if found == True:
                    quantities[place] = change[1]
                    print("Updated grocery list")
                    for i in range(length):
                        print(f"{items[i]} ${prices[i]} #{quantities[i]}") 
                else:
                    print("Item not found")
            elif choice == 4:
                item = Grocery.Four()
                length = len(items)
                for i in range(length):
                    if items[i] == item:
                        place = i
                        found = True
                if found == True:
                    print(f"{items.pop(place)} {prices.pop(place)} {quantities.pop(place)}")
                    print("These have been removed")
                    length = len(items)
                    for i in range(length):
                        print(f"{items[i]} {prices[i]} {quantities[i]}")
                else:
                    print("Item not found")
            elif choice == 5:      
                #This is what is used to end the program and gives you the total price of the items.          
                length = len(items)
                total = 0
                for i in range(length):
                    print(f"{items[i]} ${prices[i]} #{quantities[i]}") 
                    total += float(prices[i]) * int(quantities[i])
                total = round(total,2)
                print(f"Total: {total}")
                loop = False
            else:
                print("Sorry that is not an option")
        
class Grocery:
    def One():
        #This function is mainly just to ask the user for the item name, price, and quantity variables. 
        #It then puts them in a list and sends them back to the main class and function
        item = input("What is the name of the item? ").lower()
        price = input("What is the item's price? ")
        quantity = input("How many are you getting? ")
        list = [item, price, quantity]
        return list
    def Two():
        #Like the last function this one just asks for the variables the user wants to change before it sends them back to the main class to alter the data.
        #This function asks for the item name and price variable so that the main class can change the price of the item.
        item = input("Which item are you changing? ").lower()
        price = input("What is the new price of the item? ")
        changes = [item, price]
        return changes
    def Three():
        #This function is a lot like the last function in that it asks for variables to alter an item. 
        #this one however asks for name and quantity so that the main class can change the quantity of the item.
        item = input("Which item are you changing? ").lower()
        quantity = input("what is the new amount of the item? ")
        changes = [item, quantity]
        return changes
    def Four():
        item = input("Which item are you wanting to delete? ")
        return item

if __name__ == "__main__":
    Main.Main()
