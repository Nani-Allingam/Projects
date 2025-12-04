#Super Market Bill Generation

from datetime import datetime  # import date time
name = input("Enter your name: ")   #get customer name

products = '''
Rice    Rs 50
sugar   Rs 44
Oil     Rs 142
maggie  Rs 80
boost   Rs 10
panneer Rs 100
almonds Rs 400
'''
#Initializing variables 
price = 0
finalprice = 0
totalprice =0
pricelist =[]  #includes item,quanity,price
ilist = []      # item list
qlist =[]       # quantity list
plist =[]       # price list

#creating dictionary for items and their prices

items = {"rice":50,'sugar':44,'oil':142,'maggie':80,'boost':10,'panneer':100,'almonds':400}

#show items if customer enters 1
option = int(input("For list of items enter 1: "))
if option ==  1:
    print(products)

#loop for item is in the list or not
for i in range(len(items)):
    inp1 = int(input("Enter 1 for shopping or 2 for exit: ")) # ask if user wants to buy or exit
    if inp1 == 2:
       break
    if inp1 == 1:                                  #check if item is valid and calculate price
       item = input("Enter the item: ")
       quantity = int(input("Enter the quantity: "))
       if item in items.keys():
            price = quantity*(items[item])
            pricelist.append((item,quantity,price))
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            totalprice += price
            gst = (totalprice*5)/100         #calculating gst and totalprice
            finalprice = gst + totalprice
       else:
            print("Item not available")            #if item is not found display not available
    else:
        print("Invalid input")              #handling invalid input
    inp2 = input("Can I print the bill(Select yes or no): ")   #asking if user wants to generate the bill or not
    if inp2 == 'yes':
        pass
        if finalprice != 0:
            print("="*30,"Nani's Super Marker",'='*30)            #printing the final bill
            print(" "*35,'Tirupat')
            print("Name: ",name, ' '*30,'Date: ',datetime.now())
            print('-'*75)
            print("Sno",' '*8,'Items',' '*10,'Quantity',' '*5,"Price")   #prints header
            print('-'*75)
            for i in range(len(pricelist)):
                print(i,' '*10,ilist[i],' '*(17-len(ilist[i])),qlist[i]," "*10,plist[i])   #prints each purchased item
            print('-'*75)
            print(' '*50,'Totalprice: ', "Rs" , totalprice)
            print("gst amount"," "*52, "Rs" , gst)
            print('-'*75)
            print(" "*50,"Final amount: ", 'Rs',finalprice)   #prints final price including gst
            print("-"*75)
            print(" "*50,"Thank You")
            print(" "*50,"Visit again")    #thankyou note
