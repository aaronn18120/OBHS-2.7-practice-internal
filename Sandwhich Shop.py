#create a subrountine for the breadtype
from datetime import date

today = date.today()
print("Today's date:", today)

def breads():
    global breadtype, breadlist
    breadlist = ["white", "Brown", "Italian", "Granary"]
    breadcount = 0
    print("We have the following breads")
    while breadcount < len(breadlist):
        print(breadcount,"  ", breadlist[breadcount])
        breadcount = breadcount + 1
    breadtype = int(input("What number bread do you want?"))

def meat():
    global meatype, meatlist
    meatlist = ["Pepperoni", "Chicken", "Italian B.M.T", "MeatBalls","Turkey"]
    meatcount = 0
    print("We have the following meats")
    while meatcount < len(meatlist):
        print(meatcount,"  ", meatlist[meatcount])
        meatcount = meatcount + 1
    meatype = int(input("What meat number do you want?"))

def cheese():
    global cheesetype, cheeselist
    cheeselist = ["Cheddar", "Mozzarella", "Parmesan", "American","Swiss"]
    cheesecount = 0
    print("We have the following cheese")
    while cheesecount < len(cheeselist):
        print(cheesecount,"  ", cheeselist[cheesecount])
        cheesecount = cheesecount + 1
    cheesetype = int(input("What cheese number do you want?"))

def dressing():
    global dressingtype, dressinglist
    dressinglist = ["Habanero Hot Sauce", "Smoky BBQ", "Honey Mustard", "Chipotle Southwest"]
    dressingcount = 0
    print("We have the following dressings")
    while dressingcount < len(dressinglist):
        print(dressingcount,"  ", dressinglist[dressingcount])
        dressingcount = dressingcount + 1
    dressingtype = int(input("What number dressings do you want?"))

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
    print("*********************** Order for {} - {} ********".format(first_name, cellphone)) #text rpint in pyscripter
    outputFile.write("************ Order for {} - {} ********".format(first_name, cellphone))
    for order in breadorder:
        print("Order") # test rpint in pyscripter
        outputFile.write("{}\n".format(order))
    outputFile.write("***************** End of Order: {}. ************".format(today)) #test to print out in pyscripter
    outputFile.close() #clsoes tex file


#Main porgram
first_name = str(input("Please enter in your name")).title()
cellphone = str(input("Please enter in your cellphone"))
breads()
meat()
cheese()
salads()
dressing()
output_order()
