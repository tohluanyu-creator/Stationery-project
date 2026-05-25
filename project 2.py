#It meant to import required libraries
import csv
import os
from stationery import Stationery
#To list all stationery items
newItems = []
#Menu display
menu = """
===============================================
  STATIONERY INVENTORY MANAGEMENT SYSTEM
===============================================
1 - To enter new stationery item
2 - To edit the stationery item
3 - To update the stationery item which was sold
4 - To display all the stationery items
5 - To save the list of all the stationery items in .CSV file
==============================================="""
#To call a function, to input new item
def input_number():
    global newItems
    print("Please key in necessary details of new items")
    #To input the item name
    itemName = input("Please enter the name of the item: ")
    #Ask for price with error handling
    while True:
        try:
            priceItem = float(input("Please enter the price of the item: "))
            break
        except:
            print("invalid, please enter number for the price")
    #Ask for the amount of items, with error handling
    while True:
        try:
            itemAmount = int(input("Please enter the amount of items: "))
            break
        except:
            print("Invalid, Please enter number for the item")
    #Use stationery class to calculate total price
    stationeryItem = Stationery(itemName, itemAmount, priceItem)
    totalPrice = stationeryItem.calculate_total()
    print(f"Total price of all {itemName}: ${totalPrice}")
    #store item details in a dictionary
    items = {
        "name": itemName,
        "quantity": itemAmount,
        "price": priceItem
    }
    #Add dictionary to the list
    newItems.append(items)
    print(f"The {itemName} item has been added successfully!")
#To call function, which edit the item which was stored
def edit_items():
    edit = input("Please select the item you wish to edit: ")
    #Assume the item is not found
    found = False
    #Search for item in the list
    for item in newItems:
        if item["name"] == edit:
            found = True
            #Ask for new name
            item["name"] = input("Enter new name: ")
            #Ask for new amount of item, and display an error if wrong
            while True:
                try:
                    item["quantity"] = int(input("Enter new quantity: "))
                    break
                except:
                    print("please input number")
            #Ask for new amount of price, and display an error if wrong
            while True:
                try:
                    item["price"] = float(input("Enter new price: "))
                    break
                except:
                    print("please enter number")
            print(f"The {edit} item has been updated successfully!")
            break
    #Display error if item not found
    if found == False:
        print(f"{edit} is not in the system, please input a correct name")
#Function to update quantity when times are sold
def update_items():
    update = input("Please select the item you wish to update: ")
    #Ask for an amount of item sold with error handling
    while True:
        try:
            quantitySold = int(input("Please enter the quantity sold: "))
            break
        except:
            print("Please enter the correct number of quantity sold")
    #Assume item is not found
    found = False
    #Search for the item in the list
    for item in newItems:
        if item["name"] == update:
            found = True
            #subtract quantity sold and calculate money gained
            item["quantity"] = item["quantity"] - quantitySold
            moneyGained = quantitySold * item["price"]
            print(f"The {update} item has been updated successfully!")
            print(f"You have sold {quantitySold} {update} and gained ${moneyGained}")
            print(f"Remaining quantity: {item['quantity']}")
            break
    #Display error if item not found
    if found == False:
        print(f"{update} is not in the system, please input a correct name")
#Function to display all stationery items in table format
def display_items():
    if len(newItems) == 0:
        print("No items in the system!")
    else:
        # Print header row
        print("\n================================================")
        print(f"{'Name':<15} {'Quantity':<10} {'Price':<10} {'Total Price':<10}")
        print("================================================")

        # Print each item in table format
        for item in newItems:
            totalPrice = item["quantity"] * item["price"]
            print(f"{item['name']:<15} {item['quantity']:<10} ${item['price']:<10} ${totalPrice:<10}")

        print("================================================")
#Function to save all items to a csv file
def save_items():
    with open("stationery.csv", "w") as file:
        writer = csv.writer(file)
        
        #Write header row
        writer.writerow(["Name", "Quantity", "Price", "Total Price"])
        
        #Write each item as a row
        for item in newItems:
            totalPrice = item["quantity"] * item["price"]
            writer.writerow([item["name"], item["quantity"], item["price"], totalPrice])
    
    print("File saved successfully as stationery.csv!")

#Main loop to keep program running until user exists
while True:

    print(menu)
    option = input("Enter option: ")

    if option == "1":
        input_number()

    elif option == "2":
        edit_items()

    elif option == "3":
        update_items()

    elif option == "4":
        display_items()

    elif option == "5":
        save_items()

    else:
        print("Invalid option! Please enter a number from 1 to 5.")
    #Ask the user if they want to keep using the system
    moreInput = input("Do you wish to continue using this system (yes/no): ").strip().lower()
    if moreInput == "no":
        print("Thank you for using our system. Goodbye!")
        break
    else:
        #Remove screen and go back to menu
        os.system('cls' if os.name == 'nt' else 'clear')