#create a subrountine for the breadtype
from datetime import date

today = date.today()
print("Today's date:", today)

#this function checks if the user name is vaild
def force_name(message, lower, upper):
    while True:
        name= str(input(message)).title()
        if len(name) >=lower and len(name) <=upper and name.isalpha() :
            break
        else:
            print("Error, {}. No numbers please and between {} to {} words".format(message, lower, upper))
    return name

def get_phone_number(message): #Runs a message through this program
    while True: #while true loop to filter bad data
        try:
            phone_number = str(input(message)) #asks for phone number or 0 to quite.
            if len(phone_number) >= 9 and len(phone_number) <= 12 and phone_number.isnumeric(): #if the length is 9 to 12
                break #breaks function if specifications are met.
            else:
                print("Cellphone numbers only contain number and are between 9 and 12 digits") #Tells if user invalid input
        except:
            print("Please enter a vaild phone number") #tells user to enter correct phone number
    return phone_number #will return value to variable that called the function

def item_check(item_list):
    while True:
        try:
            item_amount = len(item_list)
            item_type = int(input("Please enter your selected item type 0 - {}".format(item_amount - 1)))
            if item_type >= 0 and item_type < len(item_list):
                break
            else:
                print("ERROR!! Please enter a number from 0 to ",len(item_list - 1))
        except:
            print("ERROR!! Please enter in a number not text")
    return item_type

def print_lists(lists, item):
    print("We have the following {}".format(item))
    count=0
    while count <len(list):
        print(count," ",list[count])
        count += 1
    choice = item_check(list) #this calls the item check function to ensure a vaild number is entered
    choice = list[choice]
    return choice

def salads():
    global saladtype, saladlist, saladwanted
    saladlist = ["Lettuce","Tomato","Carrot", "Cucumber","Onions"]
    saladcount = 0
    print("We have the following salads, you can have as many as you want")
    while saladcount < len(saladlist):
        print(saladcount," ",saladlist[saladcount])
        saladcount = saladcount + 1
    print("Press ENTER when you have finished choosing your salads")
    saladwanted = " "
    saladtype = " "
    while saladtype != "":
        saladtype = input("What number salad do you want?")
        if saladtype != "":
            saladtype = int(saladtype)
            saladwanted = saladwanted + " " + saladlist[saladtype]

def output_order():
    breadorder=[] #empty list
    #this adds the persons entire order details to the list.
    breadorder.append(first_name)
    breadorder.append(cellphone)
    breadorder.append(breadlist[breadtype])
    breadorder.append(meatlist[meatype])
    breadorder.append(cheeselist[cheesetype])
    breadorder.append(saladwanted)
    breadorder.append(dressinglist[dressingtype])
    breadorder.append(today)
    outputFile = open("sams_order.txt", "a") #opens the text file
    print("*********************** Order for {} - {} ********\n".format(first_name, cellphone)) #text rpint in pyscripter
    outputFile.write("************ Order for {} - {} ********\n".format(first_name, cellphone))
    for order in breadorder:
        print("Order") # test rpint in pyscripter
        outputFile.write("{}\n".format(order))
    outputFile.write("***************** End of Order: {}. ************".format(today)) #test to print out in pyscripter
    outputFile.close() #clsoes tex file


#Main porgram
first_name = force_name("Please enter in your name",2,10)
cellphone = get_phone_number("Please enter your phone number")

breadlist = ["white", "Brown", "Italian", "Granary"]
meatlist = ["Pepperoni", "Chicken", "Italian B.M.T", "MeatBalls","Turkey"]
cheeselist = ["Cheddar", "Mozzarella", "Parmesan", "American","Swiss"]
dressinglist = ["Habanero Hot Sauce", "Smoky BBQ", "Honey Mustard", "Chipotle Southwest"]
bread_selected = print_lists(breadlist, bread)
meat_selected = print_lists(meatlist, meat)
cheese_selected = print_lists(cheeselist, cheese)
salads()
dressings_selected = print_lists(dressinglist, dressing)
output_order()
